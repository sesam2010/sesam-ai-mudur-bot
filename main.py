from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Merhaba Volkan Bey.\n\nBen Sesam AI Müdür.\nHazırım."
    )

async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """📋 Bugünün Planı

1- Hepsiburada Buybox kontrol
2- Trendyol sipariş kontrol
3- Instagram paylaşımı
4- Personel görüşmeleri
5- Depo düzeni

🚀 Hedef: Satışı artırmak
"""
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("plan", plan))

app.run_polling()
