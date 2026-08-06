from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"👋 Xin chào {user.first_name}!\n\n"
        "🤖 Bot HCUONGIOS đang hoạt động."
    )
