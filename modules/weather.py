import requests

API_KEY = "9dbdfb2a0d1191a8ee478cb0ca77524b"

def get_weather():

    city = "Hyderabad"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    r = requests.get(url).json()

    if "main" not in r:
        return {
            "city": city,
            "temp": "N/A",
            "desc": "Weather unavailable"
        }

    return {
        "city": city,
        "temp": r["main"]["temp"],
        "desc": r["weather"][0]["description"]
    }