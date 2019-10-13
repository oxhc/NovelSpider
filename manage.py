# coding=utf-8
import json
import os

import auto
from url_parse import HcUrl
import fire

project_path = os.getcwd()


def load_mapping(mapping_file_name='url_mapping.json'):
    file_path = os.path.join(project_path, 'configs', mapping_file_name)
    res = None
    with open(file_path, 'r') as mapping_file:
        res = mapping_file.read()
    return json.loads(res)


def download(url, maxworker=20):
    mapping = load_mapping()
    auto.main(mapping[HcUrl(url).parse().get('domain')], url, max_workers=maxworker)

if __name__ == '__main__':
    fire.Fire()