import unittest
from PySide6.QtCore import Qt
from unittest.mock import MagicMock
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from settings import SettingsWidget


class TestSettingsWidget(unittest.TestCase):
    """Unit tests for the SettingsWidget."""

    @classmethod
    def setUpClass(cls):
        """Set up QApplication for the tests."""
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        """Tear down QApplication after all tests."""
        cls.app.quit()

    def setUp(self):
        """Setup before each test."""
        self.mock_parent = QWidget()  # Using a valid QWidget as the parent
        self.mock_back_callback = MagicMock()  # Mocking the back callback
        self.widget = SettingsWidget(parent=self.mock_parent, back_callback=self.mock_back_callback)

    def test_initialization(self):
        # Directly create the widget
        widget = SettingsWidget(parent=None, back_callback=None)

        # Call the `init_ui` method to simulate the widget's setup
        widget.init_ui()

    def test_reset_to_default(self):
        widget = SettingsWidget(parent=None, back_callback=None)
        widget.show()  # Ensure the widget is visible before checking
        self.assertTrue(widget.reset_button.isVisible())  # Check if the reset button is visible

    def test_submit_button_click(self):
        widget = SettingsWidget(parent=None, back_callback=None)
        # Example for testing username change input
        widget.change_username_input.setText("new_username")
        # Simulate button click for username change
        widget.change_username_button.click()
        self.assertEqual(widget.change_username_input.text(), "new_username")

    def test_empty_username_fields(self):
        """Test for handling empty username fields."""
        self.widget.change_username_input.clear()
        self.widget.confirm_username_input.clear()
        self.widget.change_username_button.click()
        # Assert that a warning is displayed
        QMessageBox.warning = MagicMock()
        self.widget.change_username()
        QMessageBox.warning.assert_called_once_with(self.widget, "Error", "Please fill both fields.")

    def test_non_matching_usernames(self):
        """Test for handling non-matching username inputs."""
        self.widget.change_username_input.setText("user1")
        self.widget.confirm_username_input.setText("user2")
        self.widget.change_username_button.click()
        # Assert that a warning is displayed for mismatched usernames
        QMessageBox.warning = MagicMock()
        self.widget.change_username()
        QMessageBox.warning.assert_called_once_with(self.widget, "Error", "Usernames do not match!")

    def test_password_visibility_toggle(self):
        """Test the toggle password visibility checkbox."""
        self.widget.change_password_input.setText("mypassword")
        self.widget.confirm_password_input.setText("mypassword")
        # Simulate checking the checkbox
        self.widget.show_password_checkbox.setCheckState(Qt.CheckState.Checked)
        self.assertEqual(self.widget.change_password_input.echoMode(), QLineEdit.EchoMode.Normal)
        self.assertEqual(self.widget.confirm_password_input.echoMode(), QLineEdit.EchoMode.Normal)
        # Simulate unchecking the checkbox
        self.widget.show_password_checkbox.setCheckState(Qt.CheckState.Unchecked)
        self.assertEqual(self.widget.change_password_input.echoMode(), QLineEdit.EchoMode.Password)
        self.assertEqual(self.widget.confirm_password_input.echoMode(), QLineEdit.EchoMode.Password)

    def test_reset_to_default(self):
        """Test the reset to default functionality."""
        QMessageBox.information = MagicMock()
        confirmation_dialog = MagicMock(return_value=True)
        self.widget.reset_to_default()
        QMessageBox.information.assert_called_once_with(self.widget, "Reset Successful", "Credentials reset to default.")
        self.assertEqual(self.widget.user_data['username'], "admin")
        self.assertEqual(self.widget.user_data['password'], "password")

    def test_security_question_update(self):
        """Test updating the security question."""
        self.widget.change_hint_input.setText("What is your pet's name?")
        self.widget.change_answer_input.setText("Fluffy")
        confirmation_dialog = MagicMock(return_value=True)
        self.widget.change_security_question()
        self.assertEqual(self.widget.user_data['hint'], "What is your pet's name?")
        self.assertEqual(self.widget.user_data['answer'], "fluffy")

    def test_home_button_click(self):
        """Test the home button functionality."""
        self.widget.clear_all_fields = MagicMock()
        self.widget.back_callback = MagicMock()
        self.widget.on_home_button_click()
        self.widget.clear_all_fields.assert_called_once()
        self.widget.back_callback.assert_called_once()


if __name__ == "__main__":
    unittest.main()
