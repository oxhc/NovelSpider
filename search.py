# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(962, 638)
        SearchWindow.setStyleSheet("border-color: rgb(60, 12, 255);")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.mainWidget.setFont(font)
        self.mainWidget.setStyleSheet("#mainWidget {\n"
"                        background-color: #fafafa;\n"
"                        border-width: 1px 1px 1px 1px;\n"
"                        border-style: solid;\n"
"                        border-color: rgb(160,160,160);\n"
"                        border-radius:6px;\n"
"                        }\n"
"                        QPushButton {\n"
"\n"
"                        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 159, 232 ,\n"
"                        255), stop:1 rgba(89, 183, 252, 255));\n"
"                        padding:10px;\n"
"                        color:white;\n"
"                        border-radius:10px;\n"
"\n"
"                        }\n"
"                        #close_button {\n"
"                        padding:5px;\n"
"                        border-radius:15px;\n"
"                        }\n"
"\n"
"                        QLineEdit {\n"
"                        border-width: 1px 1px 1px 1px;\n"
"                        border-style: solid;\n"
"                        border-color: rgb(160,160,160);\n"
"                        border-radius:3px;\n"
"                        height:30px;\n"
"                        }\n"
"                    ")
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.mainWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(850, 10, 81, 21))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.close_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button.setMaximumSize(QtCore.QSize(15, 15))
        self.close_button.setBaseSize(QtCore.QSize(17, 17))
        self.close_button.setStyleSheet("background-color: #f46b72;\n"
"                                        border-radius:7px;\n"
"                                    ")
        self.close_button.setText("")
        self.close_button.setAutoDefault(False)
        self.close_button.setDefault(False)
        self.close_button.setFlat(False)
        self.close_button.setObjectName("close_button")
        self.gridLayout.addWidget(self.close_button, 0, 2, 1, 1)
        self.title_button_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.title_button_2.setMaximumSize(QtCore.QSize(15, 15))
        self.title_button_2.setStyleSheet("background-color: #f9c846;\n"
"                                        border-radius:7px;\n"
"                                    ")
        self.title_button_2.setText("")
        self.title_button_2.setObjectName("title_button_2")
        self.gridLayout.addWidget(self.title_button_2, 0, 1, 1, 1)
        self.title_button_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.title_button_3.setMinimumSize(QtCore.QSize(16, 0))
        self.title_button_3.setMaximumSize(QtCore.QSize(15, 15))
        self.title_button_3.setStyleSheet("background-color: #3fb89f;\n"
"                                        border-radius:7px;\n"
"                                    ")
        self.title_button_3.setText("")
        self.title_button_3.setObjectName("title_button_3")
        self.gridLayout.addWidget(self.title_button_3, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.mainWidget)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 161, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.mybooks = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.mybooks.setObjectName("mybooks")
        self.mybooks.setColumnCount(1)
        self.mybooks.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.mybooks.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mybooks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mybooks.setItem(0, 0, item)
        self.verticalLayout.addWidget(self.mybooks)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 50, 701, 541))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setMinimumSize(QtCore.QSize(47, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.search_button.setMinimumSize(QtCore.QSize(77, 0))
        self.search_button.setObjectName("search_button")
        self.gridLayout_2.addWidget(self.search_button, 0, 2, 1, 1)
        self.book_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.book_name.setMinimumSize(QtCore.QSize(0, 7))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.book_name.setFont(font)
        self.book_name.setText("")
        self.book_name.setObjectName("book_name")
        self.gridLayout_2.addWidget(self.book_name, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.catalog_table = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.catalog_table.setShowGrid(True)
        self.catalog_table.setRowCount(1)
        self.catalog_table.setColumnCount(1)
        self.catalog_table.setObjectName("catalog_table")
        self.gridLayout_2.addWidget(self.catalog_table, 2, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_3.addWidget(self.mainWidget, 0, 1, 1, 1)
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "NoverDownloader"))
        self.label_7.setText(_translate("SearchWindow", "书籍搜索"))
        self.label_2.setText(_translate("SearchWindow", "我的书架"))
        item = self.mybooks.verticalHeaderItem(0)
        item.setText(_translate("SearchWindow", "1"))
        item = self.mybooks.horizontalHeaderItem(0)
        item.setText(_translate("SearchWindow", "书名"))
        __sortingEnabled = self.mybooks.isSortingEnabled()
        self.mybooks.setSortingEnabled(False)
        item = self.mybooks.item(0, 0)
        item.setText(_translate("SearchWindow", "仙逆"))
        self.mybooks.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("SearchWindow", "小说名称"))
        self.search_button.setText(_translate("SearchWindow", "搜索"))
        self.label_3.setText(_translate("SearchWindow", "搜索结果:"))
import ff_rc
