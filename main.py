import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
import os

# Konfiguracja logowania
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Twój Chat ID i Token
TOKEN = '7923832536:AAGiHmjAlbeVE-D0sN9rM3StPWfssq43q4U'
CHAT_ID = 8044783655  # <- Wklej swoje chat_id z Telegrama

# Harmonogram prac - tutaj aktualizujesz ręcznie lub automatyzujesz z gita
HARMONOGRAM = [
    ("🔧 Przygotowanie środowiska", 100),
    ("📦 Struktura plików + GitHub", 100),
    ("📡 Bot Telegram działa 24/7 na Render", 100),
    ("🧠 Analiza AI remontu", 40),
    ("🗺️ Interfejs z mapą i wykresami", 30),
    ("📊 Filtrowanie okazji + AI wyceny", 25),
    ("📁 Historia + logi + eksporty", 70),
    ("⚙️ Tryb „Tylko okazje komornicze”", 10),
    ("📨 Panel + powiadomienia", 50),
    ("🧪 Testy + UX", 15)
]

def format_report() -> str:
    report = "📊 *Szczegółowy raport z prac nad botem nieruchomości:*\n\n"
    total = 0
    for etap, procent in HARMONOGRAM:
        report += f"{etap}: `{procent}%`\n"
        total += procent
    overall = total // len(HARMONOGRAM)
    report += f"\n🔁 _Łączny postęp projektu:_ *{overall}%*"
    return report

def send_report(bot):
    now = datetime.now(pytz.timezone("Europe/Warsaw"))
    text = format_report() + f"\n\n🕒 Raport wygenerowany: `{now.strftime('%Y-%m-%d %H:%M:%S')}`"
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='Markdown')

def postep(update: Update, context: CallbackContext):
    update.message.reply_text(format_report(), parse_mode='Markdown')

def raport(update: Update, context: CallbackContext):
    now = datetime.now(pytz.timezone("Europe/Warsaw"))
    update.message.reply_text(format_report() + f"\n🕒 {now.strftime('%H:%M:%S')}", parse_mode='Markdown')

def zadanie(update: Update, context: CallbackContext):
    update.message.reply_text("🧠 Wyślij pytanie, a przekażę je dalej do mistrza umysłów. ✉️")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("postep", postep))
    dp.add_handler(CommandHandler("raport", raport))
    dp.add_handler(CommandHandler("zadaj_pytanie", zadanie))

    # Harmonogram wysyłki raportów co 2h
    scheduler = BackgroundScheduler(timezone=pytz.timezone("Europe/Warsaw"))
    scheduler.add_job(send_report, 'interval', hours=2, args=[updater.bot])
    scheduler.start()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

