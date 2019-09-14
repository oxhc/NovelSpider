# coding=gbk
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed

from bs4 import BeautifulSoup
import re
from entity.dcr import Chapter
import queue

from utils import safe_mkdir, get_bs

url_queue = queue.Queue()
result_queue = queue.Queue()
temp_novel = 'novel_temp/'
catalog_url = "https://www.daocaorenshuwu.com/book/shishangzuiqiangzhuixu/"
count = 0
isConfused = True


def download_chapter(url):
    bs = get_bs(url)
    title = get_title(bs)
    body = body_detect(bs)
    chapter = convert(url, title, body)
    other_pages = bs.select_one("div.page")
    other_urls = [i['href'] for i in other_pages.select("ul > li > a") if 'href' in i.attrs]
    for url in other_urls:
        other_bs = get_bs(catalog_url + url)
        chapter.content += body_detect(other_bs)
        print("第二节")
    return chapter


def save(dir, name, text):
    with open(dir + '/' + name + '.txt', 'w+', encoding='utf8') as file:
        file.write(text)


def get_chapters_url(bs: BeautifulSoup):
    atags = bs.select("div#all-chapter  a")
    ahrefs = ['https:' + a['href'] for a in atags if 'class' not in a.attrs]
    return ahrefs


def get_title(bs: BeautifulSoup):
    return bs.select_one("h1.cont-title").string


def body_detect(bs: BeautifulSoup):
    global isConfused
    cont = bs.select_one("div#cont-text")
    cont.select_one("script").clear()
    if isConfused:
        try:
            zd = cont.select_one("style").string
            cont.select_one("style").clear()
            span = cont.select(zd[1:8])
            for i in span:
                i.clear()
        except Exception:
            print(get_title(bs) + '############### wrong')
            isConfused = False
            pass
    body = '\n'.join([i for i in cont.stripped_strings][:-2])
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
    save(temp_novel, obj.chapter_id + '_' + obj.chapter_name, '# ' + obj.chapter_name + '\n\n' + obj.content)
    count += 1
    print('已下载 ' + str(count) + ' 章')
    return obj


def main():
    global temp_novel
    global catalog_url
    download_count = 15
    executor = ThreadPoolExecutor(max_workers=10)
    c_bs = get_bs(catalog_url)
    links = get_chapters_url(c_bs)
    if download_count != 0:
        links = links[:download_count]
    cuts = catalog_url.split('/')
    book_name = cuts[len(cuts) - 2]
    safe_mkdir(temp_novel + book_name)
    temp_novel = temp_novel + book_name
    url_queue.queue = queue.deque(links)

    all_task = [executor.submit(my_thread, (url)) for url in links]

    for future in as_completed(all_task):
        future.result()

    print("下载完毕")


if __name__ == '__main__':
    main()
    pass
