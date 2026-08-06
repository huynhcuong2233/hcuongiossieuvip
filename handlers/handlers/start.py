from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = f"""
🏪 <b>HCUONGIOS STORE</b>

👋 Xin chào <b>{update.effective_user.first_name}</b>

🆔 ID: <code>{update.effective_user.id}</code>

💎 Số dư: <b>0đ</b>
💰 Tổng nạp: <b>0đ</b>
📦 Đơn hàng: <b>0</b>

━━━━━━━━━━━━━━

⚡ Chọn chức năng bên dưới.
"""

    keyboard = [
        [
            InlineKeyboardButton("👤 Tài khoản", callback_data="account"),
            InlineKeyboardButton("🛒 Cửa hàng", callback_data="shop"),
        ],
        [
            InlineKeyboardButton("💳 Nạp tiền", callback_data="deposit"),
            InlineKeyboardButton("📜 Lịch sử", callback_data="history"),
        ],
        [
            InlineKeyboardButton("☎️ Hỗ trợ", callback_data="support"),
        ],
    ]

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
