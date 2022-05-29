import json

from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

from const import DOZEN_TITLE_SIZE, MAIN_HOST
from db.crud import get_dozen_title, get_size, get_one, save_request
from skeleton.view import View
from skeleton import template


def start(update, context):
    # Me(update.effective_chat.id, update.from_user.full_name)
    context.user_data['lock'] = False
    context.user_data['mz_dir'] = [None, None]
    context.user_data['current_mz_id'] = 1
    context.user_data['mz_size'] = 21
    context.user_data['temp_idd'] = 0
    context.user_data['dozen_title_start'] = 1
    context.user_data['dozen_title_end'] = DOZEN_TITLE_SIZE
    return View(template.HOME).printer(update.effective_chat.id)


def home_cb(update, _):
    return View(template.HOME).printer(update.effective_chat.id)


def add_new_cb(update, context):
    return View(template.ADD_NEW).printer(update.effective_chat.id)


def web_app_data(update, context):
    data = json.loads(update.effective_message.web_app_data.data)
    context.user_data['temp_idd'] = data['idd']
    lyrics = ""
    for x in data['lyrics']:
        lyrics += x + "\n\n"
    return View(template.REVIEW_MEZMUR, var_text=[data['title'], lyrics, data['artist'][1] + " " + data['artist'][2]], var_key=[[0, 1, ["✍️Edit", f"{MAIN_HOST}mezmurs/edit/"+str(data['idd'])]]]).printer(update.effective_chat.id)


def browse_cb(update, context):
    # reset dozone_title_start and end on fresh browser page
    data = get_dozen_title(context.user_data['dozen_title_start'], context.user_data['dozen_title_end'])
    temp = ""
    for x in data:
        temp += "/"+str(x[0])+" "+x[1]+"\n\n"
    View(template.JUST_BACK, var_text=["✅ Browser Page"]).printer(update.effective_chat.id)
    View(template.BROWSE_TITLE, var_text=[temp]).printer(update.effective_chat.id)
    context.user_data['mz_size'] = get_size()
    return 2


def search_cb(update, _):
    return View(template.SEARCH).printer(update.effective_chat.id)


def setting_cb(update, _):
    return View(template.SETTING).printer(update.effective_chat.id)


def help_cb(update, _):
    return View(template.HELP).printer(update.effective_chat.id)


def contact_us_cb(update, _):
    return View(template.CONTACT_US).printer(update.effective_chat.id)


def about_cb(update, _):
    return View(template.ABOUT).printer(update.effective_chat.id)


# PAGE 1
def save_cb(update, context):
    resp = save_request(context.user_data['temp_idd'])
    update.message.reply_text(resp)
    return View(template.HOME).printer(update.effective_chat.id)


# PAGE 2
def prev_cb(update, context):
    if context.user_data['dozen_title_start'] <= 1:
        update.callback_query.answer("LAST PAGE")
        return
    if context.user_data['dozen_title_start'] - DOZEN_TITLE_SIZE > 1:
        context.user_data['dozen_title_start'] -= DOZEN_TITLE_SIZE
    else:
        context.user_data['dozen_title_start'] = 1
    context.user_data['dozen_title_end'] = context.user_data['dozen_title_start'] + DOZEN_TITLE_SIZE - 1

    data = get_dozen_title(context.user_data['dozen_title_start'], context.user_data['dozen_title_end'])
    temp = ""
    for x in data:
        temp += "/"+str(x[0])+" "+x[1]+"\n\n"
    View(template.BROWSE_TITLE, var_text=[temp]).printer(update.effective_chat.id)
    update.callback_query.answer("🟩")


def next_cb(update, context):
    if context.user_data['dozen_title_end'] >= context.user_data['mz_size']:
        update.callback_query.answer("LAST PAGE")
        return
    if context.user_data['dozen_title_end'] + DOZEN_TITLE_SIZE < context.user_data['mz_size']:
        context.user_data['dozen_title_end'] += DOZEN_TITLE_SIZE + 1
    else:
        context.user_data['dozen_title_end'] += context.user_data['mz_size'] - context.user_data['dozen_title_end']
    context.user_data['dozen_title_start'] = context.user_data['dozen_title_end'] - DOZEN_TITLE_SIZE

    data = get_dozen_title(context.user_data['dozen_title_start'], context.user_data['dozen_title_end'])
    temp = ""
    for x in data:
        temp += "/"+str(x[0])+" "+x[1]+"\n\n"
    View(template.BROWSE_TITLE, var_text=[temp]).printer(update.effective_chat.id)
    update.callback_query.answer("🟩")


def browse_lyrics_cb(update, context):
    given = int(update.message.text.strip("/"))
    if given >= context.user_data['dozen_title_end']+1 or given < 1:
        print("invalid input")
        update.message.reply_text("invalid input!\nmaybe it's on another page")
        return
    data = get_one(given)
    lyrics = ""
    for x in data['lyrics'].split("[አዝ]"):
        lyrics += x + "\n\n"
    View(template.JUST_BACK, var_text=["✅ Browser Page"]).printer(update.effective_chat.id)
    View(template.BROWSE_LYRICS, var_text=[data['id'], data['title'], lyrics], var_key=[[0, 0, ["👁‍🗨", "cb", MAIN_HOST+"mezmurs/reader/"+str(given)]]]).printer(update.effective_chat.id)
    context.user_data['mz_size'] = get_size()
    return 21









primary_convo = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        0: [
            MessageHandler(Filters.status_update.web_app_data, web_app_data),
            MessageHandler(Filters.text & Filters.regex("^Add New$"), add_new_cb),
            MessageHandler(Filters.text & Filters.regex("^Browse$"), browse_cb),
            MessageHandler(Filters.text & Filters.regex("^Search$"), search_cb),
            MessageHandler(Filters.text & Filters.regex("^Setting$"), setting_cb),
            MessageHandler(Filters.text & Filters.regex("^Help$"), help_cb),
            MessageHandler(Filters.text & Filters.regex("^Contact Us$"), contact_us_cb),
            MessageHandler(Filters.text & Filters.regex("^About$"), about_cb),
        ],
        1: [
            MessageHandler(Filters.text & Filters.regex("^✅ Submit$"), save_cb),
            MessageHandler(Filters.status_update.web_app_data, web_app_data),
            MessageHandler(Filters.text & Filters.regex("^Back$"), home_cb)
        ],
        2: [
            MessageHandler(Filters.text & Filters.command & Filters.regex("^/\d+$"), browse_lyrics_cb),
            CallbackQueryHandler(prev_cb, pattern="^prev$"),
            CallbackQueryHandler(next_cb, pattern="^next$"),
            MessageHandler(Filters.text & Filters.regex("^Back$"), home_cb)
        ],
        21: [
            MessageHandler(Filters.text & Filters.text("^Back$"), browse_cb)
        ]
    },
    fallbacks=[MessageHandler(Filters.text & Filters.text("^Back$"), home_cb)]
)
