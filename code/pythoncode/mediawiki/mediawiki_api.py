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


def create_or_edit_page(session, title, content, api_url, user, passwd):
    """
    创建和编辑页面
    :param session:
    :param title:
    :param content:
    :param api_url:
    :param user:
    :param passwd:
    :return:
    """

    csrf_token = fetch_csrf_token(session, api_url, user, passwd)
    params = {
        "action": "edit",
        "title": title,
        "token": csrf_token,
        "format": "json",
        "appendtext": content
    }
    response = session.post(api_url, data=params)
    # {'edit': {'new': '', 'result': 'Success', 'pageid': 66, 'title': 'Pythontest', 'contentmodel': 'wikitext',
    # 'oldrevid': 0, 'newrevid': 278, 'newtimestamp': '2023-10-25T08:37:31Z', 'watched': ''}}
    # print(response.json())
    return response.json()['edit']['result']


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python mediawiki_api.py api_url, user, passwd")
        sys.exit()

    s = requests.Session()

    # print(list_all_categories(s, sys.argv[1], sys.argv[2], sys.argv[3]))

    with open("./data/test.wiki", "rb") as f:
        res = create_or_edit_page(s, "pythontest", f.read(), sys.argv[1], sys.argv[2], sys.argv[3])
        print(res)
