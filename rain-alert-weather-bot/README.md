# Rain Alert Weather Bot

OpenWeatherMap API'sinden önümüzdeki saatlerin hava durumu tahminini çeken ve yağmur ihtimali varsa e-posta ile uyarı gönderen basit bir otomasyon scripti.

**Kullanılanlar:** Python, `requests`, SMTP (Gmail), `python-dotenv`

**Çalıştırma:**
```bash
pip install -r requirements.txt
cp .env.example .env   # kendi API anahtarını ve e-posta bilgilerini gir
python main.py
```
