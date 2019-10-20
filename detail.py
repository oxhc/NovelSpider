# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 802)
        MainWindow.setStyleSheet("border-color: rgb(60, 12, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(220, 130, 561, 611))
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
                                      "                        }\n"
                                      "                    ")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 60, 351, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.url_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.url_input.setText("")
        self.url_input.setObjectName("url_input")
        self.horizontalLayout.addWidget(self.url_input)
        self.selected_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.selected_button.setStyleSheet("padding:3px;\n"
                                           "border-radius:1px;")
        self.selected_button.setObjectName("selected_button")
        self.horizontalLayout.addWidget(self.selected_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.book_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.book_name.setText("")
        self.book_name.setObjectName("book_name")
        self.horizontalLayout_2.addWidget(self.book_name)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.author = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.author.setText("")
        self.author.setObjectName("author")
        self.horizontalLayout_2.addWidget(self.author)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.status = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.status.setText("")
        self.status.setObjectName("status")
        self.horizontalLayout_5.addWidget(self.status)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.mode_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.mode_name.setText("")
        self.mode_name.setObjectName("mode_name")
        self.horizontalLayout_6.addWidget(self.mode_name)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_3 = QtWidgets.QLabel(self.mainWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 54, 12))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 121, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget_2)
        self.graphicsView.setStyleSheet("background-image: url(:/ui_design/xn.jpg);")
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.CrossPattern)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.mainWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 540, 201, 37))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.mainWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(470, 10, 81, 21))
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
        self.catalog_table = QtWidgets.QTableWidget(self.mainWidget)
        self.catalog_table.setGeometry(QtCore.QRect(30, 270, 501, 241))
        self.catalog_table.setObjectName("catalog_table")
        self.catalog_table.setColumnCount(0)
        self.catalog_table.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NoverDownloader"))
        self.label.setText(_translate("MainWindow", "网址:"))
        self.selected_button.setText(_translate("MainWindow", "查询"))
        self.label_2.setText(_translate("MainWindow", "书名:"))
        self.label_4.setText(_translate("MainWindow", "作者:"))
        self.label_6.setText(_translate("MainWindow", "状态:"))
        self.label_8.setText(_translate("MainWindow", "匹配模式:"))
        self.label_3.setText(_translate("MainWindow", "目录:"))
        self.label_5.setText(_translate("MainWindow", "封面"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.pushButton.setText(_translate("MainWindow", "开始下载"))
        self.label_7.setText(_translate("MainWindow", "书籍详情"))


import ff_rc
