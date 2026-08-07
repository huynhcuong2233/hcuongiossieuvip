from telegram import Update
from telegram.ext import ContextTypes


async def help_cmd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "📌 HCUONGIOS VIP\n\n"
        "/start - Mở menu\n"
        "/help - Trợ giúp\n"
        "/id - Lấy ID\n"
        "/ping - Kiểm tra bot\n"
        "/shop - Cửa hàng\n"
        "/contact - Liên hệ"
    )


async def id_cmd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        f"🆔 ID: {update.effective_user.id}"
    )


async def ping_cmd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🏓 Pong! Bot đang online ✅"
    )


async def shop_cmd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🛒 Gõ /start để mở cửa hàng"
    )


async def contact_cmd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "👤 Admin: @thuynhcuong2510"
    )


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
                "🎉 Chào mừng thành viên mới\n\n"
                f"👤 {user.first_name}\n"
                "🔥 HCUONGIOS VIP"
            )
        )
