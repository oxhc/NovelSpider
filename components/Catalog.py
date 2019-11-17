from utils.utils_common import get_bs
from utils.url_parse import HcUrl


class Catalog:
    def __init__(self, url, config):
        self.url = url
        self.bs = get_bs(url, config['encoding'])
        self.config = config
        self.prefix = ''

    def set_prefix(self):
        hc_url = HcUrl(self.url).parse()
        self.prefix = hc_url.get('protocol') + '://' + hc_url.get('domain')
        if self.config['chapter_url_prefix'] == 'relative':
            self.prefix = self.url
        elif self.config['chapter_url_prefix'] == 'without_protocol':
            self.prefix = hc_url.get('protocol') + ':'

    def parse_catalog(self):
        """
        解析目录页信息
        :param bs: 文档树
        :param prefix: 目录前缀
        :return: 书名, 章节链接
        """
        self.set_prefix()
        atags = self.bs.select(self.config['chapter_urls'])
        links = [[self.prefix + a['href'], a.string] for a in atags]
        book_name = self.bs.select_one(self.config['book_name']).string
        author = self.bs.select_one(self.config['author']).string
        status = self.bs.select_one(self.config['status']).string
        update_date = self.bs.select_one(self.config['update_date']).string
        res = {
                   'book_name':book_name,
                   'author':author,
                   'status':status,
                   'update_date':update_date
               }
        for key in res:
            if self.config['info_separator'] in res[key]:
                res[key] = res[key].split(self.config['info_separator'])[1]
        return res,links
