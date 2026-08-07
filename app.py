import os

import asyncio

from flask import Flask, request

from telegram import Update

from telegram.ext import (

    Application,

    CommandHandler,

    CallbackQueryHandler,

    ChatMemberHandler,

)

from handlers.start import start

from handlers.buttons import buttons

from handlers.admin import admin_handlers

from handlers.commands import (

    help_cmd,

    id_cmd,

    ping_cmd,

    shop_cmd,

    contact_cmd,

    welcome_member,

)

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

# TELEGRAM

# ==========================

tg = Application.builder().token(TOKEN).build()

# ==========================

# INITIALIZE BOT

# ==========================

loop = asyncio.new_event_loop()

asyncio.set_event_loop(loop)

loop.run_until_complete(

    tg.initialize()

)

# ==========================

# HANDLERS

# ==========================

tg.add_handler(

    CommandHandler("start", start)

)

tg.add_handler(

    CallbackQueryHandler(buttons)

)

for handler in admin_handlers():

    tg.add_handler(handler)

tg.add_handler(

    CommandHandler("help", help_cmd)

)

tg.add_handler(

    CommandHandler("id", id_cmd)

)

tg.add_handler(

    CommandHandler("ping", ping_cmd)

)

tg.add_handler(

    CommandHandler("shop", shop_cmd)

)

tg.add_handler(

    CommandHandler("contact", contact_cmd)

)

tg.add_handler(

    ChatMemberHandler(

        welcome_member,

        ChatMemberHandler.CHAT_MEMBER

    )

)

# ==========================

# WEBHOOK

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
