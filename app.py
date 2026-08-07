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


# ==========================
# DATABASE
# ==========================

setup_database()


# ==========================
# CONFIG
# ==========================

TOKEN = os.environ["BOT_TOKEN"]


# ==========================
# FLASK
# ==========================

app = Flask(__name__)


@app.route("/")
def home():
    return "✅ HCUONGIOS BOT ONLINE"


# ==========================
# TELEGRAM BOT
# ==========================

tg = (
    Application.builder()
    .token(TOKEN)
    .concurrent_updates(True)
    .build()
)


# ==========================
# HANDLERS
# ==========================

tg.add_handler(
    CommandHandler(
        "start",
        start
    )
)


tg.add_handler(
    CallbackQueryHandler(
        buttons
    )
)


for handler in admin_handlers():
    tg.add_handler(handler)


# ==========================
# WEBHOOK
# ==========================

@app.route(
    "/webhook",
    methods=["POST"]
)
async def webhook():

    try:
        data = request.get_json(force=True)

        update = Update.de_json(
            data,
            tg.bot
        )

        await tg.process_update(update)

    except Exception as e:
        print(
            "WEBHOOK ERROR:",
            e
        )

    return "ok"


# ==========================
# START / STOP BOT
# ==========================

@app.before_serving
async def startup():

    await tg.initialize()
    await tg.start()

    print(
        "🤖 HCUONGIOS BOT STARTED"
    )


@app.after_serving
async def shutdown():

    await tg.stop()
    await tg.shutdown()

    print(
        "🛑 BOT STOPPED"
    )
