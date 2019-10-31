import json
import os
from concurrent.futures import as_completed
from components.Chapter import Chapter
from components.Catalog import Catalog
from utils.thread_downloader import Downloader
from utils.utils_common import safe_mkdir, load_config


class Book:
    book_name = ""
    catalog = None
    chapters = []
    config = None
    failed_chapters = []
    information = {}
    max_workers = 15
    downloader = None
    set_total = None
    update = None
    url = ""

    def __init__(self, url, config, set_total=None, update=None):
        self.catalog = Catalog(url, config)
        self.config = config
        self.set_total = set_total
        self.update = update
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
        if self.set_total is not None:
            self.set_total(len(self.chapters))
        for chapter in self.chapters[start:end]:
            self.downloader.push(chapter.download)
        for future in as_completed(self.downloader.tasks):
            if self.update is not None:
                self.update(1)
        self.downloader.wait()
        return True

    def save(self, path, file_name):
        safe_mkdir(path)
        with open(os.path.join(path, file_name), 'w', encoding='utf8') as novel:
            for chapter in self.chapters:
                ready_to_write = '# '+ chapter.title +'\n\n' + chapter.body
                novel.write(ready_to_write+ '\n')

if __name__ == '__main__':
    # print(os.path.dirname(os.getcwd()))
    config = load_config(os.path.dirname(os.getcwd()), "88dush_config.json")
    # print(config)
    book = Book("https://www.88dush.com/xiaoshuo/131/131009/", config)
    book.load_catalog()
    print(book.information)
    book.download(0, 20)
    print(book.chapters)
    book.save(os.getcwd(), "xxx.txt")
    #
