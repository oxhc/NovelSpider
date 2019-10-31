import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_search import Ui_SearchWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_window = QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(search_window)
    ui.website_select.addItem('sss')
    ui.website_select.addItem('sss')
    ui.website_select.addItem('sss')
    ui.website_select.addItem('sss')
    search_window.show()
    sys.exit(app.exec_())