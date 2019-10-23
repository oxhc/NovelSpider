import json
import os

import requests

from components.Chapter import Chapter
from components.Catalog import Catalog
from utils.thread_downloader import Downloader


class Book:
    book_name = ""
    catalog = None
    chapters = []
    config = None
    failed_chapters = []
    information = {}
    max_workers = 15
    downloader = None
    url = ""

    def __init__(self, url, config):
        self.catalog = Catalog(url, config)
        self.config = config
        pass

    def load_catalog(self):
        self.information, links = self.catalog.parse_catalog()
        for link, order in zip(links, range(len(links))):
            chapter = Chapter(
                url=link[0],
                config=self.config
            )
            chapter.title = link[1]
            chapter.order = order
            self.chapters.append(chapter)
        return self.chapters

    def __getitem__(self, item) -> Chapter:
        self.chapters[item - 1].download()
        return self.chapters[item - 1]

    def download(self, start=0, end=0):
        self.downloader = Downloader()
        end = len(self.chapters) if end == 0 else end
        for chapter in self.chapters[start:end]:
            self.downloader.push(chapter.download)

    def save(self, path, file_name):
        pass

    def save(self):
        pass


def load_configs(root_path, config_name):
    with open(os.path.join(root_path, 'configs', config_name), 'r', encoding='utf8') as file:
        return json.loads(file.read())


if __name__ == '__main__':
    # print(os.path.dirname(os.getcwd()))
    config = load_configs(os.path.dirname(os.getcwd()), "88dush_config.json")
    # print(config)
    book = Book("https://www.88dush.com/xiaoshuo/131/131009/", config)
    book.load_catalog()
    print(book.information)
    book.download()
    book.downloader.wait()
    print(book.chapters)
    #
