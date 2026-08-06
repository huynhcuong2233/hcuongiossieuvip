import os
from flask import Flask, request

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ChatMemberHandler,
    ContextTypes,
    filters,
)

from handlers.start import start
from handlers.buttons import buttons

from database import create_tables

create_tables()

TOKEN = os.environ["BOT_TOKEN"]

app = Flask(__name__)

tg = Application.builder().token(TOKEN).build()

# Đăng ký handler
tg.add_handler(CommandHandler("start", start))
tg.add_handler(CallbackQueryHandler(buttons))
# Khởi tạo bot một lần
@app.before_request
async def initialize_bot():
    if not getattr(app, "_initialized", False):
        await tg.initialize()
        await tg.start()
        app._initialized = True

# Trang chủ
@app.get("/")
def home():
    return "✅ HCUONGIOS BOT ONLINE"



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )


# ==========================
# HCUONGIOS VIP - MENU SHOP
# ==========================

async def main_menu(update, context):

    keyboard = [
        [
            InlineKeyboardButton(
                "🛒 MUA API KEY",
                callback_data="shop"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 THANH TOÁN",
                callback_data="payment"
            ),
            InlineKeyboardButton(
                "👤 HỖ TRỢ",
                callback_data="support"
            )
        ],
        [
            InlineKeyboardButton(
                "📦 ĐƠN HÀNG",
                callback_data="orders"
            )
        ]
    ]

    text = (
        "╔════════════════╗\n"
        "⭐ *HCUONGIOS VIP* ⭐\n"
        "╚════════════════╝\n\n"
        "🚀 *Premium API Services*\n\n"
        "🔐 API KEY chất lượng cao\n"
        "⚡ Kích hoạt nhanh chóng\n"
        "🛡️ Hỗ trợ khách hàng\n"
        "💳 Thanh toán an toàn\n\n"
        "👇 Chọn dịch vụ:"
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# ==========================
# DANH SÁCH SẢN PHẨM
# ==========================

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
        "╔════════════════╗\n"
        "🛒 *CỬA HÀNG API KEY*\n"
        "╚════════════════╝\n\n"
        "⭐ PRO: Gói cao cấp\n"
        "⚡ BASIC: Gói tiết kiệm\n\n"
        "👇 Chọn sản phẩm:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
    # ==========================
# XỬ LÝ NÚT BẤM
# ==========================

async def button(update, context):

    query = update.callback_query

    await query.answer()


    # Mở cửa hàng
    if query.data == "shop":

        await show_products(update, context)


    # API PRO
    elif query.data == "product_pro":

        keyboard = [
            [
                InlineKeyboardButton(
                    "💎 PRO 1 NGÀY - 70.000đ",
                    callback_data="buy_pro_day"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔥 PRO 1 TUẦN - 210.000đ",
                    callback_data="buy_pro_week"
                )
            ],
            [
                InlineKeyboardButton(
                    "👑 PRO 1 THÁNG - 450.000đ",
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
            "╔════════════════╗\n"
            "⭐ *HCUONGIOS VIP*\n"
            "╚════════════════╝\n\n"
            "🚀 *API KEY PRO*\n\n"
            "✅ Tốc độ cao\n"
            "✅ Hỗ trợ ưu tiên\n"
            "✅ Kích hoạt nhanh\n\n"
            "💰 Chọn gói:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )


    # API BASIC
    elif query.data == "product_basic":

        keyboard = [
            [
                InlineKeyboardButton(
                    "⚡ BASIC 1 NGÀY - 50.000đ",
                    callback_data="buy_basic_day"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔥 BASIC 1 TUẦN - 150.000đ",
                    callback_data="buy_basic_week"
                )
            ],
            [
                InlineKeyboardButton(
                    "👑 BASIC 1 THÁNG - 300.000đ",
                    callback_data="buy_basic_month"
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
            "╔════════════════╗\n"
            "⚡ *API KEY BASIC*\n"
            "╚════════════════╝\n\n"
            "✅ Ổn định\n"
            "✅ Giá tốt\n"
            "✅ Dễ sử dụng\n\n"
            "💰 Chọn gói:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )


    # Thanh toán
    elif query.data == "payment":

        await query.edit_message_text(
            "💳 *THANH TOÁN HCUONGIOS VIP*\n\n"
            "🏦 Liên hệ admin để nhận thông tin thanh toán:\n\n"
            "👤 @thuynhcuong2510",
            parse_mode="Markdown"
        )


    # Hỗ trợ
    elif query.data == "support":

        await query.edit_message_text(
            "👤 *HỖ TRỢ KHÁCH HÀNG*\n\n"
            "☎️ Admin: @thuynhcuong2510\n"
            "⚡ Phản hồi nhanh",
            parse_mode="Markdown"
        )


    # Quay về menu
    elif query.data == "home":

        await query.edit_message_text(
            "🏠 *HCUONGIOS VIP*\n\n"
            "Chọn chức năng từ menu.",
            parse_mode="Markdown"
        )


    # Khi chọn mua
    elif query.data.startswith("buy_"):

        await query.edit_message_text(
            "✅ *ĐÃ CHỌN GÓI*\n\n"
            f"📦 {query.data}\n\n"
            "💳 Liên hệ admin để hoàn tất thanh toán:\n"
            "👤 @thuynhcuong2510",
            parse_mode="Markdown"
        )
        # ==========================
# CÁC LỆNH BOT
# ==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await main_menu(update, context)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📌 *LỆNH HCUONGIOS VIP*\n\n"
        "/start - Mở menu\n"
        "/help - Trợ giúp\n"
        "/id - Lấy ID Telegram\n"
        "/ping - Kiểm tra bot\n"
        "/shop - Cửa hàng\n"
        "/contact - Liên hệ",
        parse_mode="Markdown"
    )


async def id_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"🆔 ID của bạn: {update.effective_user.id}"
    )


async def ping_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🏓 Pong! HCUONGIOS VIP đang online ✅"
    )


async def shop_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await main_menu(update, context)


async def contact_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👤 Admin HCUONGIOS VIP:\n"
        "@thuynhcuong2510"
    )


# Echo tin nhắn
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        update.message.text
    )


# ==========================
# THÀNH VIÊN MỚI
# ==========================

async def welcome_member(update, context):

    if not update.chat_member:
        return

    member = update.chat_member

    old = member.old_chat_member.status
    new = member.new_chat_member.status


    if old in ["left", "kicked"] and new == "member":

        user = member.new_chat_member.user

        await context.bot.send_message(
            chat_id=member.chat.id,
            text=(
                "🎉 *THÀNH VIÊN MỚI*\n\n"
                f"👤 Xin chào {user.first_name}\n"
                "🔥 Chào mừng đến với HCUONGIOS VIP"
            ),
            parse_mode="Markdown"
        )


# ==========================
# ĐĂNG KÝ HANDLER
# ==========================

tg.add_handler(CommandHandler("help", help_cmd))
tg.add_handler(CommandHandler("id", id_cmd))
tg.add_handler(CommandHandler("ping", ping_cmd))
tg.add_handler(CommandHandler("shop", shop_cmd))
tg.add_handler(CommandHandler("contact", contact_cmd))


tg.add_handler(
    ChatMemberHandler(
        welcome_member,
        ChatMemberHandler.CHAT_MEMBER
    )
)


tg.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        echo
    )
)


# ==========================
# WEBHOOK FLASK
# ==========================

@app.post("/webhook")
async def webhook():
    update = Update.de_json(
        request.get_json(force=True),
        tg.bot
    )

    await tg.process_update(update)

    return "OK"
