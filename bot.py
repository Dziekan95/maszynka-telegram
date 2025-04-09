from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
from datetime import datetime
import threading
import time

# 🔐 TOKEN z BotFather – wklej swój
TOKEN = '7923832536:AAGiHmjAlbeVE-D0sN9rM3StPWfssq43q4U'

# 📁 Ścieżka do pliku z chat_id
chat_id_file = "telegram_bot/chat_id.txt"

# ✅ Funkcja startowa – zapisuje ID i wysyła info
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    update.message.reply_text("Cześć, mistrzu! Maszynka działa 🛠️ Raport co 2 godziny włączony.")
    with open(chat_id_file, "w") as f:
        f.write(str(chat_id))

# 🧠 Funkcja generująca szczegółowy raport
def generate_raport():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Lista postępów (nazwa, status, procent)
    postepy = [
        ("🔎 Scraper Otodom", "✔️", 100),
        ("📥 Scraper OLX", "✔️", 100),
        ("💬 Scraper Facebook (beta)", "🛠️", 40),
        ("⚖️ Aukcje komornicze", "✔️", 100),
        ("📸 Analiza zdjęć (AI)", "🛠️", 35),
        ("📝 Opisy NLP (standard mieszkania)", "✔️", 100),
        ("🏗️ Szacowanie remontu (AI)", "🛠️", 60),
        ("📍 Ocena lokalizacji (mapy)", "🛠️", 75),
        ("📈 Wskaźnik opłacalności", "✔️", 100),
        ("🧠 Scoring inwestycyjny", "🛠️", 50),
        ("🧾 Interfejs użytkownika (GUI)", "🛠️", 30),
        ("🤖 Wersja Telegram", "✔️", 100),
        ("📤 Raporty automatyczne", "✔️", 100)
    ]

    # Oblicz całościowy postęp
    srednia = sum(p[2] for p in postepy) / len(postepy)

    # Formatowanie raportu
    raport = f"📊 R A P O R T  M A S Z Y N K I\n🕒 {now}\n\n"
    raport += "📌 Postęp prac:\n"
    for nazwa, status, procent in postepy:
        raport += f"{nazwa.ljust(35)} {status} {procent}%\n"

    raport += f"\n🔢 Całkowity postęp: {round(srednia)}%\n"
    raport += f"⏰ Kolejny raport za 2 godziny."

    return raport

# 🔁 Funkcja do automatycznego raportu
def auto_report(app):
    while True:
        try:
            with open(chat_id_file) as f:
                chat_id = int(f.read().strip())
            text = generate_raport()
            app.bot.send_message(chat_id=chat_id, text=text)
        except Exception as e:
            print(f"Błąd przy wysyłaniu raportu: {e}")
        time.sleep(2 * 60 * 60)  # 2 godziny

# 🆕 Komenda: /raport – ręczne wysłanie raportu
def raport(update: Update, context: CallbackContext):
    text = generate_raport()
    update.message.reply_text(text)

# 🆕 Komenda: /wersja – pokazuje info o wersji
def wersja(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Maszynka do zarabiania hajsu\nWersja: 1.1.0\nAktualizacja: 2025-04-09")

# 🚀 Główna funkcja
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("raport", raport))
    dp.add_handler(CommandHandler("wersja", wersja))

    threading.Thread(target=auto_report, args=(updater,), daemon=True).start()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

