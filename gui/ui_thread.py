import json
import os

from PyQt5.QtCore import QThread

from gui.progress_record import DownloadProgress
from url_parse import HcUrl
from utils import load_config


def total(progress: DownloadProgress, num):
    progress.setTotal(num)


def update(progress, num):
    progress.update(num)


def load_mapping(mapping_file_name='url_mapping.json'):
    file_path = os.path.join(os.getcwd(), 'configs', mapping_file_name)
    res = None
    with open(file_path, 'r') as mapping_file:
        res = mapping_file.read()
    return json.loads(res)


class DownloadThread(QThread):

    def __init__(self, url="", progress_obj=None):
        super().__init__()
        self.url = url
        self.progress_obj = progress_obj

    def run(self):
        print('start downloading')
        url = self.url
        mapping = load_mapping()
        work_path = os.getcwd()
        config = load_config(work_path, mapping[HcUrl(url).parse().get('domain')] + '_config.json')
        from NoverDownloader import NoverDownloader
        nd = NoverDownloader(
            url,
            config, work_path=work_path,
            set_total=lambda x: total(self.progress_obj, x),
            update=lambda x: update(self.progress_obj, x),
            max_worker=20
        )
        self.progress_obj.close()
        if nd.start():
            nd.make_book()
            print("全部下载完毕")
        else:
            nd.make_book()
            print("失败章节:")
            for i in nd.faild_list:
                print(i)
