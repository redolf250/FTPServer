# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainIfOmaB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1170, 901)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 5, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 110))
        self.topBar.setStyleSheet(u"")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.topBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBarItems = QFrame(self.topBar)
        self.topBarItems.setObjectName(u"topBarItems")
        self.topBarItems.setMinimumSize(QSize(0, 65))
        self.topBarItems.setMaximumSize(QSize(16777215, 60))
        self.topBarItems.setStyleSheet(u"")
        self.topBarItems.setFrameShape(QFrame.NoFrame)
        self.topBarItems.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topBarItems)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 3)
        self.label_7 = QLabel(self.topBarItems)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_6 = QLabel(self.topBarItems)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 0))
        self.label_6.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamily(u"Monotype Corsiva")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"padding-left: 10px;")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.appCurrentFrame = QFrame(self.topBarItems)
        self.appCurrentFrame.setObjectName(u"appCurrentFrame")
        self.appCurrentFrame.setStyleSheet(u"")
        self.appCurrentFrame.setFrameShape(QFrame.StyledPanel)
        self.appCurrentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.appCurrentFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.appCurrentFrame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.appCurrentFrame)

        self.date = QFrame(self.topBarItems)
        self.date.setObjectName(u"date")
        self.date.setMinimumSize(QSize(100, 0))
        self.date.setMaximumSize(QSize(100, 16777215))
        self.date.setStyleSheet(u"")
        self.date.setFrameShape(QFrame.StyledPanel)
        self.date.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.date)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_minimize = QPushButton(self.date)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 255, 127);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(85, 255, 127,150);\n"
