# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SalesPeriodWidgethsNXPJ.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_SalesPeriodWidget(object):
    def setupUi(self, SalesPeriodWidget):
        if not SalesPeriodWidget.objectName():
            SalesPeriodWidget.setObjectName(u"SalesPeriodWidget")
        SalesPeriodWidget.resize(265, 277)
        self.verticalLayout = QVBoxLayout(SalesPeriodWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.salesPeriodLabel = QLabel(SalesPeriodWidget)
        self.salesPeriodLabel.setObjectName(u"salesPeriodLabel")
        self.salesPeriodLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.salesPeriodLabel)

        self.fromDateEdit = QDateEdit(SalesPeriodWidget)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.fromDateEdit.setCalendarPopup(True)
        self.fromDateEdit.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.fromDateEdit.setDate(QDate(2000, 1, 1))

        self.verticalLayout.addWidget(self.fromDateEdit)

        self.toDateEdit = QDateEdit(SalesPeriodWidget)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.toDateEdit.setCalendarPopup(True)
        self.toDateEdit.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.toDateEdit.setDate(QDate(2000, 1, 31))

        self.verticalLayout.addWidget(self.toDateEdit)

        self.periodDaysLabel = QLabel(SalesPeriodWidget)
        self.periodDaysLabel.setObjectName(u"periodDaysLabel")

        self.verticalLayout.addWidget(self.periodDaysLabel)

        self.instructions = QTextEdit(SalesPeriodWidget)
        self.instructions.setObjectName(u"instructions")
        self.instructions.setAutoFillBackground(False)
        self.instructions.setReadOnly(True)

        self.verticalLayout.addWidget(self.instructions)

        self.logSalesButton = QPushButton(SalesPeriodWidget)
        self.logSalesButton.setObjectName(u"logSalesButton")
        icon = QIcon()
        icon.addFile(u"../Inventory/icons/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logSalesButton.setIcon(icon)

        self.verticalLayout.addWidget(self.logSalesButton)


        self.retranslateUi(SalesPeriodWidget)

        QMetaObject.connectSlotsByName(SalesPeriodWidget)
    # setupUi

    def retranslateUi(self, SalesPeriodWidget):
        SalesPeriodWidget.setWindowTitle(QCoreApplication.translate("SalesPeriodWidget", u"Form", None))
        self.salesPeriodLabel.setText(QCoreApplication.translate("SalesPeriodWidget", u"Sales Period", None))
        self.fromDateEdit.setDisplayFormat(QCoreApplication.translate("SalesPeriodWidget", u"MM/dd/yyyy", None))
        self.toDateEdit.setDisplayFormat(QCoreApplication.translate("SalesPeriodWidget", u"MM/dd/yyyy", None))
        self.periodDaysLabel.setText(QCoreApplication.translate("SalesPeriodWidget", u"Days in Period:", None))
        self.instructions.setPlaceholderText(QCoreApplication.translate("SalesPeriodWidget", u"Select a start and end date to log and analyze sales for the period. Default timespan is 1 week.", None))
        self.logSalesButton.setText(QCoreApplication.translate("SalesPeriodWidget", u"Log Sales", None))
    # retranslateUi

