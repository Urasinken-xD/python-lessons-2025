from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import TOKEN
from random import randint, choice


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{randint(0, 999)}')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{update.message.text}')


zuefa_random = ["Камень","Ножницы", "Бумага"]
async def zuefa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{choice(zuefa_random)}')
app = ApplicationBuilder().token(TOKEN).build()


app.add_handler(CommandHandler("Zuefa", zuefa))
app.add_handler(CommandHandler("Hello", hello))
app.add_handler(CommandHandler("Random_number", random_number))
app.add_handler(MessageHandler(filters.ALL, echo))
print('Бот запущен')
app.run_polling()
print('Бот приостоновлен')

