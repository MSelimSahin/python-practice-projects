# Python Practice Projects

Python öğrenirken geliştirdiğim küçük ve orta ölçekli pratik projelerin bir araya toplandığı repo. Her klasör bağımsız bir projedir; API entegrasyonu, otomasyon, GUI (Tkinter) ve oyun geliştirme gibi farklı konuları kapsar.

## Projeler

| Proje | Açıklama | Teknolojiler |
|---|---|---|
| [rain-alert-weather-bot](./rain-alert-weather-bot) | Hava durumu API'sinden yağmur tahminini kontrol edip e-posta ile uyarı gönderen bot | Python, REST API, SMTP |
| [stock-news-alert](./stock-news-alert) | Hisse senedi fiyatındaki ani değişimi tespit edip ilgili haberleri e-posta ile bildiren uygulama | Python, Alpha Vantage API, News API, SMTP |
| [flight-deals-tracker](./flight-deals-tracker) | Uçuş fiyatlarını takip edip hedef fiyatın altına düşünce bildirim gönderen çok modüllü uygulama | Python, Amadeus API, Sheety API, SMTP |
| [password-manager-gui](./password-manager-gui) | Rastgele güçlü şifre üreten ve şifreleri yerel olarak saklayan masaüstü uygulaması | Python, Tkinter, JSON |
| [oop-coffee-machine](./oop-coffee-machine) | Nesne yönelimli programlama prensipleriyle geliştirilmiş kahve makinesi simülasyonu | Python, OOP |
| [quiz-game](./quiz-game) | Open Trivia DB API'sinden soru çekip kullanıcıyı test eden bilgi yarışması uygulaması | Python, REST API, OOP |
| [pomodoro-timer](./pomodoro-timer) | Pomodoro tekniğiyle çalışma/mola sürelerini yöneten masaüstü zamanlayıcı | Python, Tkinter |
| [turtle-crossing-game](./turtle-crossing-game) | Klasik "yolu geç" oyununun Python Turtle grafik kütüphanesiyle yapılmış versiyonu | Python, Turtle, OOP |
| [nato-alphabet-converter](./nato-alphabet-converter) | Girilen bir kelimeyi NATO fonetik alfabesine çeviren konsol uygulaması | Python, CSV, Dictionaries |
| [flask-blog-contact-form](./flask-blog-contact-form) | Flask ile geliştirilmiş, iletişim formu içeren basit bir blog uygulaması | Python, Flask, HTML/CSS |

## Kurulum

Her proje kendi klasöründe bağımsız çalışır. Bir projeyi denemek için:

```bash
cd proje-adi
pip install -r requirements.txt  # varsa
python main.py
```

API anahtarı veya e-posta bilgisi gerektiren projelerde (`rain-alert-weather-bot`, `stock-news-alert`, `flight-deals-tracker`), klasör içindeki `.env.example` dosyasını `.env` olarak kopyalayıp kendi bilgilerinizi girmeniz gerekir:

```bash
cp .env.example .env
```

## Not

Bu projeler öğrenme sürecinde, çoğunlukla "100 Days of Code" tarzı bir Python bootcamp'i takip ederken geliştirilmiştir. Amaç farklı konularda (API entegrasyonu, GUI, otomasyon, OOP) pratik yapmaktı.
