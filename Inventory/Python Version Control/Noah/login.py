from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QCheckBox, QSpacerItem, QSizePolicy, QApplication
from PySide6.QtCore import Signal, Qt
import dataUtils  # Import utility functions


class LoginWindow(QWidget):
    login_success = Signal()  # Signal emitted when login is successful

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login System")  # Set window title
        self.setGeometry(100, 100, 400, 300)  # Set window size and position

        self.layout = QVBoxLayout(self)  # Main vertical layout for login screen
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center-align layout

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Add spacer to push content down

        self.title_label = QLabel("Sign in", self)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold;")  # Set title style
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center-align title
        self.layout.addWidget(self.title_label)  # Add title label to layout

        self.label_username = QLabel("Username:", self)
        self.layout.addWidget(self.label_username)  # Add username label to layout
        self.entry_username = QLineEdit(self)  # Username input field
        self.entry_username.setFixedSize(300, 50)  # Set size for input field
        self.layout.addWidget(self.entry_username)  # Add input field to layout

        self.label_password = QLabel("Password:", self)
        self.layout.addWidget(self.label_password)  # Add password label to layout
        self.entry_password = QLineEdit(self)  # Password input field
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)  # Mask password input
        self.entry_password.setFixedSize(300, 50)  # Set size for input field
        self.layout.addWidget(self.entry_password)  # Add input field to layout

        self.show_password_checkbox = QCheckBox("Show Password", self)  # Checkbox to toggle password visibility
        # Connect checkbox to toggle method
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        self.layout.addWidget(self.show_password_checkbox)  # Add checkbox to layout

        self.login_button = QPushButton("Login", self)  # Login button
        self.login_button.setFixedSize(200, 40)  # Set button size
        self.layout.addWidget(self.login_button)  # Add login button to layout
        self.login_button.clicked.connect(self.check_login)  # Connect button to login check method

        # Trigger login when pressing Enter in username and password field
        self.entry_username.returnPressed.connect(self.check_login)
        self.entry_password.returnPressed.connect(self.check_login)

        self.exit_button = QPushButton("Exit", self)  # Exit button
        self.exit_button.setFixedSize(200, 40)  # Set button size
        self.exit_button.clicked.connect(QApplication.quit)  # Connect button to quit application
        self.layout.addWidget(self.exit_button)  # Add exit button to layout

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Spacer at bottom of layout

        # Load stored user data (or defaults if file doesn't exist)
        self.user_data = dataUtils.load_user_data()  # Load user credentials

    def check_login(self):
        username = self.entry_username.text()  # Get entered username
        password = self.entry_password.text()  # Get entered password

        message_box = QMessageBox(self)  # Create message box for feedback
        message_box.setStyleSheet("QLabel{font-size: 14px;}")  # Set message box style

        # Check if entered username and password match stored credentials
        if username == self.user_data['username'] and password == self.user_data['password']:
            message_box.setIcon(QMessageBox.Information)  # Success icon
            message_box.setWindowTitle("Login Success")  # Success message title
            message_box.setText("Welcome!")  # Success message text
            message_box.setFixedSize(300, 150)  # Set message box size
            message_box.exec()  # Display message box

            # Disable input fields and buttons after successful login
            self.entry_username.setDisabled(True)
            self.entry_password.setDisabled(True)
            self.login_button.setDisabled(True)
            self.show_password_checkbox.setDisabled(True)

            self.login_success.emit()  # Emit login success signal
        else:
            # Show error message if login fails
            message_box.setIcon(QMessageBox.Warning)  # Warning icon
            message_box.setWindowTitle("Login Failed")  # Failure message title
            message_box.setText("Invalid username or password.")  # Failure message text
            message_box.setFixedSize(300, 150)  # Set message box size
            message_box.exec()  # Display message box

    # Toggle password visibility (checkbox)
    def toggle_password_visibility(self, state):
        if state == 2:  # If checkbox is checked, show password
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)

    def reset_login_fields(self):
        # Re-enable input fields and buttons for next login attempt
        self.entry_username.setDisabled(False)
        self.entry_password.setDisabled(False)
        self.login_button.setDisabled(False)
        self.show_password_checkbox.setDisabled(False)
        # Clear input fields
        self.entry_username.clear()
        self.entry_password.clear()
