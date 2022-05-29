import requests

from const import MAIN_HOST


def get_one(idd, context=None):
    if context is not None:
        context.user_data['lock'] = True
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))
        resp = requests.get(MAIN_HOST + "mezmurs/one/" + str(idd))

        context.user_data['lock'] = False
    else:
        resp = requests.get(MAIN_HOST+"mezmurs/one/" + str(idd))
    return resp.json()


def get_three(idd, context=None):
    if context is not None:
        context.user_data['lock'] = True
        resp = requests.get(MAIN_HOST+"mezmurs/one/" + str(idd))
        context.user_data['lock'] = False
    else:
        resp = requests.get(MAIN_HOST+"mezmurs/one/" + str(idd))
    return resp.json()


def get_dozen_title(idd, size, context=None):
    if context is not None:
        context.user_data['lock'] = True
        resp = requests.get(MAIN_HOST+"mezmurs/dozen_title/" + str(idd) + "/" + str(size))
        context.user_data['lock'] = False
    else:
        resp = requests.get(MAIN_HOST+"mezmurs/dozen_title/" + str(idd) + "/" + str(size))
    return resp.json()


def get_size(context=None):
    if context is not None:
        context.user_data['lock'] = True
        resp = requests.get(MAIN_HOST+"mezmurs/size/")
        context.user_data['lock'] = False
    else:
        resp = requests.get(MAIN_HOST+"mezmurs/size/")
    return resp.json()


def save_request(idd, context=None):
    if context is not None:
        context.user_data['lock'] = True
        resp = requests.get(MAIN_HOST+"mezmurs/save/"+str(idd))
        context.user_data['lock'] = False
    else:
        resp = requests.get(MAIN_HOST+"mezmurs/save/"+str(idd))
    return resp.json()
