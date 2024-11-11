from PySide6.QtCore import QRect, Qt, QDate, QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QHeaderView, QWidget, QTableWidgetItem, QTableWidget, QVBoxLayout, QDateEdit, QSpacerItem, \
    QSizePolicy, QHBoxLayout, QPushButton

import popups
import tablereader
from widgetdesigners import Ui_InventoryWidget


# Screen user sees when viewing/making changes to inventory
class InventoryScreen(QWidget, Ui_InventoryWidget):

    def __init__(self, switch_to_home):
        # Init ui
        super(InventoryScreen, self).__init__()
        self.setupUi(self)
        self.setup_table()
        self.searchKeyBar.textChanged.connect(self.searchKeyBar_textChanged)
        self.searchCategoryBar.textChanged.connect(self.searchCategoryBar_textChanged)

        # Connect buttons
        self.addItemButton.clicked.connect(self.add_table_row)
        self.editItemButton.clicked.connect(self.editItemButton_clicked)
        self.removeItemButton.clicked.connect(self.removeItemButton_clicked)
        self.saveButton.clicked.connect(self.saveButton_clicked)
        self.homeButton.clicked.connect(switch_to_home)  # Determines action by slot passed in constructor
        self.searchKeyBar.textChanged.connect(self.search_table)  # Connect search bars to the search function
        self.searchCategoryBar.textChanged.connect(self.search_table)

    # Imports data from an existing table into tableWidget
    def import_table(self):
        # Clear pre-set columns
        self.tableWidget.setColumnCount(0)

        table = tablereader.import_workbook()
        # Add columns titles
        for column in table[0]:
            self.add_table_column(column)

        # Add row data
        for row in table[1]:
            self.add_table_row(row)

    # Set table in default state
    def setup_table(self):
        # Import table data
        self.import_table()
        self.disable_table_editing()

        # Set table formatting
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)


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
            item.setBackground(QColor("light blue")) # Mark edited row with blue


    # Adds new row to table and enables editing of row
    # row_data is an optional parameter to set values of row
    def add_table_row(self, row_data=None):
        # Create new row
        row_index = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_index)

        # If row_data is provided, use its values; otherwise, default to "New Item" and blank spaces
        for column in range(self.tableWidget.columnCount()):
            # Determine the item value based on row_data or defaults
            isImport = False
            if row_data and column < len(row_data):
                isImport = True
                item_data = row_data[column]  # Use value from row_data if available
                if isinstance(item_data, (int, float)): # Convert numbers to strings
                    item_data = str(item_data)
            else:
                item_data = "New Item" if column == 0 else ""  # Default values

            # Add item to table
            item = QTableWidgetItem(item_data)
            self.tableWidget.setItem(row_index, column, item)
            if not isImport: item.setBackground(QColor("light green")) # Mark empty added row with green

    # Adds new column to table
    # Used for overwriting default columns with file
    def add_table_column(self, column_name=""):
        # Create new column
        column_index = self.tableWidget.columnCount()
        self.tableWidget.insertColumn(column_index)

        # Add column name
        item = QTableWidgetItem(column_name)
        self.tableWidget.setHorizontalHeaderItem(column_index,  item)


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
            #Get row indexes in reverse order to avoid changing indexes as rows are removed
            selected_rows = sorted(set(index.row() for index in self.tableWidget.selectedIndexes()), reverse=True)

            for row in selected_rows:
                self.remove_table_row(row)


    # Saves table widget's data to a .xlsx file
    def saveButton_clicked(self):
        wb = tablereader.export_table(self.tableWidget)

        ws = wb.active
        for row in ws.iter_rows(values_only=True):
            print(row)

        # ADD FUNCTION TO WRITE WORKBOOK TO FILE HERE


    def searchKeyBar_textChanged(self):
        # Changes formatting for placeholder vs. user text
        if not self.searchKeyBar.text() == "":
            # Remove italics from user text
            font = self.searchKeyBar.font()
            font.setItalic(False)
            self.searchKeyBar.setFont(font)
        else:
            # Add italics to placeholder text
            font = self.searchKeyBar.font()
            font.setItalic(True)
            self.searchKeyBar.setFont(font)

        self.search_table()

    def searchCategoryBar_textChanged(self):
        # Changes formatting for placeholder vs. user text
        if not self.searchCategoryBar.text() == "":
            # Remove italics from user text
            font = self.searchCategoryBar.font()
            font.setItalic(False)
            self.searchCategoryBar.setFont(font)
        else:
            # Add italics to placeholder text
            font = self.searchCategoryBar.font()
            font.setItalic(True)
            self.searchCategoryBar.setFont(font)

    # Searches tableWidget for item names containing user-input string
    def search_table(self):
        category_search = self.searchCategoryBar.text().lower()
        value_search = self.searchKeyBar.text().lower()

        # Step 1: Identify target column based on category input
        category_column_index = -1
        if category_search:
            for column in range(self.tableWidget.columnCount()):
                header_item = self.tableWidget.horizontalHeaderItem(column)
                if header_item and category_search in header_item.text().lower():
                    category_column_index = column
                    break

        matching_rows = set()

        # Step 2: Filter rows based on category column if specified
        if category_column_index != -1:
            # Search only within specific category column
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, category_column_index)
                if item and value_search in item.text().lower():
                    matching_rows.add(row)
        else:
            # Else, search for value across all columns
            for row in range(self.tableWidget.rowCount()):
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item and value_search in item.text().lower():
                        matching_rows.add(row)
                        break  # Move to next row as soon as a match is found

        # Step 3: Show or hide rows based on final filtered rows
        for row in range(self.tableWidget.rowCount()):
            if row in matching_rows:
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)

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
        searchBarGap = self.searchCategoryBar.geometry().right() - self.searchKeyBar.geometry().left() + 20
        categoryBarRight = self.searchCategoryBar.geometry().right()
        searchBarLength =  self.tableWidget.geometry().right() - self.searchKeyBar.geometry().left()

        # Set positions for each button
        # Add, edit, and remove buttons on the bottom-right
        self.addItemButton.setGeometry(QRect(button_x_start - 200, window_height - 40, button_width, button_height))
        self.editItemButton.setGeometry(QRect(button_x_start - 100, window_height - 40, button_width, button_height))
        self.removeItemButton.setGeometry(QRect(button_x_start, window_height - 40, button_width, button_height))
        self.saveButton.setGeometry(QRect(10, window_height - 40, 71, button_height))  # Save button on the bottom-left

        # Resize and position the search bar and buttons at the top
        self.searchKeyBar.setGeometry(QRect(categoryBarRight + searchBarGap, 20, searchBarLength, button_height))  # Search bar on the top-right

        # Call the parent class resizeEvent to ensure proper handling
        super().resizeEvent(event)


