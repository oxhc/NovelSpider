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

count = 0
config = None
project_path = os.path.dirname(os.path.dirname(__file__))
save_path = None


def download_chapter(url):
    bs = get_bs(url)
    title = get_chapter_name(bs)
    body = get_body(bs)
    chapter = convert(url, title, body)
    return chapter


def parse_catalog(bs: BeautifulSoup, prefix='https://www.biquge.com.cn'):
    atags = bs.select(config['chapter_urls'])
    links = [prefix + a['href'] for a in atags if 'class' not in a.attrs]
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


def main(config_name, catalog_url, max_workers=10, undone=False, download=(0, 0)):
    """
    主函数
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
    catalog_bs = get_bs(catalog_url)
    book_name, links = parse_catalog(catalog_bs, hc_url.get('protocol') + '://' + hc_url.get('domain'))
    print('Get catalog page success')

    # 加载未下载成功链接
    if undone is True:
        links = get_undone_urls()

    # 下载数量设置
    if download != (0, 0):
        links = links[download[0]:download[1]]

    # 配置下载路径
    save_path = os.path.join(project_path, 'novel_temp', book_name)
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

    return len(faild_list)


if __name__ == '__main__':
    url = "https://www.biquge.com.cn/book/31833/"
    res = main("biquge", url, max_workers=20, undone=False)
    flag = 0
    left = res
    while res != 0 and flag < 4:
        count = 0
        res = main("biquge", url, max_workers=20, undone=True)
        if left == res:
            flag += 1
        else:
            left = res
    pass
