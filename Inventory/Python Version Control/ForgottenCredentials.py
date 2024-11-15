from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

import dataUtils

class ForgotCredentialsDialog(QDialog):
    def __init__(self, parent, user_data):
        super().__init__(parent)
        self.user_data = user_data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Forgot Credentials")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()

        # Check if the user has set a security question (hint)
        if not self.user_data['hint']:
            # Show a message if no security question is set
            QMessageBox.warning(self, "No Security Question", "You have not set a security question. Please set one in your settings.")
            self.reject()  # Close the dialog
            return

        # Display the security question
        self.question_label = QLabel(f"Security Question: {self.user_data['hint']}", self)
        layout.addWidget(self.question_label)

        # Input for the answer
        self.answer_input = QLineEdit(self)
        self.answer_input.setPlaceholderText("Enter your answer")
        layout.addWidget(self.answer_input)

        # Button to reset username or password
        self.reset_button = QPushButton("Reset Username/Password", self)
        self.reset_button.clicked.connect(self.reset_credentials)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)

    def reset_credentials(self):
        # Validate the answer
        answer = self.answer_input.text()
        if answer == self.user_data['answer']:
            # Correct answer, allow reset
            self.accept()  # Close the dialog
            self.reset_credentials_action()
        else:
            # Incorrect answer
            QMessageBox.warning(self, "Error", "Incorrect answer to the security question.")

    def reset_credentials_action(self):
        # This can either reset the password/username or return to the settings screen
        # For simplicity, let's reset the password to the default here
        self.user_data['password'] = "password"
        dataUtils.save_user_data(self.user_data['username'], self.user_data['password'], self.user_data['hint'], self.user_data['answer'])
        QMessageBox.information(self, "Success", "Your password has been reset to 'password'.")
