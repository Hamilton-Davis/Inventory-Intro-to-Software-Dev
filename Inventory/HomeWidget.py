# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QPushButton, QSizePolicy)

class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        if not HomeScreen.objectName():
            HomeScreen.setObjectName(u"HomeScreen")
        HomeScreen.resize(718, 499)
        font = QFont()
        font.setBold(False)
        HomeScreen.setFont(font)
        self.label = QLabel(HomeScreen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 541, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(40)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setWordWrap(False)
        self.inventoryButton = QPushButton(HomeScreen)
        self.inventoryButton.setObjectName(u"inventoryButton")
        self.inventoryButton.setGeometry(QRect(30, 230, 150, 150))
        self.salesButton = QPushButton(HomeScreen)
        self.salesButton.setObjectName(u"salesButton")
        self.salesButton.setGeometry(QRect(270, 230, 150, 150))
        self.settingsButton = QPushButton(HomeScreen)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(500, 230, 150, 150))
        self.exitButton = QPushButton(HomeScreen)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(620, 410, 75, 75))

        self.retranslateUi(HomeScreen)

        QMetaObject.connectSlotsByName(HomeScreen)
    # setupUi

    def retranslateUi(self, HomeScreen):
        HomeScreen.setWindowTitle(QCoreApplication.translate("HomeScreen", u"Form", None))
        self.label.setText(QCoreApplication.translate("HomeScreen", u"Inventory Management", None))
        self.inventoryButton.setText(QCoreApplication.translate("HomeScreen", u"Check Inventory", None))
        self.salesButton.setText(QCoreApplication.translate("HomeScreen", u"Sales Analysis", None))
        self.settingsButton.setText(QCoreApplication.translate("HomeScreen", u"Settings", None))
        self.exitButton.setText(QCoreApplication.translate("HomeScreen", u"Exit", None))
    # retranslateUi
