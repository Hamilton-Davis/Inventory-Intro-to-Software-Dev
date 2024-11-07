from PySide6.QtWidgets import QWidget
from SalesWidgetDesigner import Ui_SalesWidget
from SalesPeriodWidget import SalesPeriodWidget

class SalesScreen(QWidget, Ui_SalesWidget):
    def __init__(self, switch_to_home):
        super().__init__()
        self.setupUi(self)
        self.salesPeriodWidget = SalesPeriodWidget()
        self.homeButton.clicked.connect(switch_to_home)

