from telegram import Update
from telegram.ext import CallbackContext
from db.crud import update_me_request, register_me
from skeleton import template
from skeleton.view import View
from tool import up_to_data


def home(update, context):
    if context.user_data['me']['is_registered']:
        up_to_data(context.user_data['me'], update_me_request(update.effective_chat.id))
        me = context.user_data['me']
        rtn = View(template.PROFILE, var_text=[me['name'], me['lang'], me['star'], me['my_mezmurs']]).printer(
            update.effective_chat.id)
    else:
        rtn = View(template.PROFILE_UNREGISTERD).printer(update.effective_chat.id)
    return rtn


"""
def setting(update: Update, context):
    given = update.message.text
    if given == "/NAME":
        update.message.reply_text("Enter Your New Name", reply_markup=ForceReply(input_field_placeholder="Write in the reply"))    
    elif given == "/LANG":
        return View(template.SET_LANG).printer(update.effective_chat.id)
    elif given == "/MY_MEZMURS":
        update.message.reply_text("Enter Your New Name", reply_markup=ForceReply(input_field_placeholder="Write in the reply"))

"""


def set_name(update: Update, context: CallbackContext):
    if update.message.reply_to_message.text == "Enter Your New Name":
        context.user_data['me']['name'] = update.message.text
    return home(update, context)


def set_lang(update: Update, context: CallbackContext):
    qry = update.callback_query.data
    if qry == "am":
        context.user_data['me']['lang'] = "Amharic"
        update.callback_query.answer("Amharic Language Has Been Set.")
    elif qry == "eng":
        update.callback_query.answer("English Language Has Been Set.")
        context.user_data['me']['lang'] = "English"
    return home(update, context)


def register(update: Update, context: CallbackContext):
    data = update.message.contact
    me = context.user_data['me']
    me['phone'] = data.phone_number
    me['name'] = data.first_name
    me['uid'] = data.user_id
    if register_me(me) == "error":
        update.message.reply_text("Registration Failed1!\nPlease Try again\nIf the problem still persist ask /CONTACT_US")
    else:
        me['is_registered'] = True
        context.user_data['reply_view_board'].append(update.message.reply_text(f"<code>Registration Successful</code>\n\n<b>{context.user_data['me']['name']} WELCOME!!</b>", parse_mode="html").message_id)
    return home(update, context)
