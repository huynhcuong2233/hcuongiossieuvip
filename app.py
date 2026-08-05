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
    ChatMemberHandler,
    ContextTypes,
    filters
)


TOKEN = os.environ["BOT_TOKEN"]
URL = os.environ.get("RENDER_EXTERNAL_URL", "")

app = Flask(__name__)

tg = Application.builder().token(TOKEN).build()


# DÁN ĐOẠN show_products() Ở ĐÂY

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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
        ],
    ]

    await update.callback_query.edit_message_text(
        "🛒 *CHỌN SẢN PHẨM*\n\n"
        "⭐ API KEY PRO\n"
        "⚡ API KEY BASIC\n\n"
        "👇 Chọn sản phẩm:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


async def button(update, context):
    query = update.callback_query

    await query.answer()

    print("BUTTON:", query.data)

    if query.data == "shop":
        await show_products(update, context)


    elif query.data == "product_pro":

        keyboard = [
            [
                InlineKeyboardButton(
                    "💳 1 ngày - 70.000đ",
                    callback_data="buy_pro_day"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔥 1 tuần - 210.000đ",
                    callback_data="buy_pro_week"
                )
            ],
            [
                InlineKeyboardButton(
                    "👑 1 tháng - 450.000đ",
                    callback_data="buy_pro_month"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Quay lại",
                    callback_data="shop"
                )
            ]
        ]

        await query.edit_message_text(
            "╔══════════════╗\n"
            "⭐ *HCUONGIOS VIP* ⭐\n"
            "╚══════════════╝\n\n"
            "🚀 *API KEY PRO*\n\n"
            "✅ Kích hoạt nhanh\n"
            "✅ Hỗ trợ 24/7\n"
            "✅ Dịch vụ ổn định\n\n"
            "💰 *Giá:*\n"
            "🟢 1 ngày: 70.000đ\n"
            "🔵 1 tuần: 210.000đ\n"
            "🟣 1 tháng: 450.000đ",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )


    elif query.data == "product_basic":

        await query.edit_message_text(
            "╔══════════════╗\n"
            "⭐ *HCUONGIOS VIP* ⭐\n"
            "╚══════════════╝\n\n"
            "⚡ *API KEY BASIC*\n\n"
            "🟢 1 ngày: 50.000đ\n"
            "🔵 1 tuần: 150.000đ\n"
            "🟣 1 tháng: 450.000đ",
            parse_mode="Markdown"
        )


    elif query.data == "home":

        await query.edit_message_text(
            "🏠 *HCUONGIOS VIP*\n\n"
            "Chọn chức năng từ menu.",
            parse_mode="Markdown"
        )


    elif query.data.startswith("buy_"):

        await query.edit_message_text(
            "✅ Bạn đã chọn gói:\n\n"
            f"`{query.data}`\n\n"
            "☎️ Liên hệ admin để thanh toán.",
            parse_mode="Markdown"
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


# /# Contact
async def contact_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "☎️ Liên hệ admin: @thuynhcuong2510"
    )


# Echo tin nhắn thường
async def echo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# =========================
# THÔNG BÁO THÀNH VIÊN MỚI
# =========================

async def welcome_member(update, context):

    if not update.chat_member:
        return

    result = update.chat_member

    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    if old_status in ["left", "kicked"] and new_status == "member":

        user = result.new_chat_member.user

        await context.bot.send_message(
            chat_id=result.chat.id,
            text=(
                "🎉 *THÀNH VIÊN MỚI!*\n\n"
                f"👤 Xin chào {user.first_name}\n\n"
                "🔥 Chào mừng bạn đến với *HCUONGIOS VIP*"
            ),
            parse_mode="Markdown"
        )


# =========================
# ĐĂNG KÝ HANDLER
# =========================

tg.add_handler(CommandHandler("start", start))
tg.add_handler(CommandHandler("help", help_cmd))
tg.add_handler(CommandHandler("id", id_cmd))
tg.add_handler(CommandHandler("ping", ping_cmd))
tg.add_handler(CommandHandler("shop", shop_cmd))
tg.add_handler(CommandHandler("contact", contact_cmd))

# Menu nút bấm
tg.add_handler(CallbackQueryHandler(button))

# Thành viên mới
tg.add_handler(
    ChatMemberHandler(
        welcome_member,
        ChatMemberHandler.CHAT_MEMBER
    )
)

# Tin nhắn thường
tg.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        echo
    )
)


# =========================
# WEBHOOK
# =========================

@app.post("/webhook")
async def webhook():

    if not tg._initialized:
        await tg.initialize()

    update = Update.de_json(
        request.json,
        tg.bot
    )

    await tg.process_update(update)

    return "ok"


@app.get("/")
def home():
    return "OK"
