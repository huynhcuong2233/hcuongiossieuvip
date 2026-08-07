from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    text = f"""
<b>👑 HCUONGIOS VIP STORE</b>

━━━━━━━━━━━━━━━━━━

👋 Xin chào <b>{user.first_name}</b>

🆔 <b>ID:</b> <code>{user.id}</code>
💎 <b>Số dư:</b> <code>0đ</code>
🔑 <b>KEY:</b> <code>0</code>

━━━━━━━━━━━━━━━━━━

✨ <b>Dịch vụ:</b>
• 🔥 KEY Free Fire
• 🍎 Dịch vụ iOS
• ⚡ Giao hàng nhanh
• 🛡️ Hỗ trợ 24/7

━━━━━━━━━━━━━━━━━━

👇 <b>Vui lòng chọn chức năng bên dưới.</b>
"""

    keyboard = [
        [
            InlineKeyboardButton("🛒 Mua KEY", callback_data="shop"),
            InlineKeyboardButton("💳 Nạp tiền", callback_data="deposit"),
        ],
        [
            InlineKeyboardButton("👤 Tài khoản", callback_data="account"),
            InlineKeyboardButton("🔑 KEY của tôi", callback_data="mykey"),
        ],
        [
            InlineKeyboardButton("📜 Lịch sử", callback_data="history"),
            InlineKeyboardButton("☎️ Hỗ trợ", callback_data="support"),
        ],
        [
            InlineKeyboardButton("📢 Kênh Telegram", url="https://t.me/hcuongios")
        ],
    ]

    try:
    await update.message.reply_photo(
        photo=open("assets/banner.jpg", "rb"),
        caption=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
except FileNotFoundError:
    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
