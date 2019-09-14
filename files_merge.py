# coding=utf8
from functools import cmp_to_key
import queue
import os

file_path = 'novel/'
files_queue = queue.Queue()
ready_write = []


def filename_cmp(x: str, y: str):
    x_num = int(x.split('_')[0])
    y_num = int(y.split('_')[0])
    return x_num - y_num


def main():
    fies = os.listdir(file_path)
    fies.sort(key=cmp_to_key(filename_cmp))
    with open("novel.txt", "a", encoding='utf8') as novel:
        for f in fies:
            with open(file_path + f, 'r', encoding='utf8') as temp:
                novel.write(temp.read() + '\n')
    pass


if __name__ == '__main__':
    main()
    pass
