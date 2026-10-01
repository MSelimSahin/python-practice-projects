# Flight Deals Tracker

Belirlenen hedef fiyatın altına düşen uçuşları Amadeus API üzerinden takip edip, Sheety API ile Google Sheets'te tutulan kullanıcı listesine e-posta bildirimi gönderen çok modüllü bir uygulama.

**Kullanılanlar:** Python, Amadeus API, Sheety API, SMTP

**Dosya yapısı:**
- `main.py` — ana akış
- `data_manager.py` — Sheety API ile veri okuma/yazma
- `flight_search.py` — Amadeus API ile uçuş arama
- `flight_data.py` — uçuş verisi modeli
- `notification_manager.py` — e-posta bildirimi

**Çalıştırma:**
```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```
