my_token = '6018418911:AAGhHGPaOu-Cz7J9F0ZmLnxfLL_rMgme0vk'

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters, Updater

import user_interface as ui
import model_racional as mr
import tictactoe as ttt

print('running...')

async def my_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    my_list = ui.get_n(text)
    # await update.message.reply_text(func.calc(text))
    await update.message.reply_text(mr.get_result(my_list))
    
async def my_tictactoe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    app.add_handler(CallbackQueryHandler(ttt.button))  # добавление обработчика на CallBack кнопки
    ttt.game

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Сообщение о функциональности бота с командами."""
    await update.message.reply_text("Это бот позволяет играть в крестики-нолики, считать на калькуляторе и вести базу школьников.")
    await update.message.reply_text("Для игры в крестики-нолики введите /tictactoe,\nподсчетов на калькуляторе /calc, \nведения базы телефонов /phones.")
    
async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Функция для работы калькутора."""
    await update.message.reply_text("Введи выражение для подсчета используя простые или комплексные числа (через j), операторы +,-,*,/ или скобки.")
    app.add_handler(MessageHandler(filters.TEXT, my_calc))

async def tictactoe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Функция для работы крестиков-ноликов."""
    # global app
    # app.add_handler(CallbackQueryHandler(ttt.button))
    await update.message.reply_text("Давай поиграем в крестики-нолики...")
    app.add_handler(CallbackQueryHandler(ttt.button))  # добавление обработчика на CallBack кнопки
    ttt.game
    
    # app.add_handler(MessageHandler(filters.TEXT, my_tictactoe))
    
app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("tictactoe", tictactoe_command))


# app.add_handler(MessageHandler(filters.TEXT, my_calc))

app.run_polling()

