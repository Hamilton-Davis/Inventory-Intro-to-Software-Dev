from PySide6.QtWidgets import QHeaderView, QWidget, QTableWidgetItem
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QBrush, QColor
from InventoryWidgetDesigner import Ui_InventoryWidget
import popups
import tablereader

# Screen user sees when viewing/making changes to inventory
class InventoryScreen(QWidget, Ui_InventoryWidget):

    def __init__(self, switch_to_home):
        super(InventoryScreen, self).__init__()
        self.setupUi(self)
        self.setup_table()
        self.addItemButton.clicked.connect(self.add_table_row)
        self.editItemButton.clicked.connect(self.editItemButton_clicked)
        self.removeItemButton.clicked.connect(self.removeItemButton_clicked)
        self.saveButton.clicked.connect(self.saveButton_clicked)
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
                if item is None:  # If the cell is blank, create a new item
                    item = QTableWidgetItem("")
                    self.tableWidget.setItem(row, column, item)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable) # Removes editable flag from item (row, column)

    # Enables editing of selected row in table
    def enable_table_row_editing(self, row):
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            if item is None:  # If the cell is blank, create a new item
                item = QTableWidgetItem("")
                self.tableWidget.setItem(row, column, item)
            item.setFlags(item.flags() | Qt.ItemIsEditable) # Adds editable flag to item (row, column)
            item.setBackground(QBrush(QColor("light blue"))) # Mark edited row with blue

    # Adds new row to table and enables editing of row
    def add_table_row(self):
        # Create new row
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)

        # Create first cell
        item = QTableWidgetItem("New Item")
        self.tableWidget.setItem(row_count, 0, item)
        item.setBackground(QBrush(QColor("light green"))) # Mark added row with green

        # Fill remaining cells with blank spaces
        for column in range(1, self.tableWidget.columnCount()):
            item = QTableWidgetItem("")
            self.tableWidget.setItem(row_count, column, item)
            item.setBackground(QBrush(QColor("light green"))) # Mark added row with green

    # Removes selected row from table
    def remove_table_row(self, row):
        self.tableWidget.removeRow(row)

    # Enables editing of selected rows when user clicks editItemButton
    def editItemButton_clicked(self):
        for index in self.tableWidget.selectedIndexes():
            self.enable_table_row_editing(index.row())

    # Removes selected rows when user clicks removeItemButton
    def removeItemButton_clicked(self):
        if popups.delete_confirmation_dialog():
            for index in self.tableWidget.selectedIndexes():
                self.remove_table_row(index.row())

    # Saves table widget's data to a .xlsx file
    def saveButton_clicked(self):
        wb = tablereader.export_table(self.tableWidget)

        ws = wb.active
        for row in ws.iter_rows(values_only=True):
            print(row)

        # ADD FUNCTION TO WRITE WORKBOOK TO FILE HERE

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