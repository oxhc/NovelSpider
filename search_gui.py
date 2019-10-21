import sys

from utils.thread_run import ThreadProxy
from PyQt5 import QtCore, Qt
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView

from ui_search import Ui_SearchWindow
from search_book import search
from book_gui import BookWindow


class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()


class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UIProxy()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # mainWindow.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)
        self.ui.close_button.clicked.connect(self.close)

        self.ui.catalog_table.setColumnCount(3)
        self.ui.catalog_table.setRowCount(0)

        self.ui.catalog_table.setHorizontalHeaderLabels(["小说名称", "作者", "添加"])
        self.ui.catalog_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.mybooks.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.mybooks.verticalHeader().setVisible(False)
        self.ui.catalog_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.catalog_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.ui.catalog_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.catalog_table.setShowGrid(False)


        self.ui.search_button.clicked.connect(self.ui.get_info)
        self.ui.c.books_signal.connect(self.ui.set_table)
        self.ui.c.status_signal.connect(self.ui.search_button.setText)


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
    books_signal = QtCore.pyqtSignal(list)
    status_signal = QtCore.pyqtSignal(str)
    open_book_signal = QtCore.pyqtSignal(bool)
    url_signal = QtCore.pyqtSignal(str)


class UIProxy(Ui_SearchWindow):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.c = Communicate()
        self.books = None

    def get_info(self):
        self.c.status_signal.emit("正在搜索")
        self.thread = ThreadProxy(search, self.book_name.text(), self.c.books_signal)
        self.thread.start()

    def item_clicked(self, url):
        print(url)
        self.c.open_book_signal.emit(True)
        self.c.url_signal.emit(url)


    def set_table(self, books):
        print(books)
        self.books = books
        self.catalog_table.setRowCount(len(books))
        self.catalog_table.itemClicked.connect(lambda x:self.item_clicked(self.books[x.row()]['href']))
        for i in range(0, len(books)):
            print(books[i]['book_name'])
            self.catalog_table.setItem(i, 0, QTableWidgetItem(books[i]['book_name']))
            self.catalog_table.setItem(i, 1, QTableWidgetItem(books[i]['author']))
            self.catalog_table.setItem(i, 2, QTableWidgetItem(QIcon("resource/add_to_books.png"), ""))

        self.c.status_signal.emit("搜索")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_window = SearchWindow()
    book_window = BookWindow()
    # book_window.show()
    search_window.ui.c.url_signal.connect(book_window.ui.url_input.setText)
    search_window.ui.c.open_book_signal.connect(book_window.show)
    search_window.ui.c.open_book_signal.connect(book_window.raise_)
    search_window.ui.c.open_book_signal.connect(book_window.ui.get_info)
    search_window.show()
    sys.exit(app.exec_())
