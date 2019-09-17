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
    �����½�
    :param url: �½�url
    :return: �½ڶ���
    """
    bs = get_bs(url, config['encoding'])
    title = get_chapter_name(bs)
    body = get_body(bs)
    chapter = convert(url, title, body)
    return chapter


def parse_catalog(bs: BeautifulSoup, prefix=''):
    """
    ����Ŀ¼ҳ��Ϣ
    :param bs: �ĵ���
    :param prefix: Ŀ¼ǰ׺
    :return: ����, �½�����
    """
    atags = bs.select(config['chapter_urls'])
    links = [prefix + a['href'] for a in atags if 'class' not in a.attrs]
    book_name = bs.select_one(config['book_name']).string
    return book_name, links


def get_chapter_name(bs: BeautifulSoup):
    """
    ��ȡ�½���
    :param bs: �ĵ���
    :return: �½���
    """
    return bs.select_one(config['chapter_name']).string


def get_body(bs: BeautifulSoup):
    # todo: ��ûд��ҳģʽ
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
    ���غ���
    :param undone: �Ƿ�����δ���سɹ����½�
    :param download: ������Ŀ
    :param config_name: ��������
    :param catalog_url:  Ŀ¼����·��
    :param max_workers: ����߳�����
    :return:  None
    """

    #����ȫ�ֱ���
    global save_path
    global config

    # ���������ļ�
    with open(os.path.join(project_path, 'configs', config_name + '_config.json'), 'r', encoding='utf8') as config_file:
        config = json.loads(config_file.read())

    #����url
    hc_url = HcUrl(catalog_url).parse()

    # �����̳߳�
    executor = ThreadPoolExecutor(max_workers=max_workers)

    # ��ȡ�������½�����
    catalog_bs = get_bs(catalog_url, config['encoding'])

    prefix = hc_url.get('protocol') + '://' + hc_url.get('domain')

    if config['chapter_url_prefix'] == 'relative':
        prefix = catalog_url
    elif config['chapter_url_prefix'] == 'without_protocol':
        prefix = hc_url.get('protocol')+':'

    book_name, links = parse_catalog(catalog_bs, prefix)
    print('Get catalog page success')



    # ����δ���سɹ�����
    if undone is True:
        links = get_undone_urls()

    print(links)

    # ������������
    if download != (0, 0):
        links = links[download[0]:download[1]]

    # ��������·��
    save_path = os.path.join(project_path, 'novel_temp', book_name+'-'+hc_url.get('domain'))
    safe_mkdir(save_path)

    #�������ύ���̳߳�
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
    print("\n�˴�������� " + "������" + str(count) + "�� ��" + str(len(links)) + "�� " + " ʧ��" + str(len(links) - count) + "��")

    if len(faild_list) != 0:
        with open("failed_urls.txt", 'w') as file:
            for i in faild_list:
                file.write(i + '\n')
    else:
        print('ȫ���������')

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
        print("\n ������������ʧ���½�")
        failed, book_name = download(mode_name, url, max_workers=20, undone=True)
        if left == failed:
            max_failed += 1
        else:
            left = failed
    files_merge.main(book_name)
    pass
