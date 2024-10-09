# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InventoryWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6 import QtWidgets, QtGui

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 527)
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
        self.tableWidget.setGeometry(QRect(50, 80, 561, 281))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(8)
        font.setBold(True)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 490, 61, 26))
        self.addItemButton = QPushButton(Form)
        self.addItemButton.setObjectName(u"addItemButton")
        self.addItemButton.setGeometry(QRect(570, 400, 87, 26))
        self.editItemButton = QPushButton(Form)
        self.editItemButton.setObjectName(u"editItemButton")
        self.editItemButton.setGeometry(QRect(570, 440, 87, 26))
        self.removeItemButton = QPushButton(Form)
        self.removeItemButton.setObjectName(u"removeItemButton")
        self.removeItemButton.setGeometry(QRect(570, 480, 87, 26))
        font1 = QFont()
        font1.setPointSize(10)
        self.removeItemButton.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"InventoryScreen", None))
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
        self.addItemButton.setText(QCoreApplication.translate("Form", u"Add Item", None))
        self.editItemButton.setText(QCoreApplication.translate("Form", u"Edit Item", None))
        self.removeItemButton.setText(QCoreApplication.translate("Form", u"Remove Item", None))
    # retranslateUi

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.resize_and_center()


    def resize_and_center(self):
        # Define the initial window size
        window_width = 600
        window_height = 400
        self.resize(window_width, window_height)

        # Get the available screen geometry
        screen_geometry = QtGui.QScreen.availableGeometry(QApplication.primaryScreen())

        # Calculate the top-left corner position to center the window
        x = (screen_geometry.width() - window_width) // 2
        y = (screen_geometry.height() - window_height) // 2

        # Move the window to the calculated position
        self.move(x, y)

    #Event triggered by window resize, adjusts size and position of widgets
    def resizeEvent(self, event):
        # Get the current window width and height
        window_width = self.width()
        window_height = self.height()

        # Resize and position the table widget dynamically
        self.tableWidget.setGeometry(QRect(50, 80, window_width - 100, window_height - 300))
        self.adjustTableHeaderFont()

        # Resize and position the buttons dynamically
        button_width = 87
        button_height = 26
        button_x = window_width - button_width - 30  # Adjust the X position to stay on the right
        self.addItemButton.setGeometry(QRect(button_x, window_height - 180, button_width, button_height))
        self.editItemButton.setGeometry(QRect(button_x, window_height - 140, button_width, button_height))
        self.removeItemButton.setGeometry(QRect(button_x, window_height - 100, button_width, button_height))
        self.saveButton.setGeometry(QRect(10, window_height - 50, 100, button_height))  # Save button on the bottom-left

        # Call the parent class resizeEvent to ensure proper handling
        super().resizeEvent(event)

    #Adjusts tableWidget's horizontalHeader font size to fit current header size
    def adjustTableHeaderFont(self):
        header = self.tableWidget.horizontalHeader()

        # Iterate over each section (column) in the header
        for col in range(self.tableWidget.columnCount()):
            available_width = header.sectionSize(col)

            # Get the current font and start with a larger size
            font = self.tableWidget.font()

            # Measure the width of the text using QFontMetrics
            font_metrics = QtGui.QFontMetrics(font)
            header_text = self.tableWidget.horizontalHeaderItem(col).text()
            text_width = font_metrics.horizontalAdvance(header_text)

            # Reduce the font size if the text is too wide for the column
            while text_width > available_width - 10 and font.pointSize() > 5:
                font.setPointSize(font.pointSize() - 1)
                font_metrics = QtGui.QFontMetrics(font)
                text_width = font_metrics.horizontalAdvance(header_text)

            # Set the adjusted font for the header
            self.tableWidget.horizontalHeaderItem(col).setFont(font)
