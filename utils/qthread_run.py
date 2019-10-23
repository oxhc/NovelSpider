from PyQt5.QtCore import QThread


class ThreadProxy(QThread):

    def __init__(self, func=None, args=None, signal=None):
        super().__init__()
        self.func = func
        self.args = args
        self.signal = signal

    def run(self):
        if self.func is not None:
            if self.args is not None:
                res = self.func(self.args)
            else:
                res = self.func()
            if self.signal is not None:
                print(res)
                self.signal.emit(res)




