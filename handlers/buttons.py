from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import ContextTypes

import os
import qrcode

from database import (
    get_balance,
    remove_balance,
    create_order,
)

from momo import create_deposit_code

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
    elif query.data == "product_ff":
    ...
        # ==========================
    # LIÊN QUÂN
    # ==========================

    elif query.data == "product_lq":

        keyboard = [
            [
                InlineKeyboardButton(
                    "⚔️ Liên Quân iOS | 150.000đ",
                    callback_data="buy_lq"
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
⚔️ <b>LIÊN QUÂN iOS</b>

💰 Giá: <b>150.000đ</b>

🛡️ Bảo hành
⚡ Kích hoạt tự động

👇 Nhấn nút bên dưới để mua.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # PUBG
    # ==========================

    elif query.data == "product_pubg":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🎮 PUBG Dolphin | 180.000đ",
                    callback_data="buy_pubg"
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
🎮 <b>PUBG DOLPHIN iOS</b>

💰 Giá: <b>180.000đ</b>

⚡ Hỗ trợ iPhone
🛡️ Bảo hành

👇 Nhấn nút để mua.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # 8 BALL
    # ==========================

    elif query.data == "product_8ball":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🎱 8 Ball Pool | 120.000đ",
                    callback_data="buy_8ball"
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
🎱 <b>8 BALL POOL iOS</b>

💰 Giá: <b>120.000đ</b>

👇 Nhấn để mua.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # GLOBAL
    # ==========================

    elif query.data == "product_global":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🌍 Migul Global | 250.000đ",
                    callback_data="buy_global"
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
🌍 <b>MIGUL GLOBAL</b>

💰 Giá: <b>250.000đ</b>

👇 Chọn mua.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # FLORK
    # ==========================

    elif query.data == "product_flork":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔥 Flork FF MAX | 300.000đ",
                    callback_data="buy_flork"
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
🔥 <b>FLORK EXTERNAL FF MAX</b>

💰 Giá: <b>300.000đ</b>

👇 Nhấn để mua.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # KEY TEST
    # ==========================

    elif query.data == "free_key":

        keyboard = [
            [
                InlineKeyboardButton(
                    "⬅️ Quay lại",
                    callback_data="shop"
                )
            ]
        ]

        await query.edit_message_text(
            """
🎁 <b>KEY TEST MIỄN PHÍ</b>

⚡ Chức năng sẽ sớm được cập nhật.

❤️ Cảm ơn bạn đã sử dụng HCUONGIOS STORE.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    # ==========================
# NẠP TIỀN
# ==========================

elif query.data == "deposit":

    user_id = query.from_user.id

    code = create_deposit_code(user_id)

    text = f"""
💰 <b>NẠP TIỀN QUA MOMO</b>

📱 Ví MoMo:
0375942325

👤 Chủ ví:
THACH HUYNH CUONG

💵 Nội dung chuyển khoản:
<code>{code}</code>

⚠️ Vui lòng ghi đúng nội dung để được cộng tiền.
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Tôi đã chuyển tiền",
                callback_data="check_payment"
            )
        ],
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
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


    # ==========================
    # LỊCH SỬ
    # ==========================

    elif query.data == "history":

        text = """
📜 <b>LỊCH SỬ GIAO DỊCH</b>

━━━━━━━━━━━━━━

❌ Chưa có giao dịch nào.

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
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ==========================
    # HỖ TRỢ
    # ==========================

    elif query.data == "support":

        text = """
☎️ <b>HỖ TRỢ KHÁCH HÀNG</b>

👤 Admin

@thuynhcuong2510

⏰ Online mỗi ngày.

━━━━━━━━━━━━━━

❤️ Cảm ơn bạn đã sử dụng HCUONGIOS STORE.
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
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ==========================
    # HOME
    # ==========================

    elif query.data == "home":

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

        await query.edit_message_text(
            f"""
🏪 <b>HCUONGIOS STORE</b>

👋 Xin chào <b>{query.from_user.first_name}</b>

💎 API Premium
⚡ Kích hoạt nhanh
🛡️ Hỗ trợ 24/7

👇 Chọn chức năng bên dưới.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ==========================
    # KIỂM TRA THANH TOÁN
    # ==========================

    elif query.data == "check_payment":

        await query.answer(
            "⚠️ Chức năng chưa kết nối SePay.",
            show_alert=True
        )
    # ==========================
    # MUA SẢN PHẨM
    # ==========================

    elif query.data.startswith("buy_"):

        products = {
            "buy_migul_lite": ("Migul Lite - VN", 100000),
            "buy_migul_pro": ("Migul Pro - VN", 200000),
            "buy_migul_vip": ("Migul VIP - VN", 300000),
            "buy_lq": ("Liên Quân iOS", 150000),
            "buy_pubg": ("PUBG Dolphin iOS", 180000),
            "buy_global": ("Migul Global", 250000),
            "buy_flork": ("Flork FF MAX", 300000),
            "buy_8ball": ("8 Ball Pool iOS", 120000),
        }

        product_name, price = products[query.data]

        balance = get_balance(query.from_user.id)

        if balance < price:

            await query.answer(
                "❌ Số dư không đủ để mua sản phẩm.",
                show_alert=True
            )
            return

        remove_balance(
            query.from_user.id,
            price
        )

        api_key = (
            f"HCUONGIOS-"
            f"{query.from_user.id}-"
            f"{os.urandom(4).hex().upper()}"
        )

        create_order(
            query.from_user.id,
            product_name,
            price,
            api_key
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🛒 Tiếp tục mua",
                    callback_data="shop"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 Trang chủ",
                    callback_data="home"
                )
            ]
        ]

        await query.edit_message_text(
            f"""
✅ <b>MUA THÀNH CÔNG</b>

━━━━━━━━━━━━━━

📦 <b>Sản phẩm:</b>
{product_name}

💰 <b>Giá:</b>
{price:,}đ

🔑 <b>API KEY:</b>

<code>{api_key}</code>

━━━━━━━━━━━━━━

⚠️ Hãy lưu API Key cẩn thận.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==========================
    # CHƯA CÓ CHỨC NĂNG
    # ==========================

    else:

        await query.answer(
            "🚧 Chức năng đang được cập nhật.",
            show_alert=True
        )
        
