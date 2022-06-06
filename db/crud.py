import requests

from const import MAIN_HOST


def get_mezmur_detail(idd):
    resp = requests.get(MAIN_HOST + "mezmurs/" + str(idd) + "/")
    return resp.json()


def get_size():
    resp = requests.get(MAIN_HOST + "mezmurs/size/")
    return resp.json()


def save_request(data):
    resp = requests.post(MAIN_HOST + "mezmurs/save/", data=data)
    return resp.json()


def store_for_edit(data):
    resp = requests.post(MAIN_HOST + "mezmurs/store_for_edit/", data=data)
    return resp.json()


def get_page_length():
    resp = requests.get(MAIN_HOST + "mezmurs/page/available/")
    return resp.json()


def change_page(val, context):
    context.user_data['page_num'] += val
    page_num = context.user_data['page_num'] % context.user_data['page_length']
    if page_num == 0:
        page_num = context.user_data['page_length']
    resp = requests.get(MAIN_HOST + "mezmurs/page/" + str(page_num) + "/")
    return resp.json()


def register_me(me):
    resp = requests.post(MAIN_HOST + "mezmurs/user/", data=me)
    return resp.json()


def update_me_request(uid):
    resp = requests.get(MAIN_HOST + "mezmurs/user/" + str(uid) + "/")
    return resp.json()


def leaderboard_request(idd):
    resp = requests.get(MAIN_HOST + "mezmurs/leaderboard/" + str(idd) + "/")
    return resp.json()