import requests

from const import MAIN_HOST


def set_name(val, me):
    me.name = val


def set_lang(val, me):
    me.name = val


setting_methods = {
    'name': set_name,
    'lang': set_lang
}


def clean_inlines(function):
    def wrapper(*args, **kwargs):
        print("decorating")
        return function(*args, **kwargs)
    return wrapper


@clean_inlines
def say_this(p):
    print(p)


