from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget,
    QCheckBox, QSpacerItem, QSizePolicy, QApplication
)

import dataUtils  # Import utility functions


class LoginWindow(QWidget):
    login_success = Signal()  # Signal emitted when login is successful
    logout_request = Signal()  # Signal emitted when logout is requested

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login System")  # Set window title
        self.setGeometry(100, 100, 400, 300)  # Set window size and position

        # Load stored user data (or defaults if file doesn't exist)
        self.user_data = dataUtils.load_user_data()  # Move this line here

        self.layout = QVBoxLayout(self)  # Main vertical layout for login screen
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center-align layout

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Spacer

        # Title
        self.title_label = QLabel("Sign in", self)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Username field
        self.label_username = QLabel("Username:", self)
        self.layout.addWidget(self.label_username)
        self.entry_username = QLineEdit(self)
        self.entry_username.setFixedSize(300, 50)
        self.layout.addWidget(self.entry_username)

        # Password field
        self.label_password = QLabel("Password:", self)
        self.layout.addWidget(self.label_password)
        self.entry_password = QLineEdit(self)
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.entry_password.setFixedSize(300, 50)
        self.layout.addWidget(self.entry_password)

        # Show password checkbox
        self.show_password_checkbox = QCheckBox("Show Password", self)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        self.layout.addWidget(self.show_password_checkbox)

        # Login button
        self.login_button = QPushButton("Login", self)
        self.login_button.setFixedSize(300, 40)
        self.login_button.clicked.connect(self.check_login)
        self.layout.addWidget(self.login_button)

        # Forgot button
        self.forgot_button = QPushButton("Forgot Username or Password", self)
        self.forgot_button.setFixedSize(300, 40)
        self.forgot_button.clicked.connect(self.toggle_security_question)
        self.layout.addWidget(self.forgot_button)

        # Security question widgets (hidden by default)
        self.security_question_label = QLabel(self.user_data.get('hint', 'No hint available'), self)  # Fix this line
        self.security_question_label.hide()
        self.layout.addWidget(self.security_question_label)

        self.answer_input = QLineEdit(self)
        self.answer_input.setFixedSize(300, 50)
        self.answer_input.hide()
        self.layout.addWidget(self.answer_input)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setFixedSize(300, 40)
        self.submit_button.hide()
        self.submit_button.clicked.connect(self.check_security_answer)
        self.layout.addWidget(self.submit_button)

        # Exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setFixedSize(300, 40)
        self.exit_button.clicked.connect(QApplication.quit)
        self.layout.addWidget(self.exit_button)

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def check_login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        message_box = QMessageBox(self)
        message_box.setStyleSheet("QLabel{font-size: 14px;}")

        if username == self.user_data['username'] and password == self.user_data['password']:
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle("Login Success")
            message_box.setText("Welcome!")
            message_box.setFixedSize(300, 150)
            message_box.exec()

            self.entry_username.clear()
            self.entry_password.clear()
            self.answer_input.clear()

            self.login_success.emit()  # Emit success signal
        else:
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Login Failed")
            message_box.setText("Invalid username or password.")
            message_box.setFixedSize(300, 150)
            message_box.exec()

    def toggle_password_visibility(self, state):
        if state == 2:
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)

    def toggle_security_question(self):
        # Check if a security question has been set
        if not self.user_data.get('hint'):
            self.show_message("Error", "No security question has been made.")
            return  # Prevent further actions if no security question exists

        # Proceed with showing/hiding the security question and answer fields
        visible = self.security_question_label.isVisible()
        self.security_question_label.setVisible(not visible)
        self.answer_input.setVisible(not visible)
        self.submit_button.setVisible(not visible)

    def check_security_answer(self):
        # Check if a security question has been set
        if not self.user_data.get('hint'):
            self.show_message("Error", "No security question has been made.")
            return  # Prevent further actions if no security question exists

        if self.answer_input.text() == self.user_data['answer']:  # Validate with actual answer
            self.show_message("Security Question", "Welcome! Please go to settings to update username/password.")
            self.entry_username.clear()
            self.entry_password.clear()
            self.answer_input.clear()
            self.login_success.emit()  # Emit success signal
        else:
            self.show_message("Security Question", "Incorrect answer. Try again.")

    def show_message(self, title, message):
        message_box = QMessageBox(self)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.setFixedSize(300, 150)
        message_box.exec()

    def reset_login_fields(self):
        """Reset login input fields and any other related UI elements."""
        self.entry_username.clear()
        self.entry_password.clear()
        self.entry_username.setEnabled(True)
        self.entry_password.setEnabled(True)
        self.login_button.setEnabled(True)
        self.show_password_checkbox.setChecked(False)
        self.show_password_checkbox.setEnabled(True)
        self.security_question_label.hide()
        self.answer_input.hide()
        self.submit_button.hide()

    def reload(self):
        """Reload the login screen and reset user data."""
        self.reset_login_fields()  # Reset all fields
        self.user_data = dataUtils.load_user_data()  # Reload user data

        # Update the security question label with the new hint
        self.security_question_label.setText(self.user_data.get('hint', 'No hint available'))
        self.security_question_label.hide()  # Ensure it's hidden initially

        # Optionally, clear the answer field
        self.answer_input.clear()

    def logout(self):
        """Handle user logout and reset the login screen."""
        # Clear login fields
        self.entry_username.clear()
        self.entry_password.clear()
        self.entry_username.setEnabled(True)
        self.entry_password.setEnabled(True)
        self.login_button.setEnabled(True)
        self.show_password_checkbox.setChecked(False)
        self.show_password_checkbox.setEnabled(True)

        # Hide the security question fields
        self.security_question_label.hide()
        self.answer_input.hide()
        self.submit_button.hide()

        # Reload user data to ensure we have the latest security question and answer
        self.user_data = dataUtils.load_user_data()  # Reload user data to get the latest info

        # Update the security question label with the new hint
        self.security_question_label.setText(self.user_data.get('hint', 'No hint available'))

        # Optionally reset the answer field
        self.answer_input.clear()

        # Emit logout signal
        self.logout_request.emit()
