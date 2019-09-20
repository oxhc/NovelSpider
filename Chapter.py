import os

from bs4 import BeautifulSoup
from url_parse import HcUrl
from utils import get_bs


class Chapter:
    def __init__(self, url, config):
        self.url = url
        self.bs: BeautifulSoup = None
        self.config = config
        self.id = 0
        self.name = ''
        self.body = ''

    def get_chapter_name(self):
        name = self.bs.select_one(self.config['chapter_name']).string
        return name if name is not None else 'Unknown_Name'

    def get_body(self):
        # todo: 还没写分页模式
        cont = self.bs.select_one(self.config['body'])
        body = self.config['inter_lines'].join([i for i in cont.stripped_strings])
        return body

    def download(self):
        self.bs = get_bs(self.url, self.config['encoding'])
        self.id = HcUrl(self.url).get_end()
        self.name = self.get_chapter_name()
        self.body = self.get_body()

    def save(self, path):
        if path is None:
            pass
        # print(os.path.join(path, self.id + '_' + self.name))
        with open(os.path.join(path, self.id + '_' + self.name + '.txt'), 'w', encoding='utf-8') as file:
            file.write('# ' + self.name + '\n\n' + self.body)