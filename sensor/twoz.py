from const import ONE_PAGE_LENGTH, STAR_HOLDER, MAIN_HOST
from db.crud import change_page, get_page_length, get_one, get_size, get_mezmur_detail
from skeleton import template
from skeleton.view import View


def home(update, context):
    context.user_data['page_length'] = get_page_length()
    data = change_page(0, context)
    temp = ""
    for x in data:
        temp += "/" + str(x[0]) + " " + x[1] + "\n\n"
    View(template.JUST_BACK, var_text=["✅ Browser Page"]).printer(update.effective_chat.id)
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
    if given > context.user_data['page_length'] * ONE_PAGE_LENGTH or given < 1:
        update.message.reply_text("invalid input!\nThis mezmur Doesn't exist")
        return
    data = get_mezmur_detail(given)
    if data.get('id', None) is None:
        update.message.reply_text("invalid input!\nThis mezmur Doesn't exist")
        return

    lyrics = ""
    for x in data['lyrics'].split("[አዝ]"):
        lyrics += x + "\n[አዝ]\n"
    star = STAR_HOLDER.replace("0", "*", data['star'])
    View(template.JUST_BACK, var_text=["✅ Browser Page"]).printer(update.effective_chat.id)
    View(template.BROWSE_LYRICS, var_text=[data['id'], star, data['title'], lyrics, data['artist']],
         var_key=[[0, 0, ["👁‍🗨 Reading Mode", "cb", MAIN_HOST + "mezmurs/reading_mode/" + str(given)]]]).printer(
        update.effective_chat.id)
    context.user_data['mz_size'] = get_size()
    return 21
