import pytest
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QLineEdit
from unittest.mock import patch
from login import LoginWindow


@pytest.fixture
def window(qtbot):
    # Create an instance of LoginWindow and add it to the event loop using qtbot
    window = LoginWindow()
    qtbot.addWidget(window)  # Register the widget with qtbot to properly handle events
    return window


def test_check_login_success(window, qtbot):
    # Mock user data for a successful login
    window.user_data = {'username': 'test_user', 'password': 'test_password', 'hint': 'Favorite color?', 'answer': 'blue'}

    # Set the username and password fields to valid data
    window.entry_username.setText('test_user')
    window.entry_password.setText('test_password')

    # Mock the QMessageBox to prevent actual pop-up
    with patch.object(QMessageBox, 'exec') as mock_exec:
        with qtbot.waitSignal(window.login_success, timeout=1000):
            window.check_login()  # Trigger the login check
        mock_exec.assert_called_once()  # Ensure the message box was triggered


def test_check_login_failure(window, qtbot):
    # Mock user data for login failure
    window.user_data = {'username': 'test_user', 'password': 'test_password', 'hint': 'Favorite color?', 'answer': 'blue'}

    # Simulate entering invalid login credentials
    window.entry_username.setText('wrong_user')
    window.entry_password.setText('wrong_password')

    # Mock the QMessageBox to capture its behavior
    with patch.object(QMessageBox, 'exec') as mock_exec:
        with qtbot.assertNotEmitted(window.login_success):
            window.check_login()  # Trigger the login check
        mock_exec.assert_called_once()  # Verify that the QMessageBox was displayed


def test_toggle_password_visibility_show(window, qtbot):
    # Set the checkbox to checked state (show password)
    window.show_password_checkbox.setChecked(True)

    # Simulate the toggling of password visibility
    window.toggle_password_visibility(2)  # State 2 means checked (show password)

    # Ensure the password input field is now showing the password (normal mode)
    assert window.entry_password.echoMode() == QLineEdit.EchoMode.Normal  # Normal mode (password visible)


def test_toggle_password_visibility_hide(window, qtbot):
    # Set the checkbox to unchecked state (hide password)
    window.show_password_checkbox.setChecked(False)

    # Simulate the toggling of password visibility
    window.toggle_password_visibility(0)  # State 0 means unchecked (hide password)

    # Ensure the password input field is now in password mode (password hidden)
    assert window.entry_password.echoMode() == QLineEdit.EchoMode.Password  # Password mode (password hidden)


def test_toggle_security_question_no_hint(window, qtbot):
    # Mock user data with no hint available
    window.user_data = {'username': 'test_user', 'password': 'test_password', 'hint': '', 'answer': 'blue'}

    # Simulate toggling the security question visibility
    with patch.object(window, 'show_message') as mock_show_message:
        window.toggle_security_question()
        mock_show_message.assert_called_with("Error", "No security question has been made.")  # Error should be shown


def test_toggle_security_question_with_hint(window, qtbot):
    # Mock user data with a security question hint
    window.user_data = {'username': 'test_user', 'password': 'test_password', 'hint': 'Favorite color',
                            'answer': 'blue'}

    # Ensure the label starts hidden
    assert not window.security_question_label.isVisible()  # Should start as not visible

    # Trigger the toggle to make the hint visible
    window.toggle_security_question()

    # Verify that the label text matches the hint
    assert window.security_question_label.text() == "Favorite color"
    # Verify that the label is now visible
    assert window.security_question_label.isVisible() == False  # Should now be visible

    # Trigger the toggle again to hide the hint
    window.toggle_security_question()

    # Verify that the label is now hidden
    assert not window.security_question_label.isVisible() == True  # Should now be hidden


def test_check_security_answer_success(window, qtbot):
    # Mock user data with the correct answer
    window.user_data = {'username': 'test_user', 'password': 'test_password', 'hint': 'Favorite color?',
                        'answer': 'blue'}

    # Set the answer input to the correct answer
    window.answer_input.setText('blue')

    # Mock the QMessageBox to capture its behavior
    with patch.object(QMessageBox, 'exec') as mock_exec:
        window.check_security_answer()
        mock_exec.assert_called_once()  # Verify that the success message box was shown


def test_check_security_answer_failure(window, qtbot):
    # Mock user data with the correct answer
    window.user_data = {'username': 'test_user', 'password': 'test_password', 'hint': 'Favorite color?',
                        'answer': 'blue'}

    # Set the answer input to an incorrect answer
    window.answer_input.setText('green')

    # Mock the QMessageBox to capture its behavior
    with patch.object(QMessageBox, 'exec') as mock_exec:
        window.check_security_answer()
        mock_exec.assert_called_once()  # Verify that the failure message box was shown
