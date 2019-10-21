import os
import sys

from components.NoverDownloader import NoverDownloader
from utils.thread_run import ThreadProxy
from PyQt5 import QtCore, Qt
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView

from detail import Ui_MainWindow
from manage import load_mapping
from url_parse import HcUrl
from utils.utils_common import load_config


class BookWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UIProxy()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.set_table()
        self.setBound()


    def set_table(self):
        self.ui.catalog_table.setColumnCount(2)
        self.ui.catalog_table.setRowCount(0)
        self.ui.catalog_table.setHorizontalHeaderLabels(["章节名称", "下载"])
        self.ui.catalog_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.catalog_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.catalog_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def setBound(self):
        self.ui.close_button.clicked.connect(self.close)
        self.ui.selected_button.clicked.connect(self.ui.get_info)
        self.ui.c.book_name_signal.connect(self.ui.book_name.setText)
        self.ui.c.mode_signal.connect(self.ui.mode_name.setText)
        self.ui.c.author_signal.connect(self.ui.author.setText)
        self.ui.c.status_signal.connect(self.ui.status.setText)
        self.ui.c.select_button_text_signal.connect(self.ui.selected_button.setText)
        self.ui.c.links_num_signal.connect(self.ui.catalog_table.setRowCount)
        self.ui.c.links_signal.connect(self.ui.set_table_data)
        self.ui.download_button.clicked.connect(self.ui.dowload_thread)
        self.ui.c.download_total_signal.connect(self.ui.progress_obj.setMaximum)
        self.ui.c.download_num_signal.connect(lambda x:self.ui.progress_obj.setValue(self.ui.progress_obj.value()+x))

    def mousePressEvent(self, event):
        if event.button() == Qt.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.Qt.SizeAllCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.Qt.ArrowCursor))


class Communicate(QObject):
    book_name_signal = QtCore.pyqtSignal(str)
    author_signal = QtCore.pyqtSignal(str)
    update_date_signal = QtCore.pyqtSignal(str)
    status_signal = QtCore.pyqtSignal(str)
    mode_signal = QtCore.pyqtSignal(str)
    select_button_text_signal = QtCore.pyqtSignal(str)
    links_num_signal = QtCore.pyqtSignal(int)
    links_signal = QtCore.pyqtSignal(list)
    download_total_signal = QtCore.pyqtSignal(int)
    download_num_signal = QtCore.pyqtSignal(int)

def total(signal, num):
    signal.emit(num)


def update(signal, num):
    signal.emit(num)


class UIProxy(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.c = Communicate()

    def dowload_thread(self):
        try:
            self.thread = ThreadProxy(self.download, None, None)
            self.thread.start()
        except Exception:
            print("error")

    def download(self):
        print('start downloading')
        mapping = load_mapping()
        url = self.url_input.text()
        work_path = os.getcwd()
        config = load_config(work_path, mapping[HcUrl(url).parse().get('domain')] + '_config.json')
        from components.NoverDownloader import NoverDownloader
        nd = NoverDownloader(
            url,
            config, work_path=work_path,
            set_total=lambda x: total(self.c.download_total_signal, x),
            update=lambda x: update(self.c.download_num_signal, x),
            max_worker=20
        )
        if nd.start():
            nd.make_book()
            print("全部下载完毕")
        else:
            nd.make_book()
            print("失败章节:")
            for i in nd.faild_list:
                print(i)

    def fetch_info(self):
        self.c.select_button_text_signal.emit("稍后")
        mapping = load_mapping()
        url = self.url_input.text()
        work_path = os.getcwd()
        mode_name = mapping[HcUrl(url).parse().get('domain')]
        config = load_config(work_path, mode_name + '_config.json')
        nd = NoverDownloader(
            url,
            config, work_path=work_path,
            max_worker=20
        )
        self.c.book_name_signal.emit(nd.book_name)
        self.c.author_signal.emit(nd.book_info['author'])
        self.c.status_signal.emit(nd.book_info['status'])
        self.c.update_date_signal.emit(nd.book_info['update_date'])
        self.c.mode_signal.emit(mode_name)
        self.c.links_num_signal.emit(len(nd.links))
        self.c.links_signal.emit(nd.links_name)
        self.c.select_button_text_signal.emit("查询")

    def set_table_data(self, cata_list):
        for i in range(0, len(cata_list)):
            self.catalog_table.setItem(i, 0, QTableWidgetItem(cata_list[i]))

    def get_info(self):
        try:
            self.thread = ThreadProxy(self.fetch_info, None, None)
            self.thread.start()
        except Exception:
            print("error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = BookWindow()
    mainWindow.show()
    sys.exit(app.exec_())
