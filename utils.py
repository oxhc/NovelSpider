import os

import requests
from bs4 import BeautifulSoup


def real_path(relative_path):
    pass


def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    pass


def get_bs(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-us",
               "Connection": "keep-alive",
               "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf8'
    return BeautifulSoup(response.text, "html5lib")