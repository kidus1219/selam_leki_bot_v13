from db.crud import save_request
from sensor.zeroz import home


def save_cb(update, context):
    resp = save_request(context.user_data['temp_mz'])
    update.message.reply_text(resp)
    return home(update, context)


def back(update, context):
    return home(update, context)