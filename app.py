from flask import Flask, request
import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)


TOKEN = os.environ["BOT_TOKEN"]
URL = os.environ.get("RENDER_EXTERNAL_URL", "")

app = Flask(__name__)

tg = Application.builder().token(TOKEN).build()


# DÁN ĐOẠN show_products() Ở ĐÂY

async def show_products(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "⭐ API KEY PRO",
                callback_data="product_pro"
            )
        ],
        [
            InlineKeyboardButton(
                "⚡ API KEY BASIC",
                callback_data="product_basic"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Quay lại",
                callback_data="home"
            )
        ]
    ]

    await update.callback_query.edit_message_text(
        "🛒 CHỌN SẢN PHẨM",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# Sau đó mới tới
async def start(update, context):
    ...


# /start
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


async def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛒 Mua API Key",
                callback_data="shop"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 Thanh toán",
                callback_data="payment"
            ),
            InlineKeyboardButton(
                "👤 Hỗ trợ",
                callback_data="support"
            )
        ]
    ]

    text = (
        "🚀 *HCUONGIOS VIP*\n"
        "Premium API Services\n\n"
        f"👋 Xin chào {update.effective_user.first_name}!\n\n"
        "🔐 Cửa hàng API Key\n"
        "⚡ Kích hoạt nhanh\n"
        "🛡️ Hỗ trợ khách hàng\n"
        "💳 Thanh toán an toàn\n\n"
        "👇 Chọn chức năng:"
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


async def show_products(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "⭐ API KEY PRO",
                callback_data="product_pro"
            )
        ],
        [
            InlineKeyboardButton(
                "⚡ API KEY BASIC",
                callback_data="product_basic"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Quay lại",
                callback_data="home"
            )
        ]
    ]

    await update.callback_query.edit_message_text(
        "🛒 CHỌN SẢN PHẨM\n\n"
        "⭐ API KEY PRO\n"
        "⚡ API KEY BASIC",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update, context):
    query = update.callback_query

    await query.answer()

    if query.data == "shop":
        await show_products(update, context)


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
        "📨 apl pro/lite\n"
        "📨 apl \n"
        "📨 apl /apl \n\n"
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
tg.add_handler(CallbackQueryHandler(button))

tg.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


@app.post('/webhook')
async def webhook():
    await tg.initialize()

    u = Update.de_json(request.json, tg.bot)
    await tg.process_update(u)

    return "ok"

@app.get('/')
def home():
    return 'OK'
