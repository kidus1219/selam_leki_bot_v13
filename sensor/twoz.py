from const import MAIN_HOST
from db.crud import change_page, get_page_length, get_mezmur_detail
from skeleton import template
from skeleton.view import View


def home(update, context):
    if update.callback_query:
        update.callback_query.answer("Browse Page")
    else:
        #update.message.reply_text("...", reply_markup=ReplyKeyboardRemove())
        context.user_data['page_num'] = 1
    context.user_data['page_length'] = get_page_length()
    data = change_page(0, context)
    temp = ""
    for x in data:
        temp += "/" + str(x[0]) + " " + x[1] + "\n\n"
    View(template.BROWSE_TITLE, var_text=[temp]).printer(update.effective_chat.id)
    return 2


def prev_page(update, context):
    temp = ""
    data = change_page(-1, context)
    for x in data:
        temp += "/" + str(x[0]) + " " + x[1] + "\n\n"
    View(template.BROWSE_TITLE, var_text=[temp]).printer(update.effective_chat.id)
    update.callback_query.answer("PAGE " + str(context.user_data['page_num']))


def next_page(update, context):
    temp = ""
    data = change_page(1, context)
    for x in data:
        temp += "/" + str(x[0]) + " " + x[1] + "\n\n"
    View(template.BROWSE_TITLE, var_text=[temp]).printer(update.effective_chat.id)
    update.callback_query.answer("PAGE " + str(context.user_data['page_num']))


def mezmur_detail(update, context):
    given = int(update.message.text.strip("/"))
    if given < 1:
        update.message.reply_text("invalid input!\nThis mezmur Doesn't exist")
        return
    mz = get_mezmur_detail(given)
    if mz.get('id', None) is None:
        update.message.reply_text("invalid input!\nThis mezmur Doesn't exist")
        return

    lyrics = ""
    for x in mz['lyrics'].split("[አዝ]"):
        lyrics += x + "\n[አዝ]\n"
    STAR_HOLDER = "0 0 0"
    STAR_HOLDER.replace("0", "🎖", mz['star'])
    # View(template.BROWSE_LYRICS, var_text=[mz['id'], star, mz['title'], lyrics, mz['artist']], var_key=[[0, 1, ["✍️Modify", "cb", MAIN_HOST + "mezmurs/modify/" + str(given)+"/"]], [1, 0, ["👁‍🗨 Reading Mode", "cb", MAIN_HOST + "mezmurs/reading_mode/" + str(given)+"/"]]]).printer(update.effective_chat.id)
    View(template.BROWSE_LYRICS, var_text=[mz['id'], STAR_HOLDER, mz['title'], lyrics, mz['artist']], var_key=[[0, 0, ["👁‍🗨 Reading Mode", "cb", MAIN_HOST + "mezmurs/reading_mode/" + str(given) + "/"]]]).printer(update.effective_chat.id)
    return 21