class CondensedSalesLog(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.top_layout = QHBoxLayout()
        top_spacer = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.top_layout.addItem(top_spacer)
        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("MM/dd/yyyy")
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.top_layout.addWidget(self.date_edit)
        self.main_layout.addLayout(self.top_layout)

        self.tableWidget = QTableWidget()
        self.setup_table()
        self.main_layout.addWidget(self.tableWidget)

        self.bottom_layout = QHBoxLayout()
        icon = QIcon()
        icon.addFile(u"icons/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_button = QPushButton(icon, "Save", self)
        self.save_button.clicked.connect(self.save_clicked)
        self.bottom_layout.addWidget(self.save_button)
        bottom_spacer = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.bottom_layout.addItem(bottom_spacer)
        self.main_layout.addLayout(self.bottom_layout)


    def setup_table(self):
        # Import table data
        self.import_table()

        # Set table formatting
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    # Imports items' name, category, and price
    def import_table(self):
        table = tablereader.import_workbook()

        # Get the index of the required columns
        item = table[0].index("Item")
        category = table[0].index("Category")
        price = table[0].index("Price")

        # Create rows and columns
        self.tableWidget.setRowCount(len(table[1]))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Item", "Category", "Price", "Quantity Sold"])

        # Add row data, lock "Item", "Category", and "Price" columns
        for row_index, row in enumerate(table[1]):
            item_cell = QTableWidgetItem(row[item])
            item_cell.setFlags(item_cell.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_index, 0, item_cell)

            category_cell = QTableWidgetItem(row[category])
            category_cell.setFlags(category_cell.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_index, 1, category_cell)

            price_cell = QTableWidgetItem(row[price])
            price_cell.setFlags(price_cell.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_index, 2, price_cell)

            quantity_sold_cell = QTableWidgetItem("0")
            self.tableWidget.setItem(row_index, 3, quantity_sold_cell)


    # Exports data from table
    def save_clicked(self):
        wb = tablereader.export_table(self.tableWidget)

        ws = wb.active
        for row in ws.iter_rows(values_only=True):
            print(row)