"	\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.date)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.date)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_close)


        self.horizontalLayout_2.addWidget(self.date)


        self.verticalLayout_2.addWidget(self.topBarItems)


        self.verticalLayout.addWidget(self.topBar)

        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.menu = QFrame(self.main)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(250, 0))
        self.menu.setMaximumSize(QSize(250, 16777215))
        self.menu.setStyleSheet(u"#menu{\n"
"	background-color: rgb(35, 34, 48);\n"
"    border-top-right-radius: 100px;\n"
"}")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.frame = QFrame(self.menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 250))
        self.frame.setStyleSheet(u"background-color: rgb(35, 34, 48);\n"
"border-top-right-radius: 100px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 30, -1, -1)
        self.profile = QLabel(self.frame)
        self.profile.setObjectName(u"profile")
        font2 = QFont()
        font2.setPointSize(12)
        self.profile.setFont(font2)
        self.profile.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 60px;\n"
"")
        self.profile.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.profile)

        self.userName = QLabel(self.frame)
        self.userName.setObjectName(u"userName")
        self.userName.setMaximumSize(QSize(16777215, 50))
        self.userName.setFont(font1)
        self.userName.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.userName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.userName)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 300))
        self.frame_2.setStyleSheet(u"background-color: rgb(35, 34, 48);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.btn_home = QPushButton(self.frame_2)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(11)
        self.btn_home.setFont(font3)
        self.btn_home.setStyleSheet(u"QPushButton#btn_home{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	padding-left:5px;\n"
"}\n"
"\n"
"QPushButton#btn_home:pressed{\n"
"	color: rgb(93, 93, 93);\n"
"}\n"
" QPushButtonbtn_home:focus{\n"
"           color: rgb(93, 93, 93);\n"
"            padding-left:5px;\n"
"\n"
"        \n"
"  }\n"
"\n"
"QPushButton#btn_home:hover{\n"
"    color: rgb(93, 93, 93);\n"
"    padding-left: 15px; \n"
"border-left: 3px solid rgb(255, 255, 255);\n"
"}")
        self.btn_home.setIconSize(QSize(30, 30))
        self.btn_home.setAutoDefault(False)
        self.btn_home.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_dashboard = QPushButton(self.frame_2)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setMaximumSize(QSize(16777215, 50))
        self.btn_dashboard.setFont(font3)
        self.btn_dashboard.setStyleSheet(u"QPushButton#btn_dashboard{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#btn_dashboard:pressed{\n"
"	color: rgb(93, 93, 93);\n"
"}\n"
" QPushButton#btn_dashboard:focus{\n"
"           color: rgb(93, 93, 93);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"QPushButton#btn_dashboard:hover{\n"
"    color: rgb(93, 93, 93); \n"
" padding-left: 15px; \n"
"}")
        self.btn_dashboard.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_dashboard)

        self.btn_statistics = QPushButton(self.frame_2)
        self.btn_statistics.setObjectName(u"btn_statistics")
        self.btn_statistics.setMaximumSize(QSize(16777215, 50))
        self.btn_statistics.setFont(font3)
        self.btn_statistics.setStyleSheet(u"QPushButton#btn_statistics{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#btn_statistics:pressed{\n"
"	color: rgb(93, 93, 93);\n"
"}\n"
" QPushButton#btn_statistics:focus{\n"
"           color: rgb(93, 93, 93);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"QPushButton#btn_statistics:hover{\n"
"    color: rgb(93, 93, 93); \n"
"	 padding-left: 15px; \n"
"}")
        self.btn_statistics.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_statistics)

        self.btn_settings = QPushButton(self.frame_2)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMaximumSize(QSize(16777215, 50))
        self.btn_settings.setFont(font3)
        self.btn_settings.setStyleSheet(u"QPushButton#btn_settings{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButtonbtn_settings:pressed{\n"
"	color: rgb(93, 93, 93);\n"
"}\n"
" QPushButton#btn_settings:focus{\n"
"           color: rgb(93, 93, 93);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"QPushButton#btn_settings:hover{\n"
"    color: rgb(93, 93, 93); \n"
" 	padding-left: 15px; \n"
"}")
        self.btn_settings.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_settings)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 250))
        self.frame_3.setStyleSheet(u"background-color: rgb(35, 34, 48);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.theme = QFrame(self.frame_3)
        self.theme.setObjectName(u"theme")
        self.theme.setGeometry(QRect(0, 180, 241, 60))
        self.theme.setStyleSheet(u"background-color: rgb(35, 34, 48);\n"
"border-radius:30px;")
        self.theme.setFrameShape(QFrame.StyledPanel)
        self.theme.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.theme)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_8 = QPushButton(self.theme)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setPointSize(10)
        self.pushButton_8.setFont(font4)
        self.pushButton_8.setStyleSheet(u"QPushButton#pushButton_6{\n"
"background-color: rgb(57, 57, 57);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_8.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.theme)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 40))
        self.pushButton_9.setFont(font4)
        self.pushButton_9.setStyleSheet(u"\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.pushButton_9.raise_()
        self.pushButton_8.raise_()

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame.raise_()

        self.horizontalLayout.addWidget(self.menu)

        self.content = QFrame(self.main)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.content)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_7 = QVBoxLayout(self.home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.home)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
"border-radius:10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(43)
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setPointSize(17)
        self.label_8.setFont(font6)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setPointSize(16)
        self.label_10.setFont(font7)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_10)


        self.horizontalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 70))
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        font8 = QFont()
        font8.setFamily(u"Monotype Corsiva")
        font8.setPointSize(25)
        font8.setItalic(True)
        self.label_11.setFont(font8)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_11)


        self.verticalLayout_9.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, 0, -1)
        self.bytesSent = QLabel(self.frame_7)
        self.bytesSent.setObjectName(u"bytesSent")
        self.bytesSent.setStyleSheet(u"QLabel#bytesSent{\n"
"	background-color: rgb(99, 99, 99);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_13.addWidget(self.bytesSent)

        self.bytesReceived = QLabel(self.frame_7)
        self.bytesReceived.setObjectName(u"bytesReceived")
        self.bytesReceived.setStyleSheet(u"QLabel#bytesReceived{\n"
"	background-color: rgb(99, 99, 99);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_13.addWidget(self.bytesReceived)

        self.bytesTotal = QLabel(self.frame_7)
        self.bytesTotal.setObjectName(u"bytesTotal")
        self.bytesTotal.setStyleSheet(u"QLabel#bytesTotal{\n"
"	background-color: rgb(99, 99, 99);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_13.addWidget(self.bytesTotal)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 11, 851, 371))
        self.tableWidget.setFont(font3)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.home)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.label_4 = QLabel(self.dashboard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 300, 291, 141))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.dashboard)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.label_2 = QLabel(self.settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 310, 291, 141))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.settings)
        self.statistics = QWidget()
        self.statistics.setObjectName(u"statistics")
        self.label_5 = QLabel(self.statistics)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 280, 291, 141))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.statistics)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.content)


        self.verticalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SecureShare", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.profile.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.userName.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"9900", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Files Sent", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Files Received", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total 1490000", None))
        self.bytesSent.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bytesReceived.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bytesTotal.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Setttings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Statistic", None))
    # retranslateUi

