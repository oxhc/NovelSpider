# coding=utf-8
import os

from tqdm import tqdm

from components.Book import Book
from utils.config_utils import load_mapping, load_config
from utils.url_parse import HcUrl
import fire

project_path = os.getcwd()


def set_total(progress, num):
    progress.total = num


def update(progress, num):
    progress.update(num)


def main(url='', max_workers=10):
    work_path = os.getcwd()
    config = load_config(url, os.path.join(work_path, 'configs', 'url_mapping.json'))
    mode_name = config['mode_name']
    progress_display = tqdm()  # progress_display 需要实现total成员与update方法
    book = Book(
        url,
        config,
        set_total=lambda x: set_total(progress_display, x),
        update=lambda x: update(progress_display, x),
    )
    book.load_catalog()
    res = False
    try:
        res = book.download()
    except KeyboardInterrupt:
        book.terminate()
    if res:
        progress_display.close()
        # nd.make_book()
        print("全部下载完毕")
    else:
        progress_display.close()
    book.save(os.path.join(os.getcwd(), 'novels'), book.information['book_name'] + '-' + mode_name + '.txt')


def get_info(url, max_workers=10):
    work_path = os.getcwd()
    config = load_config(url, os.path.join(work_path, 'configs', 'url_mapping.json'))
    book = Book(
        url,
        config
    )
    book.load_catalog()
    print(book.information)


def download(url, maxworker=10):
    main(url, max_workers=maxworker)


if __name__ == '__main__':
    # fire.Fire()
    download("https://www.88dushu.com/xiaoshuo/1/1552/")