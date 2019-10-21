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
        MainWindow.resize(627, 424)
        MainWindow.setStyleSheet("border-color: rgb(60, 12, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.mainWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 340, 201, 37))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.download_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_3.addWidget(self.download_button)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.mainWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(530, 10, 81, 21))
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(340, 50, 251, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.catalog_table = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.catalog_table.setShowGrid(True)
        self.catalog_table.setRowCount(1)
        self.catalog_table.setColumnCount(1)
        self.catalog_table.setObjectName("catalog_table")
        self.verticalLayout_4.addWidget(self.catalog_table)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 50, 291, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.url_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.url_input.setText("")
        self.url_input.setObjectName("url_input")
        self.horizontalLayout.addWidget(self.url_input)
        self.selected_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.selected_button.setStyleSheet("padding:3px;\n"
"                                                border-radius:1px;\n"
"                                            ")
        self.selected_button.setObjectName("selected_button")
        self.horizontalLayout.addWidget(self.selected_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget_4)
        self.graphicsView.setMinimumSize(QtCore.QSize(120, 0))
        self.graphicsView.setMaximumSize(QtCore.QSize(118, 152))
        self.graphicsView.setStyleSheet("background-image: url(:/ui_design/xn.jpg);")
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.CrossPattern)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.book_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.book_name.setText("")
        self.book_name.setObjectName("book_name")
        self.horizontalLayout_7.addWidget(self.book_name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.author = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.author.setText("")
        self.author.setObjectName("author")
        self.horizontalLayout_2.addWidget(self.author)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.mode_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.mode_name.setText("")
        self.mode_name.setObjectName("mode_name")
        self.horizontalLayout_6.addWidget(self.mode_name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.status = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.status.setText("")
        self.status.setObjectName("status")
        self.horizontalLayout_5.addWidget(self.status)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.progress_obj = QtWidgets.QProgressBar(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.progress_obj.setFont(font)
        self.progress_obj.setStyleSheet("color:white;\n"
"border-radius:10px;")
        self.progress_obj.setMinimum(0)
        self.progress_obj.setMaximum(100)
        self.progress_obj.setProperty("value", 0)
        self.progress_obj.setTextVisible(True)
        self.progress_obj.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progress_obj.setObjectName("progress_obj")
        self.horizontalLayout_4.addWidget(self.progress_obj)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.mainWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NoverDownloader"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.download_button.setText(_translate("MainWindow", "开始下载"))
        self.label_7.setText(_translate("MainWindow", "书籍详情"))
        self.label_3.setText(_translate("MainWindow", "目录:"))
        self.label.setText(_translate("MainWindow", "网址:"))
        self.selected_button.setText(_translate("MainWindow", "查询"))
        self.label_5.setText(_translate("MainWindow", "封面"))
        self.label_2.setText(_translate("MainWindow", "书名:"))
        self.label_4.setText(_translate("MainWindow", "作者:"))
        self.label_8.setText(_translate("MainWindow", "匹配模式:"))
        self.label_6.setText(_translate("MainWindow", "状态:"))
        self.label_9.setText(_translate("MainWindow", "下载进度:"))
        self.progress_obj.setFormat(_translate("MainWindow", "  %p%"))
import ff_rc
