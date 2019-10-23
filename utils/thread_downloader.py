import random
import time
from concurrent.futures.thread import ThreadPoolExecutor


class Downloader:
    url = ""
    executor = None
    tasks = []
    max_workers = 15

    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=self.max_workers)

    def push(self, func):
        task = self.executor.submit(func)
        self.tasks.append(task)

    def wait(self):
        self.executor.shutdown(wait=True)


def hello(x):
    print(f"start {x}")
    time.sleep(random.randint(0, 20))
    print(f"finish {x}")



if __name__ == '__main__':
    downloader = Downloader()
    for i in range(30):
        downloader.push(lambda: hello(i))
    print("hh")
    downloader.executor.shutdown(wait=True)