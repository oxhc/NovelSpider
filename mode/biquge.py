# coding=gbk
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed

from bs4 import BeautifulSoup
import re
from entity.dcr import Chapter

from utils import safe_mkdir, get_bs, save
from . import common_var

catalog_url = ""
count = 0


def download_chapter(url):
    bs = get_bs(url)
    title = get_title(bs)
    body = body_detect(bs)
    chapter = convert(url, title, body)
    return chapter


def get_chapters_url(bs: BeautifulSoup):
    atags = bs.select("#list > dl > dd > a")
    ahrefs = ['https://www.biquge.com.cn' + a['href'] for a in atags if 'class' not in a.attrs]
    return ahrefs


def get_title(bs: BeautifulSoup):
    return bs.select_one("#wrapper > div.content_read > div > div.bookname > h1").string


def body_detect(bs: BeautifulSoup):
    global isConfused
    cont = bs.select_one("#content")
    body = '\n      '.join([i for i in cont.stripped_strings][:-2])
    body = re.sub("\n\n+", '', body)
    return body


def convert(url, title, body):
    match = re.match(".+\/(.+)\.html", url)
    if match and match.group(1):
        c_id = match.group(1)
    return Chapter(c_id, title, body)


def my_thread(url):
    global count
    obj = download_chapter(url)
    save(common_var.temp_dir, obj.chapter_id + '_' + obj.chapter_name, '# ' + obj.chapter_name + '\n\n' + obj.content)
    count += 1
    print('已下载 ' + str(count) + ' 章')
    return obj


def main(cl, max_workers=10):
    """
    主函数
    :param cl:  catalog_url
    :param max_workers: 最大线程数量
    :return:  None
    """
    global catalog_url

    catalog_url = cl
    download_count = 0
    executor = ThreadPoolExecutor(max_workers=max_workers)
    c_bs = get_bs(catalog_url)
    links = get_chapters_url(c_bs)
    if download_count != 0:
        links = links[:download_count]
    cuts = catalog_url.split('/')
    book_name = cuts[len(cuts) - 2]
    safe_mkdir(common_var.temp_dir + book_name)
    common_var.temp_dir = common_var.temp_dir + book_name

    all_task = [executor.submit(my_thread, (url)) for url in links]

    for future in as_completed(all_task):
        future.result()

    print("下载完毕")


if __name__ == '__main__':
    main("https://www.daocaorenshuwu.com/book/zhuixu/")
    pass
