import random

from telegram.ext import DispatcherHandlerStop, ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from . import zeroz, onez, twoz, threez, fourz, fivez, sixz, sevenz
from db.crud import leaderboard_request


def clear_my_persistence(update, context):
    if len(context.args) > 0:
        if context.args[0] == context.bot_data['bot_pass']['convo_persist_pass']:
            context.bot_data['bot_pass']['convo_persist_pass'] = str(random.randrange(1000, 9999))
            update.message.reply_text("Operation Successful!")
            return -1
        elif context.args[0] == context.bot_data['bot_pass']['user_data_pass']:
            context.user_data.clear()
            context.bot_data['bot_pass']['user_data_pass'] = str(random.randrange(1000, 9999))
            update.message.reply_text("Operation Successful!")
        else:
            update.message.reply_text("Operation Failed!!\nIncorrect Password")
    else:
        update.message.reply_text("Operation Failed!!\nYou Don't have PERMISSION to do this right Now")
    raise DispatcherHandlerStop


def get_leaderboard(update, context):
    context.user_data['reply_view_board'].append(update.message.reply_text("Loading...").message_id)
    data = leaderboard_request(context.bot_data['today_leaderboard_initial'])
    counter = 1
    data_view = """
🎖 Today's Leaderboard
-------------------------------------

"""
    for y in data.values():
        data_view += f"#{counter}. {y[1]} : {y[0]}\n"
        counter += 1
    context.user_data['reply_view_board'].append(update.message.reply_text(data_view).message_id)


primary_convo = ConversationHandler(
    entry_points=[CommandHandler('start', zeroz.start)],
    states={
        0: [
            MessageHandler(Filters.status_update.web_app_data, zeroz.web_app_data),
            MessageHandler(Filters.text & Filters.regex("^📖Browse$"), twoz.home),
            MessageHandler(Filters.text & Filters.regex("^🔍Search$"), threez.home),
            MessageHandler(Filters.text & Filters.regex("^👥Profile$"), fourz.home),
            MessageHandler(Filters.text & Filters.regex("^⁉️Help$"), fivez.home),
            MessageHandler(Filters.text & Filters.regex("^📥Contact Us$"), sixz.home),
            MessageHandler(Filters.text & Filters.regex("^🎖 Leaderboard$"), get_leaderboard),
            MessageHandler(Filters.text & Filters.regex("^ℹ️About$"), sevenz.home),
        ],
        1: [
            MessageHandler(Filters.text & Filters.regex("^✅ Submit$"), onez.save_cb),
            MessageHandler(Filters.status_update.web_app_data, zeroz.web_app_data),
            MessageHandler(Filters.text & Filters.regex("^Back$"), onez.back)
        ],
        2: [
            MessageHandler(Filters.text & Filters.command & Filters.regex("^/\d+$"), twoz.mezmur_detail),
            CallbackQueryHandler(twoz.prev_page, pattern="^prev$"),
            CallbackQueryHandler(twoz.next_page, pattern="^next$"),
            MessageHandler(Filters.text & Filters.regex("^Back$"), zeroz.home),
            CallbackQueryHandler(zeroz.home, pattern="^back$"),
        ],
        21: [
            CallbackQueryHandler(twoz.home, pattern="^back$"),
        ],
        4: [
            # MessageHandler(Filters.text & Filters.command & Filters.regex("^/(MY_MEZMURS)$"), fourz.setting),
            MessageHandler(Filters.contact, fourz.register),
            MessageHandler(Filters.text & Filters.reply, fourz.set_name),
        ],
        41: [
            CallbackQueryHandler(fourz.set_lang)
        ],

    },
    fallbacks=[
        MessageHandler(Filters.text & Filters.regex("^Back$"), zeroz.home),
        CommandHandler('clear_my_persistence', clear_my_persistence),
        CommandHandler('CONTACT_US', sixz.home),
    ],
    allow_reentry=True,
    name="primary_convo",
    persistent=True
)
