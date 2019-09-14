import re


class HcUrl:
    def __init__(self, url: str):
        self.url = url
        self.parts = {}

    def get_end(self):
        pass

    def get(self, key: str):
        return self.parts[key]

    def parse(self):
        re_patern = "(http.?):\/\/"
        m = re.match(re_patern, self.url)
        protocol = 'https'
        if m and m.group(1):
            protocol = m.group(1)
        self.parts['protocol'] = protocol
        se_url = re.sub("(http.?):\/\/", '', self.url)
        self.parts['domain'] = se_url.split('/')[0]


if __name__ == '__main__':
    url = HcUrl("www.daocaorenshuwu.com/book/zhuixu/")
    # print(url.get_first())
    url.parse()
    print(url.get('protocol'))
    print(url.get('domain'))
