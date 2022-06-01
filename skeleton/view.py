from copy import deepcopy

from telegram import InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

from const import TEXT_PH


class View:
    application = None  # maybe this should be instance variable
    ct = None

    @classmethod
    def get_application(cls, application):
        cls.application = application

    def __init__(self, template, shy=False, var_text=None, var_key=None, bird=False):
        # self.__class__.ct.create_snapshot(description=template['id'])

        self.text = template['text']
        self.keyboard_type = template['keyboard_type']
        self.raw_keyboard = deepcopy(template['keyboard'])
        self.shy = shy
        self.markup = None
        self.return_call = template['return_call']
        if var_text is not None:
            self.mold_text(var_text)
        if var_key is not None:
            self.mold_key(var_key)
        keyrow = []
        keyboard = []
        if self.keyboard_type == "inline":
            for x in self.raw_keyboard:
                for y in x:
                    if not y[0]:
                        continue
                    if len(y) == 3:
                        keyrow.append(InlineKeyboardButton(text=y[0], web_app=WebAppInfo(url=y[2])))
                    else:
                        keyrow.append(InlineKeyboardButton(text=y[0], callback_data=y[1]))
                keyboard.append(keyrow)
                keyrow = []
            self.markup = InlineKeyboardMarkup(keyboard)
        elif self.keyboard_type == "reply":
            for x in self.raw_keyboard:
                for y in x:
                    if not y[0]:
                        continue
                    if len(y) == 1:
                        keyrow.append(y[0])
                    else:
                        if y[1] == "contact":
                            keyrow.append(KeyboardButton(text=y[0], request_contact=True))
                        elif y[1] == "location":
                            keyrow.append(KeyboardButton(text=y[0], request_location=True))
                        else:  # check more, like poll ..
                            keyrow.append(KeyboardButton(text=y[0], web_app=WebAppInfo(url=y[1])))
                keyboard.append(keyrow)
                keyrow = []
            self.markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        elif self.keyboard_type == "remove":
            self.markup = ReplyKeyboardRemove()

    def mold_text(self, rry):
        for x in rry:
            self.text = self.text.replace(TEXT_PH, str(x),
                                          1)  # what happens if there are no TEXT_PH or amount of rry doesnt match??

    def mold_key(self, rry):
        for x in rry:
            self.raw_keyboard[x[0]][x[1]] = x[2]
    def printer(self, chat_id):
        inline_view_board = self.__class__.application.user_data[chat_id].setdefault('inline_view_board', None)
        if self.keyboard_type == "inline":
            if not inline_view_board:
                self.__class__.application.user_data[chat_id][
                    'inline_view_board'] = self.__class__.application.bot.send_message(chat_id=chat_id,
                                                                                             text=self.text,
                                                                                             protect_content=True,
                                                                                             parse_mode="html",
                                                                                             reply_markup=self.markup)
            else:
                self.__class__.application.user_data[chat_id]['inline_view_board'] = inline_view_board.edit_text(
                    text=self.text, parse_mode="html", reply_markup=self.markup)
        else:
            if not not inline_view_board:
                inline_view_board.delete()
                self.__class__.application.user_data[chat_id]['inline_view_board'] = None
            self.__class__.application.bot.send_message(chat_id=chat_id, text=self.text, parse_mode="html",
                                                              reply_markup=self.markup)

        return self.return_call

    def __repr__(self):
        return self.text
