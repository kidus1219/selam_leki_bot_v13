import json
from telegram import ReplyKeyboardRemove
from const import MAIN_HOST, STAR_HOLDER
from db.crud import get_mezmur_detail, store_for_edit
from skeleton import template
from skeleton.me import Me
from skeleton.view import View


def home(update, context):
    if update.callback_query:
        update.callback_query.answer("Home Page")
    if True or context.user_data['me'].is_registered:
        rtn = View(template.HOME, var_text=["<code>Select an option from below</code>"]).printer(update.effective_chat.id)
    else:
        rtn = View(template.HOME, var_text=[f"<b>Hi, {context.user_data['me'].name}!</b>\n\n<code>In order to access all features like </code><b>adding new mezmur,</b><code> please register by going to Profile.</code>"], var_key=[[0, 0, [None]]]).printer(update.effective_chat.id)
    return rtn


def start(update, context):
    context.user_data['me'] = Me(update.effective_chat.id, update.message.from_user.username, update.message.from_user.full_name)
    context.user_data['lock'] = False
    context.user_data['clean_input'] = True
    context.user_data['page_num'] = 1
    context.user_data['page_length'] = 0
    context.user_data['accepted_input'] = None
    context.user_data['to_be_set'] = None
    return home(update, context)


def web_app_data(update, context):
    data = json.loads(update.effective_message.web_app_data.data)
    if data.get('from', None) == "search":
        mz = get_mezmur_detail(data.get('id', 0))
        if mz.get('id', None) is None:
            update.message.reply_text("Sorry!\nThis mezmur Doesn't exist")
            return
        lyrics = ""
        for x in mz['lyrics'].split("[አዝ]"):
            lyrics += x + "\n[አዝ]\n"
        star = STAR_HOLDER.replace("0", "🎖", mz['star'])
        update.message.reply_text("...", reply_markup=ReplyKeyboardRemove())
        return View(template.BROWSE_LYRICS, var_text=[mz['id'], star, mz['title'], lyrics, mz['artist']], var_key=[[0, 1, ["✍️Modify", "cb", MAIN_HOST + "mezmurs/modify/" + str(data['id']) + "/"]], [1, 0, ["👁‍🗨 Reading Mode", "cb", MAIN_HOST + "mezmurs/reading_mode/" + str(data['id']) + "/"]]]).printer(update.effective_chat.id)
    else:
        print(data)
        lyrics = ""
        context.user_data['temp_mz'] = data
        context.user_data['temp_mz']['user'] = update.effective_chat.id
        store_for_edit(context.user_data['temp_mz'])
        for x in data['lyrics']:
            lyrics += x + "\n\n"
        return View(template.REVIEW_MEZMUR, var_text=[data['title'], lyrics, data['artist'][1] + " " + data['artist'][2]], var_key=[[0, 1, ["✍️Edit", f"{MAIN_HOST}mezmurs/edit/"+str(update.effective_chat.id)+"/"]]]).printer(update.effective_chat.id)

