import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

from config import TOKEN


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(module)-15s [%(lineno)4d] - %(message)s'
)
logging.getLogger('httpx').setLevel(logging.WARNING)
log = logging.getLogger(__name__)


async def ask_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
   log.info(f'ask_date is triggered by  {update.effective_user}')
   text = 'Когда будет мероприятие?'
   pass

async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    log.info(f'get_date is triggered by  {update.effective_user}')
    return await ask_place(Update, context)


async def ask_place(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    log.info(f'ask_place is triggered by  {update.effective_user}')
    pass

async def get_place(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    log.info(f'get_place is triggered by  {update.effective_user}')
    pass


async def register_aplication(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    log.info(f'register_aplication is triggered by  {update.effective_user}')

    return ConversationHandler.END


events_aplicatuion_handler = ConversationHandler(
    entry_points=[CommandHandler('events', ask_date())]
)