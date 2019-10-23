import os

import requests
from bs4 import BeautifulSoup
from utils.url_parse import HcUrl
from utils.utils_common import get_bs, safe_name


class Chapter:
    config = None
    order = 0
    name = ""
    url = ""
    title = ""
    body = ""
    downloaded = False
    download_time = 1
    max_try = 3

    def __init__(self, url, config):
        self.url = url
        self.bs: BeautifulSoup = None
        self.config = config

    def get_chapter_title(self):
        name = self.bs.select_one(self.config['chapter_name']).string
        return name if name is not None else 'Unknown_Name'

    def get_body(self):
        # todo: 还没写分页模式
        cont = self.bs.select_one(self.config['body'])
        self.body = self.config['inter_lines'].join([i for i in cont.stripped_strings])
        return self.body

    def download(self):
        if self.download_time >= self.max_try:
            self.body = "本章下载失败"
            return
        try:
            self.download_time += 1
            self.bs = get_bs(self.url, self.config['encoding'])
            self.name = HcUrl(self.url).get_end()
            self.title = self.get_chapter_title() if self.title == "" else self.title
            self.body = self.get_body()
            self.downloaded = True
        except requests.exceptions.ReadTimeout as rt:
            print(f"第 {self.download_time} 次下载 {self.url}")
            self.download()

        print(f"{self.title} 已下载")


    def __str__(self):
        return f"<chapter downloaded={self.downloaded} order={self.order} title={self.title}>"

    def __repr__(self):
        return self.__str__()

    def save(self, path):
        if path is None:
            pass
        with open(os.path.join(path, safe_name(self.name + '_' + self.name + '.txt')), 'w', encoding='utf-8') as file:
            file.write('# ' + self.name + '\n\n' + self.body)
