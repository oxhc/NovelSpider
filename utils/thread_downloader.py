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

    def terminate(self):
        for task in self.tasks:
            task.cancel()

    def wait(self):
        self.executor.shutdown(wait=True)

