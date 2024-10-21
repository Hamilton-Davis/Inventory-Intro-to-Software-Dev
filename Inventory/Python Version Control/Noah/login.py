from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QCheckBox, QSpacerItem, QSizePolicy
from PySide6.QtCore import Signal, Qt

# Default credentials for login
user_credentials = {"admin": "password"}


class LoginWindow(QWidget):
    # Signal emitted when login is successful
    login_success = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login System")  # Set window title
        self.setGeometry(100, 100, 400, 300)  # Set window size and position

        # Main layout (vertical) to organize widgets
        self.layout = QVBoxLayout(self)
        # Align entire layout to center (horizontally and vertically)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add spacer at top to center the elements vertically
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Add title label for "Login"
        self.title_label = QLabel("Sign in", self)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold;")  # Set font and bold style for title
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center title label horizontally
        self.layout.addWidget(self.title_label)  # Add title label to layout

        # Username label and input field
        self.label_username = QLabel("Username:", self)
        self.layout.addWidget(self.label_username)  # Add username label to layout
        self.entry_username = QLineEdit(self)  # Create QLineEdit for username input
        self.entry_username.setFixedSize(300, 50)  # Set fixed size for username input field
        self.layout.addWidget(self.entry_username)  # Add username input field to layout

        # Password label and input field
        self.label_password = QLabel("Password:", self)
        self.layout.addWidget(self.label_password)  # Add password label to layout
        self.entry_password = QLineEdit(self)  # Create QLineEdit for password input
        # Set password field to hide input using echo mode
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.entry_password.setFixedSize(300, 50)  # Set fixed size for password input field
        self.layout.addWidget(self.entry_password)  # Add password input field to layout

        # Checkbox to show or hide password
        self.show_password_checkbox = QCheckBox("Show Password", self)
        # Connect checkbox state to toggle_password_visibility method
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        self.layout.addWidget(self.show_password_checkbox)  # Add checkbox to layout

        # Login button
        self.login_button = QPushButton("Login", self)
        self.login_button.setFixedSize(200, 40)  # Set fixed size for login button
        self.layout.addWidget(self.login_button)  # Add login button to layout
        self.login_button.clicked.connect(self.check_login)  # Connect login button's click event to check_login method

        # Connect Enter/Return key to trigger login
        self.entry_username.returnPressed.connect(self.check_login)  # Pressing enter on username triggers login
        self.entry_password.returnPressed.connect(self.check_login)  # Pressing enter on password triggers login

        # Add spacer at bottom to help center elements vertically
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # Check login credentials
    def check_login(self):
        username = self.entry_username.text()  # Get username input
        password = self.entry_password.text()  # Get password input

        # Create QMessageBox object for customization
        message_box = QMessageBox(self)
        message_box.setStyleSheet("QLabel{font-size: 14px;}")  # Set smaller font for message box

        # Check if entered username and password match default credentials
        if username in user_credentials and user_credentials[username] == password:
            # If login is successful, show success message
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle("Login Success")
            message_box.setText("Welcome!")
            message_box.setFixedSize(300, 150)  # Set smaller fixed size for message box
            message_box.exec()

            # Disable input fields, checkbox, and login button
            self.entry_username.setDisabled(True)
            self.entry_password.setDisabled(True)
            self.login_button.setDisabled(True)
            self.show_password_checkbox.setDisabled(True)

            # Disconnect returnPressed signal to prevent further login attempts with "Enter"
            self.entry_username.returnPressed.disconnect(self.check_login)
            self.entry_password.returnPressed.disconnect(self.check_login)

            self.login_success.emit()  # Signal for successful login
        else:
            # If login fails, show error message
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Login Failed")
            message_box.setText("Invalid username or password.")
            message_box.setFixedSize(300, 150)  # Set a smaller fixed size for the message box
            message_box.exec()

    # Toggle password visibility (checkbox)
    def toggle_password_visibility(self, state):
        if state == 2:  # If checkbox is checked, show password
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
