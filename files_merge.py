# coding=utf8
from functools import cmp_to_key
import os

from utils.utils_common import safe_mkdir

project_path = os.getcwd()


def filename_cmp(x: str, y: str):
    x_num = int(x.split('_')[0])
    y_num = int(y.split('_')[0])
    return x_num - y_num


def main(path, book_name):
    save_path = os.path.join(path, '..', '..', 'novel')
    safe_mkdir(save_path)
    file_path = path
    fies = os.listdir(file_path)
    fies.sort(key=cmp_to_key(filename_cmp))
    with open(os.path.join(save_path, book_name+'.txt'), "a", encoding='utf8') as novel:
        for f in fies:
            with open(os.path.join(file_path, f), 'r', encoding='utf8') as temp:
                novel.write(temp.read() + '\n')
    pass


if __name__ == '__main__':
    main("赘婿-www.88dush.com")
    pass
