import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QPushButton, QHeaderView, QWidget
from PySide6.QtCore import QRect
from PySide6.QtGui import QFontMetrics, QFont, QScreen
from InventoryWidgetDesigner import Ui_Form


# Screen user sees when viewing/making changes to inventory
class InventoryScreen(QWidget, Ui_Form):
    def __init__(self):
        super(InventoryScreen, self).__init__()
        self.setupUi(self)


    # Event triggered by window resize, adjusts size and position of widgets
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
        self.saveButton.setGeometry(QRect(10, window_height - 100, 100, button_height))  # Save button on the bottom-left

        # Call the parent class resizeEvent to ensure proper handling
        super().resizeEvent(event)


    # Adjusts tableWidget's horizontalHeader font size to fit current header size
    def adjustTableHeaderFont(self):
        header = self.tableWidget.horizontalHeader()

        # Iterate over each section (column) in the header
        for col in range(self.tableWidget.columnCount()):
            available_width = header.sectionSize(col)

            # Get the current font and start with a larger size
            font = self.tableWidget.font()

            # Measure the width of the text using QFontMetrics
            font_metrics = QFontMetrics(font)
            header_text = self.tableWidget.horizontalHeaderItem(col).text()
            text_width = font_metrics.horizontalAdvance(header_text)

            # Reduce the font size if the text is too wide for the column
            while text_width > available_width - 10 and font.pointSize() > 5:
                font.setPointSize(font.pointSize() - 1)
                font_metrics = QFontMetrics(font)
                text_width = font_metrics.horizontalAdvance(header_text)

            # Set the adjusted font for the header
            self.tableWidget.horizontalHeaderItem(col).setFont(font)