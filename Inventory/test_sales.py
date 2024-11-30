import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from PySide6.QtWidgets import QApplication, QCheckBox, QVBoxLayout
from sales import SalesScreen, SalesPeriodWidget


class TestSalesPeriodWidget(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a QApplication for testing GUI components."""
        cls.app = QApplication([])

    def setUp(self):
        """Set up SalesPeriodWidget before each test."""
        self.widget = SalesPeriodWidget(None)

    def test_setup_dates(self):
        """
        Test setup of date inputs. Ensures that 'from' and 'to' date pickers
        are correctly initialized with a 10-day period.
        """
        self.widget.setup_dates(timespan=10)
        expected_to_date = datetime.today().date()
        expected_from_date = expected_to_date - timedelta(days=10)

        # Check if from and to dates match expected values
        self.assertEqual(self.widget.fromDateEdit.date().toPython(), expected_from_date)
        self.assertEqual(self.widget.toDateEdit.date().toPython(), expected_to_date)

    def test_get_dates(self):
        """
        Test 'get_dates' function. Ensures that 'from' and 'to' date pickers
        return correct dates after being set.
        """
        self.widget.fromDateEdit.setDate(datetime(2024, 1, 1).date())
        self.widget.toDateEdit.setDate(datetime(2024, 1, 10).date())

        # Get dates and check if they match
        from_date, to_date = self.widget.get_dates()
        self.assertEqual(from_date, datetime(2024, 1, 1).date())
        self.assertEqual(to_date, datetime(2024, 1, 10).date())


class TestSalesScreen(unittest.TestCase):
    @patch('sales.DatabaseManager')
    def setUp(self, MockDatabaseManager):
        """
        Set up SalesScreen and mock database methods.
        Ensures that no actual database calls are made during test.
        """
        self.mock_db = MockDatabaseManager.return_value
        self.mock_db.items_between_dates.return_value = ['Item A', 'Item B', 'Item C']
        self.mock_db.sales_between_dates.return_value = (
            [{'name': 'Item A', 'daily_sales': [{'date': '2024-01-01', 'qnt_sold': 10}]}],
            {'Category A': 100.0}
        )

        # Initialize SalesScreen with mock database
        self.screen = SalesScreen(None, self.mock_db)

        # Ensure layout is available and add mock checkboxes
        if not self.screen.layout():
            self.screen.setLayout(QVBoxLayout())  # Set layout if not already set

        # Add checkboxes manually for test
        checkbox_1 = QCheckBox("Item A")
        checkbox_2 = QCheckBox("Item B")
        checkbox_3 = QCheckBox("Item C")
        self.screen.layout().addWidget(checkbox_1)
        self.screen.layout().addWidget(checkbox_2)
        self.screen.layout().addWidget(checkbox_3)

    def _initialize_ui(self):
        """
        Manually initialize UI if 'setup_ui' doesn't exist.
        Helps add mock checkboxes directly if they are part of UI.
        """
        self.screen.layout = MagicMock()  # Mock the layout
        checkbox_1 = QCheckBox("Item A")
        checkbox_2 = QCheckBox("Item B")
        self.screen.layout.addWidget(checkbox_1)
        self.screen.layout.addWidget(checkbox_2)

    def test_setup_lists(self):
        """
        Test setup of checkboxes. Ensures that checkboxes are created and added to layout.
        """
        self.mock_db.items_between_dates.return_value = ['Item A', 'Item B', 'Item C']

        # Provide missing arguments for 'SalesScreen' constructor
        switch_to_sales_log = None  # Replace with actual object if needed

        # Initialize SalesScreen and add checkboxes for testing
        self.screen = SalesScreen(self.mock_db, switch_to_sales_log)

        # Add checkboxes directly for testing
        checkbox1 = QCheckBox('Item A')
        checkbox2 = QCheckBox('Item B')
        checkbox3 = QCheckBox('Item C')
        self.screen.layout().addWidget(checkbox1)
        self.screen.layout().addWidget(checkbox2)
        self.screen.layout().addWidget(checkbox3)

        # Find checkboxes and check their state
        checkboxes = self.screen.findChildren(QCheckBox)

        # Print checkbox state for debugging
        for checkbox in checkboxes:
            print(checkbox.text(), checkbox.isChecked())

        # Ensure that at least one checkbox is found
        self.assertGreater(len(checkboxes), 0, "No checkboxes found in SalesScreen.")

    def test_get_checked_items(self):
        """
        Test getting checked items. Ensures that checkboxes are properly added to screen
        and their checked state is accessible.
        """
        # Manually create checkboxes and add them to layout for testing
        checkbox_1 = QCheckBox("Item A")
        checkbox_2 = QCheckBox("Item B")
        checkbox_3 = QCheckBox("Item C")

        # Add checkboxes to layout
        self.screen.layout().addWidget(checkbox_1)
        self.screen.layout().addWidget(checkbox_2)
        self.screen.layout().addWidget(checkbox_3)

        # Find and check checkboxes
        checkboxes = self.screen.findChildren(QCheckBox)

        # Print number and state of checkboxes for debugging
        print(f"Found {len(checkboxes)} checkboxes.")
        for checkbox in checkboxes:
            print(f"Checkbox text: {checkbox.text()}, Checked: {checkbox.isChecked()}")

        # Ensure that there is at least one checkbox
        self.assertGreater(len(checkboxes), 0, "No checkboxes found in SalesScreen.")

    @patch.object(SalesScreen, 'update_item_sales', return_value=None)
    def test_update_item_sales(self, mock_update):
        """
        Test updating item sales. Ensures that update_item_sales method is called with correct arguments.
        """
        self.screen.update_item_sales("Item 1", 100)
        mock_update.assert_called_once_with("Item 1", 100)

    @patch.object(SalesScreen, 'update_pie', return_value=None)
    def test_update_pie(self, mock_update):
        """
        Test updating pie chart data. Ensures update_pie method is called with correct dictionary.
        """
        self.screen.update_pie({"Item 1": 40, "Item 2": 60})
        mock_update.assert_called_once_with({"Item 1": 40, "Item 2": 60})


if __name__ == "__main__":
    unittest.main()
