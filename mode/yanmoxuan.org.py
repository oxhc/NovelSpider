# coding=gbk
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed

from bs4 import BeautifulSoup
import re
from entity.ymx import YmxNovel
import queue

from utils import get_bs

start_url = "https://www.yanmoxuan.org/txt181_89985.html"

url_queue = queue.Queue()
result_queue = queue.Queue()
count = 0


def download_chapter(url):
    bs = get_bs(url)
    next_u = next_url(bs)
    title = get_title(bs)
    body = body_detect(bs)
    chapter = convert(url, title, body)
    while next_u is not None:
        next_bs = get_bs(next_u)
        next_u = next_url(next_bs)
        body = body_detect(next_bs)
        chapter.content = chapter.content + '\n' + body

    return chapter


def save(text):
    with open('novel.txt', 'a', encoding='utf8') as file:
        file.write(text)


def get_chapters_url(bs: BeautifulSoup):
    atags = bs.select("div.booklist2 > ul > li > a")
    ahrefs = [a['href'] for a in atags if 'class' not in a.attrs]
    return ahrefs


def get_title(bs: BeautifulSoup):
    return bs.title.string.split("_")[0]


def body_detect(bs: BeautifulSoup):
    cont = bs.select_one("div.cont")
    cont.select_one("div.chapter_turnpage").clear()
    cont.select_one("div.nfx").clear()
    body = '\n'.join([i for i in cont.stripped_strings][:-2])
    body = re.sub("---.+", '', body)
    body = re.sub("衍.+轩", '', body)
    body = re.sub("\n\n+", '', body)
    return body


def convert(url, title, body):
    match = re.match(".+/www\\.yanmoxuan\\.org/(.+)\\.html", url)
    if match and match.group(1):
        args = match.group(1).split("_")
        if len(args) == 2:
            args.append('1')
    return YmxNovel(args[0], args[1], title, body)


def next_url(bs: BeautifulSoup):
    links = bs.select("div.chapter_turnpage a")
    href: str = links[2]['href']
    result = re.match(".+\/", start_url).group() + href[1:]
    return result if links[2].string == '下一页' else None


def my_thread(url):
    global count
    obj = download_chapter(url)
    count += 1
    print('已下载 ' + str(count) + ' 章')
    return obj


def main():
    catalog_url = "https://www.yanmoxuan.org/txt181/"
    executor = ThreadPoolExecutor(max_workers=10)
    links = get_chapters_url(get_bs(catalog_url))
    # links = links[:10]
    # url_queue.queue = queue.deque(links)

    all_task = [executor.submit(my_thread, (url)) for url in links]

    for future in as_completed(all_task):
        data = future.result()
        result_queue.put(data)

    print("下载完毕")


if __name__ == '__main__':
    main()
    pass
