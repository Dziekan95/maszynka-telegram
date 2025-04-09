import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

# Token Twojego bota
BOT_TOKEN = "7923832536:AAGiHmjAlbeVE-D0sN9rM3StPWfssq43q4U"

# Twoje ID Telegram (czat ID)
CHAT_ID = 8044783655  # Zmienimy na Twój numer w KROKU 7

# Ustawienia logowania
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Lista szczegółowych zadań i ich status
tasks = [
    ("✅ Stworzenie repozytorium i integracja z Render", 100),
    ("🧠 Implementacja interfejsu użytkownika (GUI)", 70),
    ("🛠 AI do analizy kosztów remontu", 50),
    ("📍 Integracja map z lokalizacją", 40),
    ("🔍 Filtrowanie ofert + analiza opłacalności", 65),
    ("🧾 Generowanie logów i historii analiz", 80),
    ("📤 Wysyłanie raportów na Telegram", 90)
]

# Funkcja generująca raport
def generate_report():
    report = "📊 *Szczegółowy raport prac nad Botem Nieruchomości:*\n\n"
    for task, progress in tasks:
        report += f"{task} — *{progress}%*\n"
    report += f"\n🕒 Ostatnia aktualizacja: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    return report

# Komenda /postep
def postep(update: Update, context: CallbackContext):
    update.message.reply_text(generate_report(), parse_mode="Markdown")

# Komenda /zadaj_pytanie
def zadaj_pytanie(update: Update, context: CallbackContext):
    update.message.reply_text("💬 Prześlij pytanie, a przekażę je do mistrza ChatGPT!")

# Komenda /raport
def raport(update: Update, context: CallbackContext):
    update.message.reply_text("📨 Kolejny raport zostanie wysłany automatycznie co 2 godziny.")

# Automatyczne wysyłanie raportu
def send_report(context: CallbackContext):
    context.bot.send_message(chat_id=CHAT_ID, text=generate_report(), parse_mode="Markdown")

# Start bota
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("postep", postep))
    dispatcher.add_handler(CommandHandler("zadaj_pytanie", zadaj_pytanie))
    dispatcher.add_handler(CommandHandler("raport", raport))

    # Harmonogram raportów
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_report, 'interval', hours=2, args=[updater.bot])
    scheduler.start()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


