# coding=gbk
import json
import os
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed

from bs4 import BeautifulSoup
from tqdm import tqdm

from entity.dcr import Chapter
from url_parse import HcUrl

from utils import safe_mkdir, get_bs, save
import files_merge

count = 0
config = None
project_path = os.path.dirname(os.path.dirname(__file__))
save_path = None


def download_chapter(url):
    """
    下载章节
    :param url: 章节url
    :return: 章节对象
    """
    bs = get_bs(url, config['encoding'])
    title = get_chapter_name(bs)
    body = get_body(bs)
    chapter = convert(url, title, body)
    return chapter


def parse_catalog(bs: BeautifulSoup, prefix=''):
    """
    解析目录页信息
    :param bs: 文档树
    :param prefix: 目录前缀
    :return: 书名, 章节链接
    """
    atags = bs.select(config['chapter_urls'])
    links = [prefix + a['href'] for a in atags if 'class' not in a.attrs]
    book_name = bs.select_one(config['book_name']).string
    return book_name, links


def get_chapter_name(bs: BeautifulSoup):
    """
    获取章节名
    :param bs: 文档树
    :return: 章节名
    """
    return bs.select_one(config['chapter_name']).string


def get_body(bs: BeautifulSoup):
    # todo: 还没写分页模式
    cont = bs.select_one(config['body'])
    body = config['inter_lines'].join([i for i in cont.stripped_strings])
    return body


def convert(url, title, body):
    c_id = HcUrl(url).get_end()
    return Chapter(c_id, title, body)


def my_thread(url):
    global count
    try:
        chapter = download_chapter(url)
        save(
            save_path,
            chapter.chapter_id + '_' + chapter.chapter_name,
            '# ' + chapter.chapter_name + '\n\n' + chapter.content
        )
        count += 1
    except Exception:
        return url
    return None


def get_undone_urls():
    with open("failed_urls.txt", 'r') as file:
        links = [link[:-1] for link in file.readlines()]
    while '' in links:
        links.remove('')
    return links


def download(config_name, catalog_url, max_workers=10, undone=False, download=(0, 0)):
    """
    下载函数
    :param undone: 是否下载未下载成功的章节
    :param download: 下载数目
    :param config_name: 配置名称
    :param catalog_url:  目录所在路径
    :param max_workers: 最大线程数量
    :return:  None
    """

    #加载全局变量
    global save_path
    global config

    # 解析配置文件
    with open(os.path.join(project_path, 'configs', config_name + '_config.json'), 'r', encoding='utf8') as config_file:
        config = json.loads(config_file.read())

    #解析url
    hc_url = HcUrl(catalog_url).parse()

    # 加载线程池
    executor = ThreadPoolExecutor(max_workers=max_workers)

    # 获取书名与章节链接
    catalog_bs = get_bs(catalog_url, config['encoding'])

    prefix = hc_url.get('protocol') + '://' + hc_url.get('domain')

    if config['chapter_url_prefix'] == 'relative':
        prefix = catalog_url
    elif config['chapter_url_prefix'] == 'without_protocol':
        prefix = hc_url.get('protocol')+':'

    book_name, links = parse_catalog(catalog_bs, prefix)
    print('Get catalog page success')



    # 加载未下载成功链接
    if undone is True:
        links = get_undone_urls()

    print(links)

    # 下载数量设置
    if download != (0, 0):
        links = links[download[0]:download[1]]

    # 配置下载路径
    save_path = os.path.join(project_path, 'novel_temp', book_name+'-'+hc_url.get('domain'))
    safe_mkdir(save_path)

    #将任务提交至线程池
    all_task = [executor.submit(my_thread, url) for url in links]
    faild_list = []

    pbar = tqdm(total=len(links))
    for future in as_completed(all_task):
        back = future.result()
        if back is not None:
            faild_list.append(back)
        else:
            pbar.update(1)

    executor.shutdown(wait=True)
    pbar.close()
    print("\n此次下载完毕 " + "已下载" + str(count) + "章 共" + str(len(links)) + "章 " + " 失败" + str(len(links) - count) + "章")

    if len(faild_list) != 0:
        with open("failed_urls.txt", 'w') as file:
            for i in faild_list:
                file.write(i + '\n')
    else:
        print('全部下载完毕')

    book_name += '-' + hc_url.get('domain')
    return len(faild_list), book_name


def main(mode_name='', url=''):
    global count
    count = 0
    failed, book_name = download(mode_name, url, max_workers=20, undone=True)
    max_failed = 0
    left = failed
    while failed != 0 and max_failed < 4:
        count = 0
        print("\n 尝试重新下载失败章节")
        failed, book_name = download(mode_name, url, max_workers=20, undone=True)
        if left == failed:
            max_failed += 1
        else:
            left = failed
    files_merge.main(book_name)
    pass
