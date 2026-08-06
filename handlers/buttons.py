from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import ContextTypes

import qrcode
import os


# Tạo QR thanh toán
def create_qr(user_id):

    bank = "VIETCOMBANK"
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



# Menu chính
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
            ),
        ],
        [
            InlineKeyboardButton(
                "💳 Nạp tiền",
                callback_data="deposit"
            ),
            InlineKeyboardButton(
                "📜 Lịch sử",
                callback_data="history"
            ),
        ],
        [
            InlineKeyboardButton(
                "☎️ Hỗ trợ",
                callback_data="support"
            ),
        ],
    ]


    text = """
🏪 <b>HCUONGIOS STORE</b>

👋 Xin chào bạn!

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




# Xử lý nút bấm
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()



    # Tài khoản
    if query.data == "account":

        text = f"""
👤 <b>TÀI KHOẢN</b>

🆔 ID:
<code>{query.from_user.id}</code>

👤 Tên:
{query.from_user.first_name}

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
            reply_markup=InlineKeyboardMarkup(keyboard)
        )



    # Cửa hàng
    elif query.data == "shop":

        text = """
🛒 <b>CỬA HÀNG</b>
    elif query.data == "product_ff":

        keyboard = [
            [
                InlineKeyboardButton(
                    "⚡ Migul Lite - VN",
                    callback_data="buy_migul_lite"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔥 Migul Pro - VN",
                    callback_data="buy_migul_pro"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Quay lại",
                    callback_data="shop"
                )
            ]
        ]

        text = """
🔥 <b>MIGUL FREEFIRE • VN</b>

Chọn sản phẩm bạn muốn mua:

━━━━━━━━━━━━━━

⚡ Migul Lite - VN
🔥 Migul Pro - VN

👇 Chọn gói:
"""

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "product_lq":

        keyboard = [
            [
                InlineKeyboardButton(
                    "⚔️ Liên Quân iOS",
                    callback_data="buy_lienquan"
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

Chọn sản phẩm muốn mua:
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "product_8ball":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🎱 8 Ball Pool iOS",
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

Chọn sản phẩm:
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "product_tipa":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🚀 TIPA FF External",
                    callback_data="buy_tipa"
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
🚀 <b>TIPA FF EXTERNAL</b>

Hỗ trợ TrollStore.

Chọn sản phẩm:
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "product_global":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🌍 Migul Global",
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

Chọn sản phẩm:
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "product_pubg":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🎮 PUBG Dolphin IOS",
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
🎮 <b>PUBG DOLPHIN IOS</b>

Chọn sản phẩm:
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "product_flork":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔥 Flork External FF MAX",
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

Chọn sản phẩm:
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "free_key":

        await query.edit_message_text(
            """
🎁 <b>KEY TEST MIỄN PHÍ</b>

Bạn có thể nhận key test tại đây.

⏳ Hệ thống đang xử lý...
""",
            parse_mode="HTML"
        )

🚀 API Premium

📦 Sản phẩm đang cập nhật.

Vui lòng quay lại sau.
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



    # Nạp tiền
    elif query.data == "deposit":


        qr_path = create_qr(query.from_user.id)


        caption = f"""
💳 <b>NẠP TIỀN HCUONGIOS VIP</b>

🏦 <b>Ngân hàng:</b> VIETCOMBANK

💳 <b>Số tài khoản:</b>
<code>1052960029</code>

👤 <b>Chủ tài khoản:</b>
THACH HUYNH CUONG


━━━━━━━━━━━━━━

📝 <b>Nội dung chuyển khoản:</b>

<code>HCUONGIOS {query.from_user.id}</code>


💰 Tối thiểu: 10.000đ

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



    # Lịch sử
    elif query.data == "history":

        text = """
📜 <b>LỊCH SỬ</b>

Bạn chưa có giao dịch nào.
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



    # Hỗ trợ
    elif query.data == "support":

        text = """
☎️ <b>HỖ TRỢ</b>

👤 Admin:
@thuynhcuong2510

⚡ Phản hồi nhanh.
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



    # Quay lại menu
    elif query.data == "home":

        await query.edit_message_text(
            """
🏪 <b>HCUONGIOS STORE</b>

👋 Chào mừng bạn!

Chọn chức năng bên dưới.
""",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([
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
            ])
        )


    else:
elif query.data == "shop":
    # menu sản phẩm


elif query.data == "product_ff":
    # Migul FreeFire Lite/Pro


elif query.data == "product_lq":
    # Liên Quân


elif query.data == "product_pubg":
    # PUBG


else:
    await query.answer("Chức năng đang phát triển.")
            show_alert=True
        )
