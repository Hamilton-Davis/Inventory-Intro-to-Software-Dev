from PySide6.QtWidgets import QWidget

from widgetdesigners import Ui_SalesPeriodWidget


class SalesPeriodWidget(QWidget, Ui_SalesPeriodWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
