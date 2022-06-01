from telegram import Update
from telegram.ext import CallbackContext
from skeleton import template
from skeleton.view import View
from tool import setting_methods


def home(update, context):
    me = context.user_data['me']
    if me.is_registered:
        rtn = View(template.PROFILE, var_text=[me.name, me.lang, me.star, me.accepted, me.declined]).printer(
            update.effective_chat.id)
    else:
        rtn = View(template.PROFILE_UNREGISTERD).printer(update.effective_chat.id)
    return rtn


def setting(update: Update, context):
    given = update.message.text
    if given == "/NAME":
        context.user_data['to_be_set'] = "name"
        update.message.reply_text("Enter New Name", quote=True)
    elif given == "/LANG":
        return View(template.SET_LANG).printer(update.effective_chat.id)


def confirm_input_cb(update: Update, context: CallbackContext):
    context.user_data['accepted_input'] = update.message.text
    return View(template.CONFIRM_INPUT, var_text=[update.message.text]).printer(update.effective_chat.id)


def yes_cb(update: Update, context: CallbackContext):
    setting_methods[context.user_data['to_be_set']](context.user_data['accepted_input'], context.user_data['me'])
    update.callback_query.answer("Yes")
    return View(template.HOME).printer(update.effective_chat.id)


def no_cb(update: Update, context: CallbackContext):
    update.callback_query.answer("No")
    return View(template.HOME).printer(update.effective_chat.id)


def set_lang_cb(update: Update, context: CallbackContext):
    qry = update.callback_query.data
    if qry == "am":
        context.user_data['me'].lang = "Amharic"
        update.callback_query.answer("Amharic Language Has Been Set.")
    elif qry == "eng":
        update.callback_query.answer("English Language Has Been Set.")
        context.user_data['me'].lang = "English"
    return View(template.HOME).printer(update.effective_chat.id)


def register(update: Update, context: CallbackContext):
    data = update.message.contact
    me = context.user_data['me']
    me.phone = data.phone_number
    me.name = data.first_name
    me.uid = data.user_id
    me.is_registered = True
    update.message.reply_text(
        f"<code>Registration Successful</code>\n\n<b>{context.user_data['me'].name} WELCOME!!</b>", quote=True,
        parse_mode="html")
    return home(update, context)
