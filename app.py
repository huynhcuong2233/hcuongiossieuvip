import os

from flask import Flask, request

from telegram import Update

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from handlers.start import start
from handlers.buttons import buttons
from handlers.admin import admin_handlers

from database import setup_database


setup_database()

TOKEN = os.environ["BOT_TOKEN"]

app = Flask(__name__)


@app.route("/")
def home():
    return "✅ HCUONGIOS BOT ONLINE"


tg = Application.builder().token(TOKEN).build()


tg.add_handler(
    CommandHandler("start", start)
)

tg.add_handler(
    CallbackQueryHandler(buttons)
)


for handler in admin_handlers():
    tg.add_handler(handler)


# ==========================
# WEBHOOK TELEGRAM
# ==========================

@app.route("/webhook", methods=["POST"])
async def webhook():

    data = request.get_json(force=True)

    update = Update.de_json(
        data,
        tg.bot
    )

    await tg.process_update(update)

    return "ok"
