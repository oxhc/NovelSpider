# coding=gbk
import json
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed

from bs4 import BeautifulSoup
from entity.dcr import Chapter
from mode import common_var
from url_parse import HcUrl

from utils import safe_mkdir, get_bs, save

count = 0
config = None


def download_chapter(url):
    bs = get_bs(url)
    title = get_chapter_name(bs)
    body = get_body(bs)
    chapter = convert(url, title, body)
    return chapter


def parse_catalog(bs: BeautifulSoup):
    atags = bs.select(config['chapter_urls'])
    links = [config['chapter_url_prefix'] + a['href'] for a in atags if 'class' not in a.attrs]
    book_name = bs.select_one(config['book_name']).string
    return book_name, links


def get_chapter_name(bs: BeautifulSoup):
    return bs.select_one(config['chapter_name']).string


def get_body(bs: BeautifulSoup):
    cont = bs.select_one(config['body'])
    body = config['inter_lines'].join([i for i in cont.stripped_strings])
    return body


def convert(url, title, body):
    c_id = HcUrl(url).get_end()
    return Chapter(c_id, title, body)


def my_thread(url):
    global count
    chapter = download_chapter(url)
    save(common_var.temp_dir, chapter.chapter_id + '_' + chapter.chapter_name, '# ' + chapter.chapter_name + '\n\n' + chapter.content)
    count += 1
    return chapter


def main(config_name, catalog_url, max_workers=10):
    """
    主函数
    :param config_name: 配置名称
    :param catalog_url:  目录所在路径
    :param max_workers: 最大线程数量
    :return:  None
    """

    # 解析配置文件
    global config
    with open(config_name + '_config.json', 'r') as config_file:
        config = json.loads(config_file.read())

    executor = ThreadPoolExecutor(max_workers=max_workers)
    catalog_bs = get_bs(catalog_url)
    book_name, links = parse_catalog(catalog_bs)
    print(links)

    # 下载数量
    download_count = 0
    if download_count != 0:
        links = links[:download_count]

    safe_mkdir(common_var.temp_dir + book_name)
    common_var.temp_dir = common_var.temp_dir + book_name

    all_task = [executor.submit(my_thread, url) for url in links]

    for future in as_completed(all_task):
        future.result()
        print("已下载"+str(count)+"章 共"+str(len(links))+"章")

    print("下载完毕")


if __name__ == '__main__':
    main("biquge", "https://www.biquge.com.cn/book/30158/")
    pass
