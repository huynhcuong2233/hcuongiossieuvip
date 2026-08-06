from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import ContextTypes


async def main_menu(update, context):
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

    text = """
🏪 <b>HCUONGIOS STORE</b>

👋 Chào mừng bạn!

👇 Chọn chức năng:
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # giữ toàn bộ code xử lý nút của bạn ở dưới đây
    if query.data == "account":
        text = f"""
👤 <b>TÀI KHOẢN</b>

🆔 ID: <code>{query.from_user.id}</code>
👤 Tên: {query.from_user.first_name}

💎 Số dư: 0đ
💰 Đã nạp: 0đ
📦 Đơn hàng: 0
"""

        keyboard = [
            [InlineKeyboardButton("⬅️ Quay lại", callback_data="home")]
        ]

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "shop":
        text = """
🛒 <b>CỬA HÀNG</b>

📦 Chưa có sản phẩm.

Admin sẽ cập nhật sau.
"""

        keyboard = [
            [InlineKeyboardButton("⬅️ Quay lại", callback_data="home")]
        ]

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "deposit":

        caption = f"""
💳 <b>NẠP TIỀN TỰ ĐỘNG</b>

🏦 <b>Ngân hàng:</b> MB Bank
👤 <b>Chủ tài khoản:</b> THACH THI NGOC TRAN
💳 <b>Số tài khoản:</b> 26251008201010

━━━━━━━━━━━━━━

📝 <b>Nội dung chuyển khoản:</b>

<code>FF{query.from_user.id}</code>

💰 Tối thiểu: <b>10.000đ</b>

⚡ Sau khi chuyển khoản đúng nội dung, hệ thống sẽ tự động cộng tiền.

━━━━━━━━━━━━━━

❗ Không sửa nội dung chuyển khoản.
"""

        keyboard = [
            [
                InlineKeyboardButton("🔄 Kiểm tra", callback_data="check_payment"),
            ],
            [
                InlineKeyboardButton("⬅️ Quay lại", callback_data="home"),
            ],
        ]

        await query.message.reply_photo(
            photo=open("assets/qr_mb.jpg", "rb"),
            caption=caption,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "history":
        text = """
📜 <b>LỊCH SỬ</b>

Bạn chưa có giao dịch nào.
"""

        keyboard = [
            [InlineKeyboardButton("⬅️ Quay lại", callback_data="home")]
        ]

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "support":
        text = """
☎️ <b>HỖ TRỢ</b>

Telegram:
@hcuongios
"""

        keyboard = [
            [InlineKeyboardButton("⬅️ Quay lại", callback_data="home")]
        ]

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "home":
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

        text = """
🏪 <b>HCUONGIOS STORE</b>

👋 Chào mừng bạn!

💎 Số dư: 0đ

Chọn chức năng bên dưới.
"""

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "check_payment":
        await query.answer(
            "⚠️ Chức năng kiểm tra thanh toán chưa được kết nối SePay.",
            show_alert=True,
        )

    else:
        await query.answer("Chức năng đang phát triển.")
