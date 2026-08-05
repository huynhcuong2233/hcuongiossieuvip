from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ['BOT_TOKEN']
URL = os.environ.get('RENDER_EXTERNAL_URL', '')

app = Flask(__name__)

tg = Application.builder().token(TOKEN).build()


# /start
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot online!\n\n"
        "Danh sách lệnh:\n"
        "/help - Xem lệnh\n"
        "/id - Lấy ID\n"
        "/ping - Kiểm tra bot\n"
        "/shop - Cửa hàng\n"
        "/contact - Liên hệ"
    )


# /help
async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 LỆNH BOT\n\n"
        "/start - Khởi động bot\n"
        "/help - Trợ giúp\n"
        "/id - Lấy ID Telegram\n"
        "/ping - Kiểm tra online\n"
        "/shop - Xem sản phẩm\n"
        "/contact - Liên hệ admin"
    )


# /id
async def id_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 ID của bạn: {update.effective_user.id}"
    )


# /ping
async def ping_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏓 Pong! Bot đang hoạt động ✅"
    )


# /shop
async def shop_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 CỬA HÀNG\n\n"
        "📨 migul pro/lite\n"
        "📨 proxy\n"
        "📨 tipa/flork\n\n"
        "Liên hệ admin để @thuynhcuong2510 mua key."
    )


# /contact
async def contact_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "☎️ Liên hệ admin: @thuynhcuong2510"
    )


# Echo tin nhắn thường
async def echo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


# Đăng ký lệnh
tg.add_handler(CommandHandler('start', start))
tg.add_handler(CommandHandler('help', help_cmd))
tg.add_handler(CommandHandler('id', id_cmd))
tg.add_handler(CommandHandler('ping', ping_cmd))
tg.add_handler(CommandHandler('shop', shop_cmd))
tg.add_handler(CommandHandler('contact', contact_cmd))

tg.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


@app.post('/webhook')
async def webhook():
    await tg.initialize()

    if URL:
        await tg.bot.set_webhook(URL + '/webhook')

    u = Update.de_json(request.json, tg.bot)
    await tg.process_update(u)

    return 'ok'


@app.get('/')
def home():
    return 'OK'
