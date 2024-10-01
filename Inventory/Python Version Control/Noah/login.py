import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QDialog
)

# Dictionary to store user credentials (Replace with text file later or we can fill dictionary on a file read later)
user_credentials = {}


class SignupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        # Username input
        self.label_new_username = QLabel("New Username:")
        self.layout.addWidget(self.label_new_username)
        self.entry_new_username = QLineEdit()
        self.layout.addWidget(self.entry_new_username)

        # Password input
        self.label_new_password = QLabel("New Password:")
        self.layout.addWidget(self.label_new_password)
        self.entry_new_password = QLineEdit()
        self.entry_new_password.setEchoMode(QLineEdit.EchoMode.Password)  # Make password hidden
        self.layout.addWidget(self.entry_new_password)

        # Signup button
        self.signup_button = QPushButton("Create Account")
        self.signup_button.clicked.connect(self.create_account)
        self.layout.addWidget(self.signup_button)

        self.setLayout(self.layout)


    # Handle signup button click
    def create_account(self):
        
        new_username = self.entry_new_username.text()
        new_password = self.entry_new_password.text()

        # Check if username already exists
        if new_username in user_credentials:
            QMessageBox.warning(self, "Signup Failed", "Username already exists.")
        else:
            # Add new username and password to credentials dictionary
            user_credentials[new_username] = new_password
            QMessageBox.information(self, "Signup Success", "Account created successfully!")
            self.accept()  # Close dialog


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login System")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        # Username input
        self.label_username = QLabel("Username:")
        self.layout.addWidget(self.label_username)
        self.entry_username = QLineEdit()
        self.layout.addWidget(self.entry_username)

        # Password input
        self.label_password = QLabel("Password:")
        self.layout.addWidget(self.label_password)
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)  # Make password hidden
        self.layout.addWidget(self.entry_password)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)
        self.layout.addWidget(self.login_button)

        # Signup button
        self.signup_button = QPushButton("Signup")
        self.signup_button.clicked.connect(self.open_signup)  # Connect to static method
        self.layout.addWidget(self.signup_button)

        self.setLayout(self.layout)

    
    # Handle login button click
    def check_login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        # Verify username and password against stored credentials (Not saved to text file yet)
        if username in user_credentials and user_credentials[username] == password:
            QMessageBox.information(self, "Login Success", "Welcome!")
            self.close()  # Close login window on successful login
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    
    # Open signup dialog
    @staticmethod
    def open_signup(self):
        signup_dialog = SignupDialog()
        signup_dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show main login window
    login_window = LoginWindow()
    login_window.show()
    
    sys.exit(app.exec())
