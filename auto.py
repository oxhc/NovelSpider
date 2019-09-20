# coding=utf-8
import os
from tqdm import tqdm

from NoverDownloader import NoverDownloader
from utils import load_config


def total(ji, num):
    ji.total = num


def update(ji, num):
    ji.update(num)


def main(mode_name='', url='', max_workers=20):
    work_path = os.getcwd()
    config = load_config(work_path, mode_name+'_config.json')
    ji = tqdm()
    nd = NoverDownloader(
        url,
        config, work_path=work_path,
        set_total=lambda x: total(ji, x),
        update=lambda x: update(ji, x),
        max_worker=max_workers
    )

    if nd.start():
        ji.close()
        nd.make_book()
        print("全部下载完毕")
    else:
        ji.close()

