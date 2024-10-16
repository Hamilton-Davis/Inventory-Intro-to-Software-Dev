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
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # Event triggered by window resize, adjusts size and position of widgets
    def resizeEvent(self, event):
        # Get the current window width and height
        window_width = self.width()
        window_height = self.height()

        # Resize and position the table widget dynamically
        self.tableWidget.setGeometry(QRect(10, 60, window_width - 20, window_height - 120))

        # Resize and position the buttons dynamically
        button_width = 87
        button_height = 26
        button_spacing = 10  # Spacing between buttons

        # Button positions
        button_x_start = window_width - button_width - 10  # Adjust the X position to stay on the right side

        # Set positions for each button
        # Add, edit, and remove buttons on the bottom-right
        self.addItemButton.setGeometry(QRect(button_x_start - 200, window_height - 40, button_width, button_height))
        self.editItemButton.setGeometry(QRect(button_x_start - 100, window_height - 40, button_width, button_height))
        self.removeItemButton.setGeometry(QRect(button_x_start, window_height - 40, button_width, button_height))
        self.saveButton.setGeometry(QRect(10, window_height - 40, 71, button_height))  # Save button on the bottom-left

        # Resize and position the search bar and buttons at the top
        self.searchBar.setGeometry(QRect(230, 20, window_width - 290, button_height))  # Search bar on the top-right
        self.searchButton.setGeometry(QRect(window_width - 50, 20, 41, button_height))  # Search button on the top-right

        # Home button (fixed size)
        self.homeButton.setGeometry(QRect(10, 20, 71, button_height))  # Home button on the top-left

        # Call the parent class resizeEvent to ensure proper handling
        super().resizeEvent(event)