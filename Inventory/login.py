from PySide6.QtWidgets import (
    QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog, QCheckBox
)

# Dictionary store default user credentials for the login system
user_credentials = {"admin": "password"}  # Default credentials (username: 'admin', password: 'password')


# Define LoginWindow class that inherits from QDialog (for login window interface)
class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login System")  # Set title of window
        self.setGeometry(100, 100, 400, 300)  # Define size and position of login window

        self.layout = QVBoxLayout()  # Create a vertical layout to stack widgets

        # Username field setup
        self.label_username = QLabel("Username:")  # Label for username field
        self.layout.addWidget(self.label_username)  # Add username label to layout
        self.entry_username = QLineEdit()  # QLineEdit for user to input username
        self.layout.addWidget(self.entry_username)  # Add username input field to layout

        # Password field setup
        self.label_password = QLabel("Password:")  # Label for password field
        self.layout.addWidget(self.label_password)  # Add password label to layout
        self.entry_password = QLineEdit()  # QLineEdit for user to input password
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)  # Set password input to hidden by default
        self.layout.addWidget(self.entry_password)  # Add password input field to layout

        # Checkbox to toggle password visibility
        self.show_password_checkbox = QCheckBox("Show Password")  # Checkbox to show/hide the password
        # Connect checkbox state change to toggle method
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        self.layout.addWidget(self.show_password_checkbox)  # Add checkbox to layout

        # Login button setup
        self.login_button = QPushButton("Login")  # Button for submitting login credentials
        self.login_button.clicked.connect(self.check_login)  # Connect button click event to check_login method
        self.layout.addWidget(self.login_button)  # Add login button to layout

        self.setLayout(self.layout)  # Set layout for window

    # Check for correct username and password
    def check_login(self):
        username = self.entry_username.text()  # Get username
        password = self.entry_password.text()  # Get password

        # Check if username exists and password matches
        if username in user_credentials and user_credentials[username] == password:
            QMessageBox.information(self, "Login Success", "Welcome!")  # Show success message
            self.accept()  # Close login dialog with success status
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")  # Show failure message

    # Toggle visibility of password field based on state of checkbox
    def toggle_password_visibility(self, state):

        # If checkbox checked, show password
        if state == 2:  # Qt.Checked is represented by value 2
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Normal)  # Show password
        else:
            self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)  # Hide password (replaces with dots)
