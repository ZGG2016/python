import os
import shutil
import time


def login(session, api_url, user, passwd):
    """
    get login token and log in
    :param session:
    :param api_url:
    :param user:
    :param passwd:
    :return:
    """
    # 1. GET request to fetch login token
    params_0 = {
        'action': 'query',
        'format': 'json',
        'utf8': '',
        'meta': 'tokens',
        'type': 'login'
    }

    r = session.get(api_url, params=params_0)
    login_token = r.json()['query']['tokens']['logintoken']
    # 2. POST request to log in
    params_1 = {
        'action': 'login',
        'format': 'json',
        'utf8': '',
        'lgname': user,
        'lgpassword': passwd,
        'lgtoken': login_token
    }

    session.post(api_url, data=params_1)


def fetch_csrf_token(session, api_url, user, passwd):
    login(session, api_url, user, passwd)
    params_2 = {
        'action': 'query',
        'format': 'json',
        'meta': 'tokens'
    }
    r = session.get(api_url, params=params_2)
    # {'batchcomplete': '', 'query': {'tokens': {'csrftoken': '883bca8c14e42a91a67b9682d7d5cad46538d3cb+\\'}}}
    # print(r.json())
    return r.json()['query']['tokens']['csrftoken']


def backup_dirs(dirs):
    """
    将目录下的内容移动到备份目录，并清空当前目录
    :param dirs: 要备份的目录列表
    :return:
    """
    for d in dirs:
        if os.path.exists(d) and len(os.listdir(d)):
            current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
            new_dir = d + "_" + current_time
            os.mkdir(new_dir)

            paths = os.listdir(d)
            for path in paths:
                shutil.move(d + "\\" + path, new_dir)


def create_dirs(dirs):
    """
    创建不存在的目录
    :param dirs:
    :return:
    """
    for d in dirs:
        if not os.path.exists(d):
            os.mkdir(d)
