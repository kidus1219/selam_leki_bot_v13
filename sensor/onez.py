from skeleton import template
from skeleton.view import View


def home(update, context):
    return View(template.ADD_NEW).printer(update.effective_chat.id)


def save_cb(update, context):
    resp = save_request(context.user_data['temp_idd'], update.effective_chat.id)
    update.message.reply_text(resp)
    return View(template.HOME).printer(update.effective_chat.id)


