import re
from urllib.parse import urlparse


class HcUrl:
    url = ""
    protocol = ""
    domain = ""
    last_part = ""

    def __init__(self, url: str):
        self.url = url
        self.__parts = {}

    def get_end(self):
        t_url = re.sub("\/$|.html?", '', self.url)
        result = t_url.split('/')
        return result[len(result)-1]

    def get(self, key: str):
        return self.__parts[key]

    def parse(self):
        re_patern = "(http.?):\/\/"
        m = re.match(re_patern, self.url)
        protocol = 'https'
        if m and m.group(1):
            protocol = m.group(1)
        self.__parts['protocol'] = protocol
        se_url = re.sub("(http.?):\/\/", '', self.url)
        self.__parts['domain'] = se_url.split('/')[0]
        return self


if __name__ == '__main__':
    url = urlparse("https://www.biquge.com.cn/book/31833.html")
    print(url)
