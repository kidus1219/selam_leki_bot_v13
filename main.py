import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, TypeHandler
from config import TOKEN, PORT, DATABASE_URL
from db.postgrespersistence import PostgresPersistence
from skeleton.view import View
from sensor.primary import primary_convo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def cleaner(update: Update, context: CallbackContext):
    if update.message is None:
        return
    if context.user_data.get('clean_input', True):
        try:
            update.message.delete()
        except Exception as e:
            print("cleaner Failed ", e)
    else:
        context.user_data['clean_input'] = True


def get_bot_pass(update: Update, context: CallbackContext):
    update.message.reply_text(str(context.bot_data['bot_pass']))


if __name__ == '__main__':
    # updater = Updater(TOKEN, persistence=PostgresPersistence(url=DATABASE_URL))
    updater = Updater(TOKEN)
    application = updater.dispatcher
    application.bot_data['bot_pass'] = {'convo_persist_pass': "1234", 'user_data_pass': "5678"}
    application.bot_data['today_leaderboard_initial'] = 21
    View.application = application

    application.add_handler(TypeHandler(Update, cleaner), -1)
    application.add_handler(primary_convo)
    application.add_handler(CommandHandler('get_bot_pass', get_bot_pass, filters=Filters.user(user_id=[543495028])))

    # updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://selam-leki-bot-v13.herokuapp.com/' + TOKEN, drop_pending_updates=True)
    updater.start_polling(drop_pending_updates=True)
    updater.idle()
