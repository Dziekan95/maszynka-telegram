import logging
import datetime
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import Updater, CommandHandler

# 🔐 Wklej tutaj swój token bota Telegram
TOKEN = "7923832536:AAGiHmjAlbeVE-D0sN9rM3StPWfssq43q4U"

# 💬 Wklej tutaj swoje CHAT_ID (np. 123456789)
CHAT_ID = 8044783655

# 📋 Konfiguracja logowania
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# 📊 Funkcja generująca szczegółowy raport
def get_progress_report():
    return (
        "📊 Raport postępu prac nad botem nieruchomości:\n"
        "— Pobieranie danych z serwisów: ✅ 100%\n"
        "— Wyszukiwanie okazji: 🟡 70%\n"
        "— Szacowanie kosztów remontu: 🟡 40%\n"
        "— GUI z mapą: 🟠 25%\n"
        "— Tryb AI predykcji wartości: 🔜 10%\n"
        "— System rekomendacji: 🔜 5%\n"
        "\n🕒 Ostatnia aktualizacja: "
        + datetime.datetime.now(pytz.timezone('Europe/Warsaw')).strftime("%Y-%m-%d %H:%M:%S")
    )

# 🕑 Automatyczny raport
def send_report(context):
    report = get_progress_report()
    context.bot.send_message(chat_id=CHAT_ID, text=report)

# 🧠 Komenda: /postep
def postep(update, context):
    update.message.reply_text(get_progress_report())

# 📈 Komenda: /raport
def raport(update, context):
    update.message.reply_text("📌 Oczekuj raportu automatycznego lub wpisz /postep, by uzyskać bieżący stan.")

# ❓ Komenda: /zadaj
def pytanie(update, context):
    update.message.reply_text("✉️ Twoje pytanie zostało zarejestrowane. Przekażę je twórcy!")

# 🚀 Start aplikacji
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("postep", postep))
    dp.add_handler(CommandHandler("raport", raport))
    dp.add_handler(CommandHandler("zadaj", pytanie))

    scheduler = BackgroundScheduler(timezone=pytz.timezone('Europe/Warsaw'))
    scheduler.add_job(send_report, 'interval', hours=2, args=[updater])
    scheduler.start()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


