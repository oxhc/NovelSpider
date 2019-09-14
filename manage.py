from url_parse import HcUrl
from mode import common_var
import fire


def main(url, maxworker=10):
    url = HcUrl(url)
    url.parse()
    website_name = url.get('domain').split('.')[1]
    package = __import__('mode.' + website_name)
    mode = getattr(package, website_name)
    method = getattr(mode, 'main')
    method(url.url, maxworker)


if __name__ == '__main__':
    main("https://www.daocaorenshuwu.com/book/zhuixu/")
    # fire.Fire(main)
    # common_var.test()