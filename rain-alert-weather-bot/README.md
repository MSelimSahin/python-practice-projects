# Rain Alert Weather Bot

A simple automation script that fetches the hourly weather forecast from the OpenWeatherMap API and sends an email alert if rain is expected.

**Tech stack:** Python, `requests`, SMTP (Gmail), `python-dotenv`

**Run it:**
```bash
pip install -r requirements.txt
cp .env.example .env   # fill in your own API key and email credentials
python main.py
```
