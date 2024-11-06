# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InventoryWidgetOwQwNz.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pathlib import Path
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QAbstractItemView, QLineEdit,
                               QPushButton, QTableWidget, QTableWidgetItem)

icons_path = Path(__file__).absolute().parent / 'icons'

class Ui_InventoryWidget(object):
    def setupUi(self, InventoryWidget):
        if not InventoryWidget.objectName():
            InventoryWidget.setObjectName(u"InventoryWidget")
        InventoryWidget.resize(830, 483)
        self.tableWidget = QTableWidget(InventoryWidget)
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
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(10, 60, 811, 371))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(8)
        font.setBold(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.saveButton = QPushButton(InventoryWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 440, 61, 26))
        icon = QIcon()
        icon.addFile(u"icons/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon)
        self.addItemButton = QPushButton(InventoryWidget)
        self.addItemButton.setObjectName(u"addItemButton")
        self.addItemButton.setGeometry(QRect(530, 440, 87, 26))
        icon1 = QIcon()
        icon1.addFile(u"icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addItemButton.setIcon(icon1)
        self.editItemButton = QPushButton(InventoryWidget)
        self.editItemButton.setObjectName(u"editItemButton")
        self.editItemButton.setGeometry(QRect(630, 440, 87, 26))
        icon2 = QIcon()
        icon2.addFile(u"icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editItemButton.setIcon(icon2)
        self.removeItemButton = QPushButton(InventoryWidget)
        self.removeItemButton.setObjectName(u"removeItemButton")
        self.removeItemButton.setGeometry(QRect(730, 440, 87, 26))
        font1 = QFont()
        font1.setPointSize(11)
        self.removeItemButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icons/trash-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.removeItemButton.setIcon(icon3)
        self.searchKeyBar = QLineEdit(InventoryWidget)
        self.searchKeyBar.setObjectName(u"searchKeyBar")
        self.searchKeyBar.setGeometry(QRect(490, 20, 331, 26))
        font2 = QFont()
        font2.setItalic(True)
        self.searchKeyBar.setFont(font2)
        self.homeButton = QPushButton(InventoryWidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 20, 71, 26))
        icon4 = QIcon()
        icon4.addFile(u"icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButton.setIcon(icon4)
        self.searchCategoryBar = QLineEdit(InventoryWidget)
        self.searchCategoryBar.setObjectName(u"searchCategoryBar")
        self.searchCategoryBar.setGeometry(QRect(190, 20, 291, 26))
        self.searchCategoryBar.setFont(font2)

        self.retranslateUi(InventoryWidget)

        QMetaObject.connectSlotsByName(InventoryWidget)
    # setupUi

    def retranslateUi(self, InventoryWidget):
        InventoryWidget.setWindowTitle(QCoreApplication.translate("InventoryWidget", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InventoryWidget", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InventoryWidget", u"Category", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InventoryWidget", u"Quantity", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InventoryWidget", u"Cost", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InventoryWidget", u"Sale Price", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InventoryWidget", u"Available", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InventoryWidget", u"Date Stocked", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InventoryWidget", u"Contact", None));
        self.saveButton.setText(QCoreApplication.translate("InventoryWidget", u"Save", None))
        self.addItemButton.setText(QCoreApplication.translate("InventoryWidget", u"Add", None))
        self.editItemButton.setText(QCoreApplication.translate("InventoryWidget", u"Edit", None))
        self.removeItemButton.setText(QCoreApplication.translate("InventoryWidget", u"Remove", None))
        self.searchKeyBar.setPlaceholderText(QCoreApplication.translate("InventoryWidget", u"Search for...", None))
        self.homeButton.setText(QCoreApplication.translate("InventoryWidget", u"Home", None))
        self.searchCategoryBar.setPlaceholderText(QCoreApplication.translate("InventoryWidget", u"Search in categories...", None))
    # retranslateUi

