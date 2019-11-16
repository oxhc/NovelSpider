import json
import os
from urllib.parse import urlparse


def load_mapping(mapping_file_name='url_mapping.json'):
    project_path = os.getcwd()
    file_path = os.path.join(project_path, 'configs', mapping_file_name)
    with open(file_path, 'r') as mapping_file:
        res = mapping_file.read()
    return json.loads(res)


def load_config(link, mapping_path, not_mapping=None):
    if not_mapping is not None:
        with open(not_mapping, 'r', encoding='utf8') as config_file:
            return json.loads(config_file.read())
    domain = urlparse(link).netloc
    with open(mapping_path, 'r', encoding='utf8') as mapping_file:
        mapping = json.loads(mapping_file.read())
    config_dir = os.path.dirname(mapping_path)
    with open(os.path.join(config_dir, mapping['rules_dir'], mapping[domain]+'.json'), 'r', encoding='utf8') as config_file:
        return json.load(config_file)
    #with open(os.path.join(root_path, config_name), 'r', encoding='utf8') as file:
    #    return json.loads(file.read())
    pass

if __name__ == '__main__':
    print(urlparse("https://88dushu.com/xiaoshuo/1/1552/").netloc)