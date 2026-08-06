from telegram import Update
from telegram.ext import ContextTypes

from .buttons import main_menu

async def start(update, context):
    await main_menu(update, context)
