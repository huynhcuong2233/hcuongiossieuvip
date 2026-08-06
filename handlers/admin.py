from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from database import confirm_deposit


ADMIN_ID = 123456789  # đổi thành ID Telegram của bạn


async def approve_deposit(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # kiểm tra admin

    if update.effective_user.id != ADMIN_ID:

        await update.message.reply_text(
            "❌ Bạn không có quyền."
        )
        return


    if len(context.args) < 1:

        await update.message.reply_text(
            "Cách dùng:\n/duyet MÃ_NẠP"
        )
        return


    content = context.args[0]


    result = confirm_deposit(content)


    if result:

        user_id, amount = result

        await update.message.reply_text(
            f"""
✅ Đã duyệt nạp tiền

👤 User:
{user_id}

💰 Số tiền:
{amount:,}đ
"""
        )


        # báo cho khách

        await context.bot.send_message(
            chat_id=user_id,
            text=f"""
🎉 Nạp tiền thành công!

💰 +{amount:,}đ

Cảm ơn bạn đã sử dụng HCUONGIOS STORE.
"""
        )


    else:

        await update.message.reply_text(
            "❌ Không tìm thấy mã nạp hoặc đã duyệt."
        )



def admin_handlers():

    return [
        CommandHandler(
            "duyet",
            approve_deposit
        )
    ]
