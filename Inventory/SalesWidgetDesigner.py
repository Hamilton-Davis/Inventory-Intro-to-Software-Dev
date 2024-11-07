# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SalesWidgetNMfkPB.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

from SalesPeriodWidget import SalesPeriodWidget

class Ui_SalesWidget(object):
    def setupUi(self, SalesWidget):
        if not SalesWidget.objectName():
            SalesWidget.setObjectName(u"SalesWidget")
        SalesWidget.resize(701, 484)
        self.salesPeriodWidget = SalesPeriodWidget(SalesWidget)
        self.salesPeriodWidget.setObjectName(u"salesPeriodWidget")
        self.salesPeriodWidget.setGeometry(QRect(470, 10, 221, 241))
        self.homeButton = QPushButton(SalesWidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 20, 80, 26))
        icon = QIcon()
        icon.addFile(u"../Inventory/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButton.setIcon(icon)
        self.itemSalesGraph = QWidget(SalesWidget)
        self.itemSalesGraph.setObjectName(u"itemSalesGraph")
        self.itemSalesGraph.setGeometry(QRect(10, 70, 271, 181))
        self.itemSalesOptionList = QListWidget(SalesWidget)
        self.itemSalesOptionList.setObjectName(u"itemSalesOptionList")
        self.itemSalesOptionList.setGeometry(QRect(290, 70, 101, 171))
        self.itemQntGraph = QWidget(SalesWidget)
        self.itemQntGraph.setObjectName(u"itemQntGraph")
        self.itemQntGraph.setGeometry(QRect(10, 290, 271, 181))
        self.itemQntOptionList = QListWidget(SalesWidget)
        self.itemQntOptionList.setObjectName(u"itemQntOptionList")
        self.itemQntOptionList.setGeometry(QRect(290, 290, 101, 171))
        self.categorySalesGraph = QWidget(SalesWidget)
        self.categorySalesGraph.setObjectName(u"categorySalesGraph")
        self.categorySalesGraph.setGeometry(QRect(420, 290, 271, 181))

        self.retranslateUi(SalesWidget)

        QMetaObject.connectSlotsByName(SalesWidget)
    # setupUi

    def retranslateUi(self, SalesWidget):
        SalesWidget.setWindowTitle(QCoreApplication.translate("SalesWidget", u"Form", None))
        self.homeButton.setText(QCoreApplication.translate("SalesWidget", u"Home", None))
    # retranslateUi

