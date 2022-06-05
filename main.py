import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, TypeHandler, DispatcherHandlerStop

from config import TOKEN, PORT, DATABASE_URL
from db.postgrespersistence import PostgresPersistence
from skeleton.view import View
from sensor.primary import primary_convo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# ct = classtracker.ClassTracker()
# ct.track_class(View, name=str(View))


def chk(update, context):
    # print(ct.stats.print_summary())
    pass


def wait_abit_cb(update, context):
    print(context.user_data.get('lock', "none"))
    if context.user_data.get('lock', False):
        update.message.reply_text("wait a lil bit,,")
        raise DispatcherHandlerStop


def input_cleaner(update: Update, context):
    if context.user_data.get('clean_input', True):
        update.message.delete()
    else:
        context.user_data['clean_input'] = True


if __name__ == '__main__':
    updater = Updater(TOKEN, persistence=PostgresPersistence(url=DATABASE_URL))
    application = updater.dispatcher
    View.application = application
    # View.ct = ct

    # application.user_data['lock'] = False
    application.add_handler(TypeHandler(Update, input_cleaner), 1)
    application.add_handler(primary_convo)
    application.add_handler(CommandHandler('chk', chk))
    #  start weebhook
    # updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://selam-leki-bot-v13.herokuapp.com/' + TOKEN, drop_pending_updates=True)
    updater.start_polling(drop_pending_updates=True)
    updater.idle()
