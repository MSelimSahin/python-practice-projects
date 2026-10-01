# Flight Deals Tracker

A multi-module application that tracks flights below a target price via the Amadeus API and emails a list of users (stored in a Google Sheet via the Sheety API) when a deal is found.

**Tech stack:** Python, Amadeus API, Sheety API, SMTP

**File structure:**
- `main.py` — main flow
- `data_manager.py` — reads/writes data via the Sheety API
- `flight_search.py` — searches flights via the Amadeus API
- `flight_data.py` — flight data model
- `notification_manager.py` — sends email notifications

**Run it:**
```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```
