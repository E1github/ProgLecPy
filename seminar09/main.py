# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     bar.next()
# bar.finish()



from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from telegram.ext import filters
app = ApplicationBuilder().token("5476492755:AAFZgt5w3WTZOC8Nzh9556qkOroWBtQwl7I").build()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, любимая Татьяна!")

async def start2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message.text
    await update.message.reply_text(' '.join(list(filter(lambda element: 'при' not in element.lower(), m.split()))))
    

app.add_handler(CommandHandler("hola", hello))
app.add_handler(CommandHandler("candy", start))
app.add_handler(MessageHandler(filters.TEXT, start2))
# app.add_handler(MessageHandler(filters.Text('слышь, хеллоу!'), start))

print('start')
app.run_polling()