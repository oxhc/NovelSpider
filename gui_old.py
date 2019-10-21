#!/usr/bin/python
import os
import re
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QProgressBar)

from gui.progress_record import DownloadProgress
from gui.ui_thread import DownloadThread


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class Main_Window(QWidget):
    download_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.catalog = QLabel('目录页链接')
        self.mode = QLabel('模式')
        self.review = QLabel('输出')
        self.prog = QLabel('进度')

        self.catalog_edit = QLineEdit()
        self.modeEdit = QLineEdit()
        self.reviewEdit = QTextEdit()
        self.reviewEdit.setReadOnly(True)
        self.reviewEdit.setObjectName("reviewEdit")
        self.pregress_bar = QProgressBar(self)
        self.download_button = QPushButton("下载")
        self.bu2 = QPushButton("暂停")
        self.modeEdit.setText("自动选择")
        self.initUI()
        self.project_path = os.getcwd()
        self.old = sys.stdout
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)
        self.thread = None
        self.progress_obj = None
        self.set_bound()

    def outputWritten(self, text):
        cursor = self.reviewEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.reviewEdit.setTextCursor(cursor)
        self.reviewEdit.ensureCursorVisible()

    def download(self, maxworker=10):
        self.thread = DownloadThread(self.catalog_edit.text(), self.progress_obj)
        self.thread.start()

    def outputWritten(self, text):
        cursor = self.reviewEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.reviewEdit.setTextCursor(cursor)
        self.reviewEdit.ensureCursorVisible()

    def click(self, checked):
        self.download_signal.emit()

    def set_bound(self):
        self.progress_obj = DownloadProgress()
        self.progress_obj.progress_signal.connect(self.pregress_bar.setValue)
        self.download_button.clicked.connect(self.download)
        pass

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(18)

        grid.addWidget(self.catalog, 1, 0)
        grid.addWidget(self.catalog_edit, 1, 1)
        grid.addWidget(self.download_button, 1, 2)

        grid.addWidget(self.mode, 2, 0)
        grid.addWidget(self.modeEdit, 2, 1)
        grid.addWidget(self.bu2, 2, 2)

        grid.addWidget(self.prog, 3, 0)
        grid.addWidget(self.pregress_bar, 3, 1, 1, 2)

        grid.addWidget(self.review, 4, 0)
        grid.addWidget(self.reviewEdit, 4, 1, 5, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('NoverDownloader')


class HcUrl:
    def __init__(self, url: str):
        self.url = url
        self.__parts = {}

    def get(self, key: str):
        return self.__parts[key]

    def parse(self):
        se_url = re.sub("(http.?):\/\/", '', self.url)
        self.__parts['domain'] = se_url.split('/')[0]
        return self


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec_())
    sys.stdout = app.old
