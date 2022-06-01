from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from . import zeroz, onez, twoz, threez, fourz, fivez, sixz, sevenz

primary_convo = ConversationHandler(
    entry_points=[CommandHandler('start', zeroz.start)],
    states={
        0: [
            MessageHandler(Filters.status_update.web_app_data, zeroz.web_app_data),
            MessageHandler(Filters.text & Filters.regex("^Add New$"), onez.home),
            MessageHandler(Filters.text & Filters.regex("^Browse$"), twoz.home),
            MessageHandler(Filters.text & Filters.regex("^Search$"), threez.home),
            MessageHandler(Filters.text & Filters.regex("^Profile$"), fourz.home),
            MessageHandler(Filters.text & Filters.regex("^Help$"), fivez.home),
            MessageHandler(Filters.text & Filters.regex("^Contact Us$"), sixz.home),
            MessageHandler(Filters.text & Filters.regex("^About$"), sevenz.home),
        ],
        1: [
            MessageHandler(Filters.text & Filters.regex("^✅ Submit$"), onez.save_cb),
            MessageHandler(Filters.status_update.web_app_data, zeroz.web_app_data),
            MessageHandler(Filters.text & Filters.regex("^Back$"), zeroz.home)
        ],
        2: [
            MessageHandler(Filters.text & Filters.command & Filters.regex("^/\d+$"), twoz.mezmur_detail),
            CallbackQueryHandler(twoz.prev_page, pattern="^prev$"),
            CallbackQueryHandler(twoz.next_page, pattern="^next$"),
            MessageHandler(Filters.text & Filters.regex("^Back$"), zeroz.home)
        ],
        21: [
            MessageHandler(Filters.text & Filters.text("^Back$"), twoz.home)
        ],
        4: [
            MessageHandler(Filters.text & Filters.command & Filters.regex("^/(NAME|LANG|ACCEPTED)$"), fourz.setting),
            MessageHandler(Filters.contact, fourz.register),
        ],
        43: [
            #CallbackQueryHandler(set_lang_cb)
        ],

    },
    fallbacks=[MessageHandler(Filters.text & Filters.regex("^Back$"), zeroz.home)]
)
