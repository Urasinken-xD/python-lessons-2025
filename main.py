import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

from config import TOKEN

from random import randint, choice


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(module)-15s [%(lineno)4d] - %(message)s'
)
logging.getLogger('httpx').setLevel(logging.WARNING)
log = logging.getLogger(__name__)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Реагирует на команду '/hello' и говорит привет"""
    user = update.effective_user
    log.info(f'Функция hello вызвана пользователем {user}')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Реагирует на команду '/random_number' и выдает случайное число"""
    user = update.effective_user
    log.info(f'Функция random_number вызвана пользователем {user}\n')
    await update.message.reply_text(f'{randint(0, 99999999999999999999999999999999999999)}')


zuefa_random = "камень, ножницы, бумага"


async def zuefa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Сыграет, с пользователем в цуефа"""
    user = update.effective_user
    log.info(f'Функция zuefa вызвана пользователем {user}\n')

    await update.message.reply_text(f'{choice(zuefa_random)}')


async def say_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Рассказывает, какие ф-ции доступны у бота"""
    user = update.effective_user
    log.info(f'Функция help вызвана пользователем {user}\n')

    text = [
        f'Привет, {user.first_name}! ',
        'Я школьный бот, который может реагировать на следующие команды',
        '/hello - говорю привет',
        '/help, /start - покажу список доступных команд',
        'Если хочешь поиграть со мной цуефа, просто напиши "камень", "ножницы" или "бумага"',
        '/random_number - напишу случайное число',
        '/say_keyboard - покажу клавиатуру'
    ]
    text = '\n'.join(text)

    await update.message.reply_text(text)


async def say_keybord(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показывает клавиатуру"""
    user = update.effective_user
    log.info(f'Функция say_keybord вызвана пользователем {user}')

    buttons = [
        [InlineKeyboardButton('Раз', callback_data='Раз'),
         InlineKeyboardButton('Два', callback_data='Два'),
         InlineKeyboardButton('Три', callback_data='Три')],
        [InlineKeyboardButton('Четыре', callback_data='Четыре'),
         InlineKeyboardButton('Пять', callback_data='Пять')],
        [InlineKeyboardButton('Шесть', callback_data='Шесть')]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        text='Выберите опцию на кклавиатуре',
        reply_markup=keyboard
    )


async def react_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Реагирует на нажатие кнопки на клавиатуре"""
    user = update.effective_user
    log.info(f'Функция react_keyboard вызвана пользователем {user}')

    query = update.callback_query

    buttons = [
        [InlineKeyboardButton('Раз', callback_data='Раз'),
         InlineKeyboardButton('Два', callback_data='Два'),
         InlineKeyboardButton('Три', callback_data='Три')],
        [InlineKeyboardButton('Четыре', callback_data='Четыре'),
         InlineKeyboardButton('Пять', callback_data='Пять')],
        [InlineKeyboardButton('Шесть', callback_data='Шесть')]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await query.edit_message_text(
        text=query.data,
        reply_markup=keyboard
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Функция, реагирующая эхом на любое сообщение"""
    user = update.effective_user
    message = update.message
    log.info(f'Функция echo вызвана пользователем {user}\n' + ' ' * 73 + f'{message = }')
    await update.message.reply_text(f'{update.message.text}')


app = ApplicationBuilder().token(TOKEN).build()


#Регестрация обработчиков
app.add_handler(CommandHandler("Hello", hello))
app.add_handler(CommandHandler(["Help", "Start"], say_help))
app.add_handler(CommandHandler('keyboard', say_keybord))
app.add_handler(CommandHandler("Random_number", random_number))
app.add_handler(MessageHandler(filters.Text(["камень", "ножницы", "бумага"]), zuefa))
app.add_handler(MessageHandler(filters.ALL, echo))
print('Бот запущен')
app.run_polling()
print('Бот приостоновлен')