from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("🔥 START ĐƯỢC GỌI")

    await update.message.reply_text(
        "✅ HCUONGIOS VIP BOT ONLINE\n\n"
        "🎉 Lệnh /start hoạt động bình thường!"
    )
