my_token = '6018418911:AAGhHGPaOu-Cz7J9F0ZmLnxfLL_rMgme0vk'

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import user_interface as ui
import model_racional as mr

async def my_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    my_list = ui.get_n(text)
    # await update.message.reply_text(func.calc(text))
    await update.message.reply_text(mr.get_result(my_list))
    
app = ApplicationBuilder().token(my_token).build()

app.add_handler(MessageHandler(filters.TEXT, my_calc))

app.run_polling()

