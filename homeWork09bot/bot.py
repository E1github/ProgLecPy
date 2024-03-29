my_token = '6018418911:AAGhHGPaOu-Cz7J9F0ZmLnxfLL_rMgme0vk'

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters, Updater
import logging

import user_interface as ui
import model_racional as mr
import tictactoe as ttt

logging.basicConfig(level=logging.INFO, filename="bot.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


print('running...')

async def my_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    my_list = ui.get_n(text)
    logging.info(f"The expression from user: {text}.")
    result = mr.get_result(my_list)
    logging.info(f"The result from function: {result}.")
    # await update.message.reply_text(func.calc(text))
    await update.message.reply_text(result)
    
# async def my_tictactoe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     app.add_handler(CallbackQueryHandler(ttt.button))  # добавление обработчика на CallBack кнопки
#     ttt.newGame

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Сообщение о функциональности бота с командами
    await update.message.reply_text("Это бот позволяет играть в крестики-нолики, считать на калькуляторе и вести базу школьников.")
    await update.message.reply_text("Для игры в крестики-нолики введите /tictactoe,\nподсчетов на калькуляторе /calc, \nведения базы телефонов /phones.")
    
async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Функция для работы калькутора
    await update.message.reply_text("Введи выражение для подсчета используя простые или комплексные числа (через j), операторы +,-,*,/ или скобки.")
    app.add_handler(MessageHandler(filters.TEXT, my_calc))

async def tictactoe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Функция для работы крестиков-ноликов
    await update.message.reply_text("Для старта игры в крестики-нолики набери /game")
    app.add_handler(CallbackQueryHandler(ttt.button))  # добавление обработчика на CallBack кнопки
    app.add_handler(CommandHandler("game", ttt.newGame))
    
    
app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("tictactoe", tictactoe_command))


# app.add_handler(MessageHandler(filters.TEXT, my_calc))

app.run_polling()

