import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")
GROUP_LINK = "https://t.me/+P0fvrB2xT700YjJi"

logging.basicConfig(level=logging.INFO)

KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("🌱 Новичок-Свежачок", callback_data="A")],
    [InlineKeyboardButton("💅 Мастер Педикюра", callback_data="B")],
    [InlineKeyboardButton("🦶 Подолог", callback_data="C")],
])

GROUP_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("👉 Войти в сообщество", url=GROUP_LINK)],
])

TEXTS = {
    "A": "🌱 Отлично! Подология — одна из самых востребованных профессий.\n\n📌 Скоро появится видео: *«Как войти в профессию и не потерять время и деньги»*\n\nА пока — присоединяйся к закрытому сообществу 👇",
    "B": "💅 Ты уже в деле — теперь время расти!\n\n📌 Скоро появится видео: *«Где мастер педикюра теряет деньги каждый месяц»*\n\nА пока — присоединяйся к закрытому сообществу 👇",
    "C": "🦶 Коллега! Даже опытные подологи находят здесь то чего не хватало.\n\n📌 Скоро появится видео: *«Почему даже опытные подологи теряют клиентов»*\n\nА пока — присоединяйся к закрытому сообществу 👇",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Скажи — кто ты?", reply_markup=KEYBOARD)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=TEXTS[query.data], parse_mode="Markdown", reply_markup=GROUP_KEYBOARD)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Нажми /start чтобы начать 👇")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))
    print("Бот запущен!")
    app.run_polling()
