from db.crud import register_me


def up_to_data(old: dict, new: dict):
    for x, y in new.items():
        if x in old:
            old[x] = y


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
