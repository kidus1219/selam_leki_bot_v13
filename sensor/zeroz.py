import json

from const import MAIN_HOST
from skeleton import template
from skeleton.me import Me
from skeleton.view import View


def home(update, context):
    if context.user_data['me'].is_registered:
        rtn = View(template.HOME, var_text=["<code>Select an option from below</code>"]).printer(update.effective_chat.id)
    else:
        rtn = View(template.HOME, var_text=[f"<b>Hi, {context.user_data['me'].name}!</b>\n\n<code>In order to access all features like </code><b>adding new mezmur,</b><code> please register by going to Profile.</code>"], var_key=[[0, 0, [None]]]).printer(update.effective_chat.id)
    return rtn


def start(update, context):
    context.user_data['me'] = Me(update.effective_chat.id, update.message.from_user.username,
                                 update.message.from_user.full_name)
    context.user_data['lock'] = False
    context.user_data['mz_dir'] = [None, None]
    context.user_data['current_mz_id'] = 1
    context.user_data['mz_size'] = 21
    context.user_data['temp_idd'] = 0
    context.user_data['dozen_title_start'] = 1

    context.user_data['page_num'] = 1
    context.user_data['page_length'] = 0

    context.user_data['accepted_input'] = None
    context.user_data['to_be_set'] = None
    return home(update, context)


def web_app_data(update, context):
    data = json.loads(update.effective_message.web_app_data.data)
    context.user_data['temp_idd'] = data['idd']
    lyrics = ""
    for x in data['lyrics']:
        lyrics += x + "\n\n"
    return View(template.REVIEW_MEZMUR, var_text=[data['title'], lyrics, data['artist'][1] + " " + data['artist'][2]],
                var_key=[[0, 1, ["✍️Edit", f"{MAIN_HOST}mezmurs/edit/" + str(data['idd'])]]]).printer(
        update.effective_chat.id)

