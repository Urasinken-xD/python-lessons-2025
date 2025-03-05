from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import TOKEN
from random import randint, choice
import logging




async def du_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{randint(0, 99999999999999999999999999999999999999)}')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{update.message.text}')


zuefa_random = ["Камень","Ножницы", "Бумага"]
async def zuefa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{choice(zuefa_random)}')



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Рассказывает, какие ф-ции доступны у бота"""

    text = [
        f'Привет, {user.first_name}! ',
        'Я школьный бот, который может реагировать на следующие команды',
        '/hello,/Start - говорю привет',
        '/du_help - покажу список доступных команд',
        '/zuefa - сыграю с тобой в цуефа'
        '/random_number - напишу случайное число'
    ]
    text = '\n'.join(text)
    await update.message.reply_text(f'{update.message.text}')

app = ApplicationBuilder().token(TOKEN).build()


#Регестрация обработчиков
app.add_handler(CommandHandler("Hello", hello))
app.add_handler(CommandHandler(["Help", "Start"], help))
app.add_handler(CommandHandler("Random_number", random_number))
app.add_handler(MessageHandler(["камень", "ножницы", "бумага"], zuefa))
app.add_handler(MessageHandler(filters.ALL, echo))
print('Бот запущен')
app.run_polling()
print('Бот приостоновлен')

