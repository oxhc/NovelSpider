from PyQt5.QtCore import QThread


class ThreadProxy(QThread):

    def __init__(self, func=None, args=None):
        super().__init__()
        self.func = func
        self.args = args

    def run(self):
        if self.func is not None:
            self.func()



