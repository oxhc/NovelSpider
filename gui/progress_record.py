from PyQt5 import QtCore


class DownloadProgress(QtCore.QObject):
    progress_signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.step = 0
        self.total = 100
        self.per = 0

    def setTotal(self, num):
        self.total = num

    def update(self, num):
        self.step += num
        if self.per == int((self.step / self.total) * 100):
            return
        self.per = int((self.step / self.total) * 100)
        if self.per <= 100:
            self.progress_signal.emit(self.per)


    def close(self):
        self.step = 0
        self.total = 100
        self.per = 0
        self.progress_signal.emit(self.per)