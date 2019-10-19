from bs4 import BeautifulSoup


from utils import get_bs
from url_parse import HcUrl

class Catalog:
    url: str = None
    bs: BeautifulSoup = None
    config = None

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
        links = [self.prefix + a['href'] for a in atags if 'class' not in a.attrs]
        book_name = self.bs.select_one(self.config['book_name']).string
        return book_name, links