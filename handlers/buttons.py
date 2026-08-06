from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import ContextTypes

import os
import qrcode

# ==========================
# TẠO QR
# ==========================

def create_qr(user_id):

    bank = "VIETCOMBANK"
    account = "1052960029"
    name = "THACH HUYNH CUONG"

    content = f"HCUONGIOS {user_id}"

    qr = qrcode.make(
        f"""
BANK:{bank}
ACCOUNT:{account}
NAME:{name}
CONTENT:{content}
"""
    )

    os.makedirs("assets", exist_ok=True)

    path = f"assets/qr_{user_id}.png"

    qr.save(path)

    return path


# ==========================
# MENU CHÍNH
# ==========================

async def main_menu(update, context):

    keyboard = [

        [
            InlineKeyboardButton(
                "👤 Tài khoản",
                callback_data="account"
            ),

            InlineKeyboardButton(
                "🛒 Cửa hàng",
                callback_data="shop"
            )
        ],

        [
            InlineKeyboardButton(
                "💳 Nạp tiền",
                callback_data="deposit"
            ),

            InlineKeyboardButton(
                "📜 Lịch sử",
                callback_data="history"
            )
        ],

        [
            InlineKeyboardButton(
                "☎️ Hỗ trợ",
                callback_data="support"
            )
        ]
    ]

    text = f"""
🏪 <b>HCUONGIOS STORE</b>

━━━━━━━━━━━━━━━━━━

👋 Xin chào
<b>{update.effective_user.first_name}</b>

💎 Dịch vụ API Premium
⚡ Kích hoạt tự động
🛡️ Bảo hành nhanh
🔥 Giá tốt mỗi ngày

━━━━━━━━━━━━━━━━━━

👇 Chọn chức năng bên dưới.
"""

    await update.message.reply_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==========================
# CALLBACK BUTTON
# ==========================

async def buttons(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()
        # ==========================
    # TÀI KHOẢN
    # ==========================

    if query.data == "account":

        text = f"""
👤 <b>THÔNG TIN TÀI KHOẢN</b>

━━━━━━━━━━━━━━

🆔 <b>ID:</b>
<code>{query.from_user.id}</code>

👤 <b>Tên:</b>
{query.from_user.first_name}

💰 <b>Số dư:</b> 0đ
💎 <b>Tổng đã nạp:</b> 0đ
📦 <b>Đơn hàng:</b> 0

━━━━━━━━━━━━━━
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
            text=text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # CỬA HÀNG
    # ==========================

    elif query.data == "shop":

        keyboard = [

            [
                InlineKeyboardButton(
                    "🔥 Migul FreeFire • VN",
                    callback_data="product_ff"
                )
            ],

            [
                InlineKeyboardButton(
                    "⚔️ Liên Quân iOS",
                    callback_data="product_lq"
                )
            ],

            [
                InlineKeyboardButton(
                    "🎱 8 Ball Pool iOS",
                    callback_data="product_8ball"
                )
            ],

            [
                InlineKeyboardButton(
                    "🌍 Migul Global",
                    callback_data="product_global"
                )
            ],

            [
                InlineKeyboardButton(
                    "🎮 PUBG Dolphin iOS",
                    callback_data="product_pubg"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔥 Flork FF MAX",
                    callback_data="product_flork"
                )
            ],

            [
                InlineKeyboardButton(
                    "🎁 Key Test Miễn Phí",
                    callback_data="free_key"
                )
            ],

            [
                InlineKeyboardButton(
                    "⬅️ Quay lại",
                    callback_data="home"
                )
            ]
        ]

        text = """
🛒 <b>CỬA HÀNG SẢN PHẨM</b>

━━━━━━━━━━━━━━

Hãy chọn sản phẩm bạn muốn mua.

💡 Các sản phẩm được cập nhật thường xuyên.

━━━━━━━━━━━━━━
"""

        await query.edit_message_text(
            text=text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # MIGUL FREEFIRE
    # ==========================

    elif query.data == "product_ff":

        keyboard = [

            [
                InlineKeyboardButton(
                    "⚡ Migul Lite | 100.000đ",
                    callback_data="buy_migul_lite"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔥 Migul Pro | 200.000đ",
                    callback_data="buy_migul_pro"
                )
            ],

            [
                InlineKeyboardButton(
                    "👑 Migul VIP | 300.000đ",
                    callback_data="buy_migul_vip"
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
            """
🔥 <b>MIGUL FREEFIRE • VN</b>

⚡ Lite
🔥 Pro
👑 VIP

👇 Chọn gói muốn mua.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
