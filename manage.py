# coding=utf-8
import json
import os

from tqdm import tqdm

from components.NoverDownloader import NoverDownloader
from url_parse import HcUrl
import fire

from utils.utils_common import load_config

project_path = os.getcwd()


def set_total(progress, num):
    progress.total = num


def update(progress, num):
    progress.update(num)


def main(mode_name='', url='', max_workers=20):
    work_path = os.getcwd()
    config = load_config(work_path, mode_name + '_config.json')
    progress_display = tqdm()    # progress_display 需要实现total成员与update方法
    nd = NoverDownloader(
        url,
        config, work_path=work_path,
        set_total=lambda x: set_total(progress_display, x),
        update=lambda x: update(progress_display, x),
        max_worker=max_workers
    )
    if nd.start():
        progress_display.close()
        nd.make_book()
        print("全部下载完毕")
    else:
        progress_display.close()


def load_mapping(mapping_file_name='url_mapping.json'):
    file_path = os.path.join(project_path, 'configs', mapping_file_name)
    res = None
    with open(file_path, 'r') as mapping_file:
        res = mapping_file.read()
    return json.loads(res)


def get_info(url, max_workers=20):
    mapping = load_mapping()
    work_path = os.getcwd()
    mode_name = mapping[HcUrl(url).parse().get('domain')]
    config = load_config(work_path, mode_name + '_config.json')
    nd = NoverDownloader(
        url,
        config, work_path=work_path,
        max_worker=max_workers
    )
    print(nd.catalog_url)
    print(nd.book_name)
    print(nd.book_info['author'])
    print(nd.book_info['status'])
    print(nd.book_info['update_date'])
    print(mode_name)



def download(url, maxworker=20):
    mapping = load_mapping()
    main(mapping[HcUrl(url).parse().get('domain')], url, max_workers=maxworker)


if __name__ == '__main__':
    fire.Fire()
