import os
import sys

from components.NoverDownloader import NoverDownloader
from gui.thread_run import ThreadProxy
from PyQt5 import QtCore, Qt
from PyQt5.QtCore import QCoreApplication, QObject
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView

from detail import Ui_MainWindow
from manage import load_mapping
from url_parse import HcUrl
from utils import load_config


class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()


class BookWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UIProxy()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # mainWindow.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.selected_button.clicked.connect(self.ui.get_info)
        self.ui.c.book_name_signal.connect(self.ui.book_name.setText)
        self.ui.c.mode_signal.connect(self.ui.mode_name.setText)
        self.ui.c.author_signal.connect(self.ui.author.setText)
        # ui.c.update_date_signal.connect(ui.up.setText)
        self.ui.c.status_signal.connect(self.ui.status.setText)
        self.ui.c.select_button_text_signal.connect(self.ui.selected_button.setText)
        self.ui.catalog_table.setColumnCount(2)
        self.ui.catalog_table.setRowCount(0)


        self.ui.catalog_table.setHorizontalHeaderLabels(["章节名称", "下载"])
        self.ui.catalog_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.catalog_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.catalog_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.c.links_num_signal.connect(self.ui.catalog_table.setRowCount)
        self.ui.c.links_signal.connect(self.ui.set_table_data)

    def select(self):
        pass

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



class UIProxy(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.thread = None
        self.c = Communicate()
        self.items = [
            'haha',
            'xxxx'
        ]

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
        print(nd.catalog_url)
        print(nd.book_name)
        self.c.book_name_signal.emit(nd.book_name)
        print(nd.book_info['author'])
        self.c.author_signal.emit(nd.book_info['author'])
        self.c.status_signal.emit(nd.book_info['status'])
        self.c.update_date_signal.emit(nd.book_info['update_date'])
        self.c.mode_signal.emit(mode_name)
        self.c.links_num_signal.emit(len(nd.links))
        self.c.links_signal.emit(nd.links_name)
        print(nd.book_info['status'])
        print(nd.book_info['update_date'])
        print(mode_name)
        self.c.select_button_text_signal.emit("查询")

    def set_table_data(self, cata_list):
        for i in range(0, len(cata_list)):
            self.catalog_table.setItem(i,0, QTableWidgetItem(cata_list[i]))


    def get_info(self):
        self.thread = ThreadProxy(self.fetch_info, None, None)
        self.thread.start()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = BookWindow()

    
    # styleFile = './style.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # mainWindow.setStyleSheet(qssStyle)

    mainWindow.show()
    sys.exit(app.exec_())
