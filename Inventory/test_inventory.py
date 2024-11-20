import unittest
from unittest.mock import MagicMock
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication
from inventory import InventoryScreen, DatabaseManager, HeaderIndex


class TestInventoryScreen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Start Qt event loop for testing

    def test_add_table_row(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)
        screen.add_table_row(["New Item", "Category C", 5.00, 7.00, 50])

        # Check if the new row was added
        self.assertEqual(screen.tableWidget.rowCount(), 1)
        self.assertEqual(screen.tableWidget.item(0, 0).text(), "New Item")

    def test_remove_table_row(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)
        screen.add_table_row(["Item A", "Category D", 10.00, 12.00, 150])

        # Remove the first row
        screen.remove_table_row(0)

        # Verify if the row was removed
        self.assertEqual(screen.tableWidget.rowCount(), 0)

    def test_valid_save_valid(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)
        screen.add_table_row(["Valid Item", "Category A", 10.00, 15.00, 100])

        # Call valid_save and check if it passes
        result, message = screen.valid_save()
        self.assertTrue(result)
        self.assertEqual(message, "")

    def test_valid_save_invalid_item_name(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)
        screen.add_table_row(["", "Category A", 10.00, 15.00, 100])

        # Call valid_save and check for the validation error for empty item name
        result, message = screen.valid_save()
        self.assertFalse(result)
        self.assertEqual(message, "Item names must be set before saving.")

    def test_valid_save_invalid_duplicate_item(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)
        screen.add_table_row(["Duplicate Item", "Category A", 10.00, 15.00, 100])
        screen.add_table_row(["Duplicate Item", "Category B", 20.00, 30.00, 200])

        # Call valid_save and check for the validation error for duplicate item names
        result, message = screen.valid_save()
        self.assertFalse(result)
        self.assertEqual(message, "Duplicate item name found: 'Duplicate Item'. \nEach item must have a unique name.")

    def test_search_table(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)
        screen.add_table_row(["Item 1", "Category A", 10.00, 15.00, 100])
        screen.add_table_row(["Item 2", "Category B", 20.00, 30.00, 200])

        # Perform search and filter the rows
        screen.searchKeyBar.setText("Item 1")
        screen.search_table()

        # Verify that only "Item 1" is visible
        self.assertTrue(screen.tableWidget.isRowHidden(1))  # "Item 2" should be hidden

    def test_enable_table_row_editing(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)
        screen.add_table_row(["Editable Item", "Category A", 10.00, 15.00, 100])

        # Enable editing for the first row
        screen.enable_table_row_editing(0)

        # Verify that the row is editable
        item = screen.tableWidget.item(0, HeaderIndex.NAME.value)
        self.assertTrue(item.flags() & Qt.ItemIsEditable)

        # Check the background color of the item
        self.assertEqual(item.background().color(), QColor("light blue"))

    def test_resizeEvent(self):
        screen = InventoryScreen(show_home_screen=MagicMock())
        screen.setupUi(screen)

        # Simulate window resizing
        screen.resizeEvent(None)

        # Verify if the table widget's geometry is updated
        self.assertEqual(screen.tableWidget.geometry().width(), screen.width() - 20)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()  # Exit the event loop after tests


if __name__ == "__main__":
    unittest.main()
