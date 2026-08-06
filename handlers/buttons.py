from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import ContextTypes

import qrcode
import os


def create_qr(user_id):
    bank = "VCB"
    account = "1052960029"
    name = "THACH HUYNH CUONG"
    content = f"HCUONGIOS {user_id}"

    qr_data = (
        f"Ngân hàng: {bank}\n"
        f"STK: {account}\n"
        f"Chủ TK: {name}\n"
        f"Nội dung: {content}"
    )

    os.makedirs("assets", exist_ok=True)

    qr = qrcode.make(qr_data)
    path = f"assets/qr_{user_id}.png"
    qr.save(path)

    return path


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

💎 Dịch vụ API Premium
⚡ Kích hoạt nhanh
🛡️ Hỗ trợ khách hàng

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

    # Tài khoản
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
            [
                InlineKeyboardButton(
                    "⬅️ Quay lại",
                    callback_data="home"
                )
            ]
        ]

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


    # Nạp tiền
    elif query.data == "deposit":

        qr_path = create_qr(query.from_user.id)

        caption = f"""
💳 <b>NẠP TIỀN HCUONGIOS VIP</b>

🏦 <b>Ngân hàng:</b> VIETCOMBANK
💳 <b>Số tài khoản:</b> 1052960029
👤 <b>Chủ tài khoản:</b> THACH HUYNH CUONG

━━━━━━━━━━━━━━

📝 <b>Nội dung chuyển khoản:</b>

<code>HCUONGIOS {query.from_user.id}</code>

💰 <b>Tối thiểu:</b> 10.000đ

⚡ Chuyển khoản đúng nội dung để hệ thống nhận diện.

━━━━━━━━━━━━━━

✅ Quét QR để thanh toán
"""

        keyboard = [
            [
                InlineKeyboardButton(
                    "⬅️ Quay lại",
                    callback_data="home"
                )
            ]
        ]

        with open(qr_path, "rb") as img:
            await query.message.reply_photo(
                photo=img,
                caption=caption,
                parse_mode="HTML",
                reply_markup=InlineKeyboardMarkup(keyboard)
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
@thuynhcuong2510
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
