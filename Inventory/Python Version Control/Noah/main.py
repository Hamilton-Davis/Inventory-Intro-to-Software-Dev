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

# Dictionary to store user credentials
user_credentials = {}


class SignupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label_new_username = QLabel("New Username:")
        self.layout.addWidget(self.label_new_username)
        self.entry_new_username = QLineEdit()
        self.layout.addWidget(self.entry_new_username)

        self.label_new_password = QLabel("New Password:")
        self.layout.addWidget(self.label_new_password)
        self.entry_new_password = QLineEdit()
        self.entry_new_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.entry_new_password)

        self.signup_button = QPushButton("Create Account")
        self.signup_button.clicked.connect(self.create_account)
        self.layout.addWidget(self.signup_button)

        self.setLayout(self.layout)

    def create_account(self):
        new_username = self.entry_new_username.text()
        new_password = self.entry_new_password.text()

        if new_username in user_credentials:
            QMessageBox.warning(self, "Signup Failed", "Username already exists.")
        else:
            user_credentials[new_username] = new_password
            QMessageBox.information(self, "Signup Success", "Account created successfully!")
            self.accept()  # Close the dialog


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login System")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        self.label_username = QLabel("Username:")
        self.layout.addWidget(self.label_username)
        self.entry_username = QLineEdit()
        self.layout.addWidget(self.entry_username)

        self.label_password = QLabel("Password:")
        self.layout.addWidget(self.label_password)
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.entry_password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)
        self.layout.addWidget(self.login_button)

        self.signup_button = QPushButton("Signup")
        self.signup_button.clicked.connect(self.open_signup)
        self.layout.addWidget(self.signup_button)

        self.setLayout(self.layout)

    def check_login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if username in user_credentials and user_credentials[username] == password:
            QMessageBox.information(self, "Login Success", "Welcome!")
            self.close()  # Close the login window
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    @staticmethod
    def open_signup(self):
        signup_dialog = SignupDialog()
        signup_dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
