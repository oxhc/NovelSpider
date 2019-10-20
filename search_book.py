import json
import os

import requests
from bs4 import BeautifulSoup
import urllib.parse

from url_parse import HcUrl


def load_configs(root_path, config_name):
    with open(os.path.join(root_path, 'configs', config_name), 'r', encoding='utf8') as file:
        return json.loads(file.read())


def make_prefix(url, config):
    hc_url = HcUrl(url).parse()
    prefix = hc_url.get('protocol') + '://' + hc_url.get('domain')
    if config == 'relative':
        prefix = url
    elif config == 'without_protocol':
        prefix = hc_url.get('protocol') + ':'
    return prefix


def search(book_name: str):
    configs = load_configs(os.getcwd(), 'search_rules.json')
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-us",
               "Connection": "keep-alive",
               "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
               "Content-Type": "application/x-www-form-urlencoded"
               }
    results = None
    for website_url in configs:
        config = configs[website_url]
        if config['method'] == 'POST':
            config['key'][config['book_name_in_key']] = book_name
            response = requests.post(
                url=config['target_url'],
                headers=headers,
                data=urllib.parse.urlencode(config['key'], encoding='gbk')
            )
            response.encoding = config['encoding']
            bs = BeautifulSoup(response.text, "html5lib")
            authors = bs.select(config['author'])[1:]
            prefix = make_prefix(website_url, config['url_prefix'])
            results = [{
                'href': prefix + i['href'],
                'book_name': i.string,
                'author': j.string
            } for i, j in zip(bs.select(config['book_name']), authors)]
    return results
    # print(configs)
if __name__ == '__main__':
    print(search("仙逆"))