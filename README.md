Interactive Dashboard Web App

A fully-featured, interactive dashboard built with Flask, designed to help you track your day-to-day activities. It combines weather updates, news, quotes, diary notes, expenses tracking, and a calendar in one polished interface.

Features

Login & Registration with validation and warnings for invalid credentials

Dashboard Home:

Interactive weather card 🌤

News cards with hover effects and emojis 📰

Random motivational quotes 💡

Diary: Add, view, and manage personal notes

Expenses Tracker: Keep track of your spending

Calendar: Embedded Google Calendar

Dark Mode toggle for all pages

Responsive design with animations and hover effects

Folder Layout
project-root/
  app.py                  # Main Flask application
  database/
    data.db               # SQLite database
  modules/
    weather.py            # Fetch weather data
    news.py               # Fetch news data
    quotes.py             # Fetch motivational quotes
  static/
    css/
      style.css           # Dashboard styling
      login.css           # Login/Register styling
  templates/
    base.html             # Dashboard layout
    base_login.html       # Login/Register layout
    login.html
    register.html
    home.html
    diary.html
    expenses.html
    calendar.html
  README.md
How to Use

Register a new account or log in with an existing one.

Navigate the dashboard using the sidebar: Home, Diary, Expenses, Calendar.

Add notes in the diary or track expenses directly from their respective pages.

Toggle dark mode using the button at the top-right for a night-friendly theme.

Weather and news sections are interactive and show updated data with a modern, animated UI.

APIs

Weather: Custom Python module (weather.py) – can connect to OpenWeatherMap or other APIs

News: Custom Python module (news.py) – uses public news APIs

Quotes: https://api.quotify.top/random for motivational quotes

Styling & Interactivity

Responsive design using flexbox and grid

Hover effects on cards, buttons, and links

Subtle animations for content and notifications

Emojis and stickers to make the interface more engaging

Dark mode compatible across all pages

Future Improvements

Add charts and graphs for expense trends

Include profile settings and avatars

Real-time updates for weather and news

Drag-and-drop functionality for diary notes
