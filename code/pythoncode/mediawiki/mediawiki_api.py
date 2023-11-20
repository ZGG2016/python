# -----------------------------------------------------
# Name: mediawiki_api
# Description: mediawiki 的 python api 接口测试
# Date: 2023.10.25
# ------------------------------------------------------
import sys
import requests
from utils import login, fetch_csrf_token


def get_all_categories(session, api_url, user, passwd):
    """
    获取所有的分类名称
    :param session:
    :param api_url:
    :param user:
    :param passwd:
    :return:
    """

    params = {
        "action": "query",
        "format": "json",
        "list": "allcategories",
    }
    login(session, api_url, user, passwd)
    response = session.get(url=api_url, params=params)
    categories = []
    for item in response.json()["query"]["allcategories"]:
        categories.append(item['*'])

    return categories


def create_or_edit_page(session, title, content, api_url, user, passwd, create_only):
    """
    创建或编辑页面
    :param session:
    :param title:
    :param content:
    :param api_url:
    :param user:
    :param passwd:
    :param create_only: 仅创建页面，如果页面已存在，就返回error
    :return:
    """

    csrf_token = fetch_csrf_token(session, api_url, user, passwd)
    params_true = {
        "action": "edit",
        "title": title,
        "token": csrf_token,
        "format": "json",
        "text": content,
        "createonly": "true"
    }
    params_false = {
        "action": "edit",
        "title": title,
        "token": csrf_token,
        "format": "json",
        "text": content,
    }
    t = params_true if create_only == "y" else params_false
    response = session.post(api_url, data=t)
    # {'edit': {'new': '', 'result': 'Success', 'pageid': 66, 'title': 'Pythontest', 'contentmodel': 'wikitext',
    # 'oldrevid': 0, 'newrevid': 278, 'newtimestamp': '2023-10-25T08:37:31Z', 'watched': ''}}
    # {'error': {'code': 'articleexists', 'info': 'The article you tried to create has been created already.'......}}
    # print(response.json())
    return response.json()


def delete_page(session, title, api_url, user, passwd):
    """
    删除页面
    :param session:
    :param title: 页面名称
    :param api_url:
    :param user:
    :param passwd:
    :return:
    """
    csrf_token = fetch_csrf_token(session, api_url, user, passwd)
    params = {
        'action': "delete",
        'title': title,
        'token': csrf_token,
        'format': "json",
        'reason': f"deleted by {user}",
        'watchlist': "unwatch"  # 控制文件监视参数
    }
    response = session.post(api_url, data=params)
    # {'delete': {'title': 'Test1', 'reason': 'deleted by Admin2023', 'logid': 358}}
    # print(response.json())
    return response.json()


def upload_file(session, api_url, user, passwd, file_path, target_name):
    csrf_token = fetch_csrf_token(session, api_url, user, passwd)
    params = {
        "action": "upload",
        "filename": target_name,
        "format": "json",
        "token": csrf_token,
        "ignorewarnings": 1
    }

    file = {
        'file': (target_name, open(file_path, 'rb'), 'multipart/form-data')
    }

    response = session.post(api_url, files=file, data=params)
    # print(list(response.json()["upload"]["warnings"].keys())[0])
    return response.json()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python mediawiki_api.py api_url, user, passwd")
        sys.exit()

    s = requests.Session()

    # print(list_all_categories(s, sys.argv[1], sys.argv[2], sys.argv[3]))

    # with open("./data/test.wiki", "rb") as f:
    #     res = create_or_edit_page(s, "pythontest", f.read(), sys.argv[1], sys.argv[2], sys.argv[3])
    #     print(res)

    # res = delete_page(s, "Test2", sys.argv[1], sys.argv[2], sys.argv[3])

    res = upload_file(s, sys.argv[1], sys.argv[2], sys.argv[3], "./data/test3.png", "File_3.png ")
    print(res)
