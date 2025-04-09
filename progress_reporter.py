import datetime

def generate_report():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
🛠️ RAPORT POSTĘPU PRAC NAD BOTEM DO NIERUCHOMOŚCI
Data i godzina generacji: {now}

1. 🔍 Moduł wyszukiwania okazji inwestycyjnych:
   - Status: ✅ Zakończony
   - Opis: Analizuje oferty z wielu źródeł i filtruje okazje.
   - Progres: 100%

2. 🧠 AI do szacowania kosztów remontu:
   - Status: 🔄 W toku
   - Opis: Wersja beta, uczy się na podstawie zdjęć i opisów.
   - Progres: 60%

3. 📉 Analiza opłacalności:
   - Status: 🕓 Oczekuje na dane wejściowe z AI
   - Opis: Moduł oceniający zysk z inwestycji.
   - Progres: 30%

4. 📍 Wykresy, mapy, zdjęcia, filtry:
   - Status: ✅ Zakończony
   - Opis: GUI pokazujące dane w przejrzysty sposób.
   - Progres: 100%

5. 🔔 System powiadomień:
   - Status: 🔄 W toku
   - Opis: Powiadomienia Telegram + email
   - Progres: 70%

6. 🗂️ Historia i raporty:
   - Status: 🔄 W toku
   - Opis: System logów i eksportów ofert
   - Progres: 85%

💡 Całkowity postęp: około 74%

"""
    return report
