# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InventoryWidgetWSOstE.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(830, 483)
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 60, 811, 371))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(8)
        font.setBold(True)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 440, 61, 26))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.saveButton.setIcon(icon)
        self.addItemButton = QPushButton(Form)
        self.addItemButton.setObjectName(u"addItemButton")
        self.addItemButton.setGeometry(QRect(530, 440, 87, 26))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.addItemButton.setIcon(icon1)
        self.editItemButton = QPushButton(Form)
        self.editItemButton.setObjectName(u"editItemButton")
        self.editItemButton.setGeometry(QRect(630, 440, 87, 26))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.editItemButton.setIcon(icon2)
        self.removeItemButton = QPushButton(Form)
        self.removeItemButton.setObjectName(u"removeItemButton")
        self.removeItemButton.setGeometry(QRect(730, 440, 87, 26))
        font1 = QFont()
        font1.setPointSize(11)
        self.removeItemButton.setFont(font1)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.removeItemButton.setIcon(icon3)
        self.searchBar = QLineEdit(Form)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(370, 20, 401, 26))
        font2 = QFont()
        font2.setItalic(True)
        self.searchBar.setFont(font2)
        self.searchButton = QPushButton(Form)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(780, 20, 41, 26))
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.searchButton.setIcon(icon4)
        self.homeButton = QPushButton(Form)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 20, 71, 26))
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.homeButton.setIcon(icon5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Category", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Purchase Price", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Sale Price", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Available", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Date Stocked", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Contact", None));
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.addItemButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.editItemButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.removeItemButton.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("Form", u"Search Item", None))
        self.searchButton.setText("")
        self.homeButton.setText(QCoreApplication.translate("Form", u"Home", None))
    # retranslateUi

