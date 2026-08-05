from flask import Flask,request
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,ContextTypes,filters
import os
TOKEN=os.environ['BOT_TOKEN']
URL=os.environ.get('RENDER_EXTERNAL_URL','')
app=Flask(__name__)
tg=Application.builder().token(TOKEN).build()
async def start(update:Update,ctx:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bot online!')
async def echo(update:Update,ctx:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)
tg.add_handler(CommandHandler('start',start))
tg.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,echo))
@app.post('/')
async def webhook():
    await tg.initialize()
    if URL:
        await tg.bot.set_webhook(URL+'/')
    u=Update.de_json(request.json,tg.bot)
    await tg.process_update(u)
    return 'ok'
@app.get('/')
def home():
    return 'OK'
