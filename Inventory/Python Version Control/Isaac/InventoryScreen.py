from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QPushButton, QHeaderView, QWidget, QTableWidgetItem
from PySide6.QtCore import QRect, Qt, Signal
from InventoryWidgetDesigner import Ui_InventoryWidget


# Screen user sees when viewing/making changes to inventory
class InventoryScreen(QWidget, Ui_InventoryWidget):

    def __init__(self, switch_to_home):
        super(InventoryScreen, self).__init__()
        self.setupUi(self)
        self.setup_table()
        self.addItemButton.clicked.connect(self.add_table_row)
        self.editItemButton.clicked.connect(self.editItemButton_clicked)
        self.removeItemButton.clicked.connect(self.removeItemButton_clicked)
        self.homeButton.clicked.connect(switch_to_home) # Determines action by slot passed in constructor

    # Set table in default state
    def setup_table(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.disable_table_editing()

    # Disables editing of all rows and columns in table
    def disable_table_editing(self):
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable) # Removes editable flag from item (row, column)

    # Enables editing of selected row in table
    def enable_table_row_editing(self, row):
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            item.setFlags(item.flags() | Qt.ItemIsEditable) # Adds editable flag to item (row, column)

    # Adds new row to table and enables editing of row
    def add_table_row(self):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        newItem = QTableWidgetItem("New Item")
        self.tableWidget.setItem(row_count, 0, newItem)

    # Removes selected row from table
    def remove_table_row(self, row):
        self.tableWidget.removeRow(row)

    # Enables current row when user clicks editItemButton
    def editItemButton_clicked(self):
        self.enable_table_row_editing(self.tableWidget.currentRow())

    # Removes current row when user clicks removeItemButton
    def removeItemButton_clicked(self):
        self.remove_table_row(self.tableWidget.currentRow())

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