# Python Practice Projects

A collection of small to medium-sized Python projects built while learning Python. Each folder is an independent project covering different topics: API integration, automation, GUI development (Tkinter), and game development.

## Projects

| Project | Description | Tech Stack |
|---|---|---|
| [rain-alert-weather-bot](./rain-alert-weather-bot) | Checks the weather forecast via an API and sends an email alert if rain is expected | Python, REST API, SMTP |
| [stock-news-alert](./stock-news-alert) | Detects sudden stock price changes and emails related news articles | Python, Alpha Vantage API, News API, SMTP |
| [flight-deals-tracker](./flight-deals-tracker) | Tracks flight prices and sends a notification when they drop below a target price | Python, Amadeus API, Sheety API, SMTP |
| [password-manager-gui](./password-manager-gui) | Desktop app that generates strong random passwords and stores them locally | Python, Tkinter, JSON |
| [oop-coffee-machine](./oop-coffee-machine) | A coffee machine simulation built with object-oriented programming principles | Python, OOP |
| [quiz-game](./quiz-game) | A trivia quiz app that pulls questions from the Open Trivia Database API | Python, REST API, OOP |
| [pomodoro-timer](./pomodoro-timer) | A desktop timer that manages work/break intervals using the Pomodoro technique | Python, Tkinter |
| [turtle-crossing-game](./turtle-crossing-game) | A classic "cross the road" arcade game built with Python's Turtle graphics library | Python, Turtle, OOP |
| [nato-alphabet-converter](./nato-alphabet-converter) | Converts an input word into the NATO phonetic alphabet | Python, CSV, Dictionaries |
| [flask-blog-contact-form](./flask-blog-contact-form) | A simple blog application built with Flask, including a contact form | Python, Flask, HTML/CSS |

## Setup

Each project runs independently from its own folder. To try one out:

```bash
cd project-name
pip install -r requirements.txt  # if present
python main.py
```

For projects that require an API key or email credentials (`rain-alert-weather-bot`, `stock-news-alert`, `flight-deals-tracker`), copy the `.env.example` file in that folder to `.env` and fill in your own values:

```bash
cp .env.example .env
```

## Note

These projects were built while following a Python bootcamp-style curriculum ("100 Days of Code"). The goal was to practice different areas: API integration, GUI development, automation, and OOP.
