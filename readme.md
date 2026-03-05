# Personal Assistant Dashboard

A web-based personal assistant dashboard built with **Flask**. This project integrates weather updates, news, motivational quotes, a calendar, diary, and expense tracking in a clean, interactive interface. The dashboard supports **dark mode**, animations, and hover effects for an engaging user experience.

---

## Features

- **User Authentication**
  - Login and registration system with secure session management.
  - Validation messages for wrong credentials or missing fields.

- **Dashboard**
  - Displays weather, news, and a motivational quote on the homepage.
  - Interactive cards with hover effects and animations.

- **Diary**
  - Add, view, and manage personal notes.
  - Notes are saved per user in SQLite.

- **Expenses**
  - Add, view, and track expenses by category.
  - Interactive table with hover highlights.

- **Calendar**
  - Embedded Google Calendar for scheduling and holidays.

- **News**
  - Live news feed with auto-slider animations and visually appealing cards.

- **Dark Mode**
  - Toggle between light and dark themes with smooth transitions.

---
```
## Project Structure
project-root/
├─ app.py                  # Main Flask application
├─ database/
│   └─ data.db             # SQLite database
├─ modules/
│   ├─ weather.py          # Fetch weather data
│   ├─ news.py             # Fetch news data
│   └─ quotes.py           # Fetch motivational quotes
├─ static/
│   └─ css/
│       ├─ style.css       # Dashboard styling
│       └─ login.css       # Login/Register styling
├─ templates/
│   ├─ base.html           # Dashboard layout
│   ├─ base_login.html     # Login/Register layout
│   ├─ login.html
│   ├─ register.html
│   ├─ home.html
│   ├─ diary.html
│   ├─ expenses.html
│   └─ calendar.html
└─ README.md
```

## How to Use

1. Register a new account or log in with an existing one.  
2. Navigate the dashboard using the sidebar: **Home**, **Diary**, **Expenses**, **Calendar**.  
3. Add notes in the diary or track expenses directly from their respective pages.  
4. Toggle dark mode using the button at the top-right for a night-friendly theme.  
5. Weather and news sections are interactive and show updated data with a modern, animated UI.  

---

## APIs

- **Weather**: Custom Python module (`weather.py`) – can connect to OpenWeatherMap or other APIs  
- **News**: Custom Python module (`news.py`) – uses public news APIs  
- **Quotes**: [Quotify API](https://api.quotify.top/random) for motivational quotes  

---

## Styling & Interactivity

- Responsive design using **flexbox** and **grid**  
- **Hover effects** on cards, buttons, and links  
- Subtle **animations** for content and notifications  
- **Emojis and stickers** to make the interface more engaging  
- **Dark mode** compatible across all pages  

---

## Future Improvements

- Add **charts and graphs** for expense trends  
- Include **profile settings** and avatars  
- **Real-time updates** for weather and news  
- **Drag-and-drop functionality** for diary notes  