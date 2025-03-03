from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config import TOKEN

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token("8145363054:AAHgz7xsLj5fTK6ywBYtfquOGBfxrFDSREs").build()

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{update.message.text}')

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.ALL, echo))
print('Бот запущен')
app.run_polling()
print('Бот приостоновлен')