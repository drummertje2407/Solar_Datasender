# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\SolarUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import qdarkstyle
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer


from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1091, 871))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.SignalLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SignalLabel.setObjectName("SignalLabel")
        self.gridLayout.addWidget(self.SignalLabel, 0, 2, 1, 1)

        self.MainTimeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.MainTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainTimeLabel.setObjectName("MainTimeLabel")
        self.gridLayout.addWidget(self.MainTimeLabel, 0, 1, 1, 1)



        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(23, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        def Dashboardtab(self):
            self.Dashboardtab = QtWidgets.QWidget()
            self.Dashboardtab.setObjectName("Dashboardtab")
            self.layoutWidget = QtWidgets.QWidget(self.Dashboardtab)
            self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 921, 841))
            self.layoutWidget.setObjectName("layoutWidget")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
            self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
            self.gridLayout_2.setObjectName("gridLayout_2")

            self.timeLabel = QtWidgets.QLabel(self.layoutWidget)
            font = QtGui.QFont()
            font.setFamily("Segoe UI Semibold")
            font.setPointSize(30)
            font.setBold(True)
            font.setWeight(75)
            self.timeLabel.setFont(font)
            self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.timeLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.timeLabel.setObjectName("timeLabel")
            self.gridLayout_2.addWidget(self.timeLabel, 0, 1, 1, 1)

            self.Infopanel_1 = QtWidgets.QFormLayout()
            self.Infopanel_1.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
            self.Infopanel_1.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.Infopanel_1.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.Infopanel_1.setObjectName("Infopanel_1")

            self.voltageLabel1 = QtWidgets.QLabel(self.layoutWidget)
            self.voltageLabel1.setMinimumSize(QtCore.QSize(200, 70))
            font = QtGui.QFont()
            font.setPointSize(34)
            self.voltageLabel1.setFont(font)
            self.voltageLabel1.setMidLineWidth(0)
            self.voltageLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.voltageLabel1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.voltageLabel1.setObjectName("voltageLabel1")
            self.Infopanel_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.voltageLabel1)

            self.powerLabel1 = QtWidgets.QLabel(self.layoutWidget)
            self.powerLabel1.setMinimumSize(QtCore.QSize(200, 70))
            font = QtGui.QFont()
            font.setPointSize(34)
            self.powerLabel1.setFont(font)
            self.powerLabel1.setMidLineWidth(0)
            self.powerLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.powerLabel1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.powerLabel1.setObjectName("powerLabel1")
            self.Infopanel_1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.powerLabel1)

            self.voltageLabel2 = QtWidgets.QLabel(self.layoutWidget)
            font = QtGui.QFont()
            font.setPointSize(34)
            self.voltageLabel2.setFont(font)
            self.voltageLabel2.setObjectName("voltageLabel2")
            self.Infopanel_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voltageLabel2)
            self.powerLabel2 = QtWidgets.QLabel(self.layoutWidget)
            font = QtGui.QFont()
            font.setPointSize(34)
            self.powerLabel2.setFont(font)
            self.powerLabel2.setObjectName("powerLabel2")
            self.Infopanel_1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.powerLabel2)

            self.gridLayout_2.addLayout(self.Infopanel_1, 2, 0, 1, 1)

            self.LapLabel = QtWidgets.QLabel(self.layoutWidget)
            font = QtGui.QFont()
            font.setFamily("Segoe UI Semibold")
            font.setPointSize(30)
            font.setBold(True)
            font.setWeight(75)
            self.LapLabel.setFont(font)
            self.LapLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.LapLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.LapLabel.setObjectName("LapLabel")
            self.gridLayout_2.addWidget(self.LapLabel, 0, 0, 1, 1)

            self.Infopanel_2 = QtWidgets.QFormLayout()
            self.Infopanel_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
            self.Infopanel_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.Infopanel_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.Infopanel_2.setObjectName("Infopanel_2")

            self.voltageLabel1_2 = QtWidgets.QLabel(self.layoutWidget)
            self.voltageLabel1_2.setMinimumSize(QtCore.QSize(200, 70))
            font = QtGui.QFont()
            font.setPointSize(34)
            self.voltageLabel1_2.setFont(font)
            self.voltageLabel1_2.setMidLineWidth(0)
            self.voltageLabel1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.voltageLabel1_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.voltageLabel1_2.setObjectName("voltageLabel1_2")
            self.Infopanel_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.voltageLabel1_2)

            self.powerLabel1_2 = QtWidgets.QLabel(self.layoutWidget)
            self.powerLabel1_2.setMinimumSize(QtCore.QSize(200, 70))
            font = QtGui.QFont()
            font.setPointSize(34)
            self.powerLabel1_2.setFont(font)
            self.powerLabel1_2.setMidLineWidth(0)
            self.powerLabel1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.powerLabel1_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.powerLabel1_2.setObjectName("powerLabel1_2")
            self.Infopanel_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.powerLabel1_2)

            self.voltageLabel2_2 = QtWidgets.QLabel(self.layoutWidget)
            font = QtGui.QFont()
            font.setPointSize(34)
            self.voltageLabel2_2.setFont(font)
            self.voltageLabel2_2.setObjectName("voltageLabel2_2")
            self.Infopanel_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voltageLabel2_2)

            self.powerLabel2_2 = QtWidgets.QLabel(self.layoutWidget)
            font = QtGui.QFont()
            font.setPointSize(34)
            self.powerLabel2_2.setFont(font)
            self.powerLabel2_2.setObjectName("powerLabel2_2")
            self.Infopanel_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.powerLabel2_2)

            self.gridLayout_2.addLayout(self.Infopanel_2, 2, 1, 1, 1)

            self.browser = QWebView(self.Dashboardtab)
            self.browser.setGeometry(QtCore.QRect(130, 50, MainWindow.width() - 200, 481))
            self.browser.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.browser.setHtml(""""
                                                            <html>
                                                                <body>
                                                                    <iframe width="560" height="315" src="https://www.estela.co/en/tracking-race/5177/basto-8-milles-ie-lescala-2" frameborder="0" allowfullscreen>
                                                                    </iframe>
                                                                </body>
                                                            <html>""")
            self.browser.setObjectName("Browser")

            self.tabWidget.addTab(self.Dashboardtab, "")

        def tab_2(self):
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.tabWidget.addTab(self.tab_2, "")
            self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)

        def Errorbar(self):
            self.verticalLayout_4 = QtWidgets.QVBoxLayout()
            self.verticalLayout_4.setObjectName("verticalLayout_4")

            self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_7.setObjectName("label_7")
            self.verticalLayout_4.addWidget(self.label_7)

            self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_5.setObjectName("label_5")
            self.verticalLayout_4.addWidget(self.label_5)

            self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_4.setObjectName("label_4")
            self.verticalLayout_4.addWidget(self.label_4)

            self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_2.setObjectName("label_2")
            self.verticalLayout_4.addWidget(self.label_2)

            spacerItem = QtWidgets.QSpacerItem(20, 155, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_4.addItem(spacerItem)
            self.gridLayout.addLayout(self.verticalLayout_4, 1, 2, 1, 1)

        def Navigationbar(self):
            self.NavigationBar = QtWidgets.QVBoxLayout()
            self.NavigationBar.setSpacing(4)
            self.NavigationBar.setObjectName("NavigationBar")

            self.tabButton1 = QtWidgets.QPushButton(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tabButton1.sizePolicy().hasHeightForWidth())

            self.tabButton1.setSizePolicy(sizePolicy)
            self.tabButton1.setCheckable(True)
            self.tabButton1.setAutoExclusive(False)
            self.tabButton1.setAutoDefault(False)
            self.tabButton1.setDefault(False)
            self.tabButton1.setFlat(False)
            self.tabButton1.setObjectName("tabButton1")
            self.NavigationBar.addWidget(self.tabButton1)
            self.tabButton2 = QtWidgets.QPushButton(self.gridLayoutWidget)

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tabButton2.sizePolicy().hasHeightForWidth())
            self.tabButton2.setSizePolicy(sizePolicy)
            self.tabButton2.setCheckable(True)
            self.tabButton2.setAutoExclusive(False)
            self.tabButton2.setAutoDefault(False)
            self.tabButton2.setDefault(False)
            self.tabButton2.setFlat(False)
            self.tabButton2.setObjectName("tabButton2")
            self.NavigationBar.addWidget(self.tabButton2)

            self.tabButton3 = QtWidgets.QPushButton(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tabButton3.sizePolicy().hasHeightForWidth())
            self.tabButton3.setSizePolicy(sizePolicy)
            self.tabButton3.setCheckable(True)
            self.tabButton3.setAutoExclusive(False)
            self.tabButton3.setAutoDefault(False)
            self.tabButton3.setDefault(False)
            self.tabButton3.setFlat(False)
            self.tabButton3.setObjectName("tabButton3")
            self.NavigationBar.addWidget(self.tabButton3)

            self.tabButton4 = QtWidgets.QPushButton(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tabButton4.sizePolicy().hasHeightForWidth())
            self.tabButton4.setSizePolicy(sizePolicy)
            self.tabButton4.setCheckable(True)
            self.tabButton4.setAutoExclusive(False)
            self.tabButton4.setAutoDefault(False)
            self.tabButton4.setDefault(False)
            self.tabButton4.setFlat(False)
            self.tabButton4.setObjectName("tabButton4")
            self.NavigationBar.addWidget(self.tabButton4)
            self.gridLayout.addLayout(self.NavigationBar, 1, 0, 1, 1)

            # Connect all the buttons, using lambda because otherwhise we can't pass on an argument:
            self.tabButton1.clicked.connect(lambda: self.NavButton_clicked(1))
            self.tabButton2.clicked.connect(lambda: self.NavButton_clicked(2))
            self.tabButton3.clicked.connect(lambda: self.NavButton_clicked(3))
            self.tabButton4.clicked.connect(lambda: self.NavButton_clicked(4))

        MainWindow.setCentralWidget(self.centralwidget)

        Dashboardtab(self)
        tab_2(self)
        Errorbar(self)
        Navigationbar(self)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.SignalLabel.setText(_translate("MainWindow", "TextLabel"))
        self.MainTimeLabel.setText(_translate("MainWindow", "15:12"))
        self.tabButton1.setText(_translate("MainWindow", "PushButton"))
        self.tabButton2.setText(_translate("MainWindow", "PushButton"))
        self.tabButton3.setText(_translate("MainWindow", "PushButton"))
        self.tabButton4.setText(_translate("MainWindow", "PushButton"))
        self.timeLabel.setText(_translate("MainWindow", "02:59:37"))
        self.voltageLabel1.setText(_translate("MainWindow", "24.1"))
        self.powerLabel1.setText(_translate("MainWindow", "24.1"))
        self.voltageLabel2.setText(_translate("MainWindow", "V"))
        self.powerLabel2.setText(_translate("MainWindow", "W"))
        self.LapLabel.setText(_translate("MainWindow", "1 / 5"))
        self.voltageLabel1_2.setText(_translate("MainWindow", "18"))
        self.powerLabel1_2.setText(_translate("MainWindow", "100"))
        self.voltageLabel2_2.setText(_translate("MainWindow", "km/h"))
        self.powerLabel2_2.setText(_translate("MainWindow", "W"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dashboardtab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

    def NavButton_clicked(self, button):
        if button == 1:
            self.tabWidget.setCurrentIndex(0)
            self.tabButton2.setChecked(False)
            self.tabButton3.setChecked(False)
            self.tabButton4.setChecked(False)
        if button == 2:
            self.tabWidget.setCurrentIndex(1)
            self.tabButton1.setChecked(False)
            self.tabButton3.setChecked(False)
            self.tabButton4.setChecked(False)
        if button == 3:
            self.tabWidget.setCurrentIndex(2)
            self.tabButton1.setChecked(False)
            self.tabButton2.setChecked(False)
            self.tabButton4.setChecked(False)
        if button == 4:
            self.tabWidget.setCurrentIndex(3)
            self.tabButton1.setChecked(False)
            self.tabButton2.setChecked(False)
            self.tabButton3.setChecked(False)









