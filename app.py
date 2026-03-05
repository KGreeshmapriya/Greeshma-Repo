from flask import Flask, render_template, redirect, request, session, url_for, jsonify
import sqlite3
from functools import wraps
from modules.weather import get_weather
from modules.news import get_news
from modules.quotes import get_quote
app = Flask(__name__)
app.secret_key = "super_secret_key"
DB = "database/data.db"

# --- DB INIT ---
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS diary(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            note TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- LOGIN REQUIRED DECORATOR ---
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# --- LOGIN ---
@app.route("/login", methods=["GET","POST"])
def login():
    message = ""
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT id FROM users WHERE username=? AND password=?", (username,password))
        user = c.fetchone()
        conn.close()
        if user:
            session["user_id"] = user[0]
            return redirect(url_for("home"))
        else:
            message = "❌ Invalid username or password!"
    return render_template("login.html",message = message)

# --- REGISTER ---
@app.route("/register", methods=["GET","POST"])
def register_page():
    message = ""
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            c.execute("INSERT INTO users(username,password) VALUES (?,?)", (username,password))
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            message = "❌ Username already exists!"
    return render_template("register.html",message = message)

# --- LOGOUT ---
@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for("login"))

# --- HOME / DASHBOARD ---
@app.route("/")
@login_required
def home():
    weather = get_weather()
    quote = get_quote()
    news = get_news()
    return render_template("home.html", weather=weather, quote=quote, news=news)

# --- DIARY ---
@app.route("/diary", methods=["GET","POST"])
@login_required
def diary():
    user_id = session["user_id"]
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    if request.method=="POST":
        note = request.form["note"]
        c.execute("INSERT INTO diary(user_id,note) VALUES (?,?)", (user_id,note))
        conn.commit()
    c.execute("SELECT id,note FROM diary WHERE user_id=?", (user_id,))
    notes = c.fetchall()
    conn.close()
    return render_template("diary.html", notes=notes)

# --- EXPENSES ---
@app.route("/expenses", methods=["GET","POST"])
@login_required
def expenses():
    user_id = session["user_id"]
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    if request.method=="POST":
        category = request.form["category"]
        amount = request.form["amount"]
        c.execute("INSERT INTO expenses(user_id,category,amount) VALUES (?,?,?)", (user_id,category,amount))
        conn.commit()
    c.execute("SELECT id,category,amount FROM expenses WHERE user_id=?", (user_id,))
    expenses = c.fetchall()
    conn.close()
    return render_template("expenses.html", expenses=expenses)

# --- CALENDAR ---
@app.route("/calendar")
@login_required
def calendar():
    return render_template("calender.html")

if __name__ == "__main__":
    app.run(debug=True)


    