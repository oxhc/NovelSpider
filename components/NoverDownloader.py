import os
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import files_merge
from components import Book
from components.Catalog import Catalog
from components.Chapter import Chapter
from utils.utils_common import safe_mkdir
from utils import url_parse


class NoverDownloader:
    def __init__(self, url, config, max_worker=10, work_path=None, set_total=None, update=None):
        self.book = Book(url, config, set_total=set_total, update=update)
        self.book.load_catalog()
        return
        self.downloaded_count = 0
        self.total_count = 0
        self.catalog = None
        self.save_path = ''
        self.termination = False
        self.book_name = ''
        self.faild_list = []
        self.config = config
        self.catalog_url = url
        self.max_worker = max_worker
        self.domain = url_parse.HcUrl(url).parse().get('domain')
        self.set_total = set_total
        self.update = update
        self.try_times = 0
        self.faild_count = 0
        self.catalog = Catalog(self.catalog_url, config=self.config)
        self.book_info, self.catas = self.catalog.parse_catalog()
        self.links = [i[0] for i in self.catas]
        self.links_name = [i[1] for i in self.catas]
        for key in self.book_info:
            if self.config['info_separator'] in self.book_info[key]:
                self.book_info[key] = self.book_info[key].split(self.config['info_separator'])[1]
        self.book_name = self.book_info['book_name']
        self.total_count = len(self.links)

        if work_path is not None:
            self.work_path = work_path
        else:
            self.work_path = os.getcwd()

    def get_undone_urls(self):
        return self.faild_list

    def download_thread(self, url):
        if self.termination:
            return None
        try:
            chapter = Chapter(url, self.config)
            chapter.download()
            chapter.save(self.work_path)
            self.downloaded_count += 1
            if self.update is not None:
                self.update(1)
        except Exception:
            return url
        return None

    def make_book(self):
        return
        files_merge.main(self.work_path, self.book_name+'-'+self.domain)

    def start(self, undone=False):
        return self.book.download()
        if self.try_times > 3:
            return False
        # 获取目录页
        if not undone:
            if self.set_total is not None:
                self.set_total(self.total_count)
            self.work_path = os.path.join(self.work_path, 'novel_temp', self.book_name + '-' + self.domain)
            safe_mkdir(self.work_path)
        else:
            self.links = self.get_undone_urls()

        print('Get catalog success')

        executor = ThreadPoolExecutor(max_workers=self.max_worker)

        # 将任务提交至线程池
        all_task = [executor.submit(self.download_thread, url) for url in self.links]
        self.faild_list = []

        for future in as_completed(all_task):
            back = future.result()
            if back is not None:
                self.faild_list.append(back)

        executor.shutdown(wait=True)
        # print("\n此次下载完毕 " + "已下载" + str(count) + "章 共" + str(len(links)) + "章 " + " 失败" + str(len(links) - count) + "章")

        if len(self.faild_list) == self.faild_count:
            self.try_times += 1
        else:
            self.faild_count = len(self.faild_list)

        if len(self.faild_list) != 0:
            print("\nAttempt to download faild chapters")
            for i in self.faild_list:
                print(i)
            return self.start(undone=True)
        else:
            return True