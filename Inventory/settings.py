from PySide6.QtCore import Qt, Signal, QRect
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, \
    QLineEdit, QMessageBox, QCheckBox, QGridLayout

import dataUtils  # Import utility functions
from popups import confirmation_dialog  # Import confirmation dialog function


class SettingsWidget(QWidget):
    data_updated = Signal()  # Signal emitted when data is updated

    def __init__(self, parent, back_callback):
        super().__init__(parent)
        self.back_callback = back_callback
        self.user_data = dataUtils.load_user_data()  # Load user data at initialization
        self.init_ui()  # Initialize UI

    def init_ui(self):
        # Main layout for settings screen
        self.main_layout = QVBoxLayout(self)

        # Title label for settings screen
        self.title_label = QLabel("Settings", self)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # Spacer for layout structure
        self.main_layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Grid layout to align username, password, and hint/question sections
        grid_layout = QGridLayout()

        # ---------- Change Username Section ----------
        username_label = QLabel("Change Username", self)
        username_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(username_label, 0, 0)

        self.change_username_input = QLineEdit(self)
        self.change_username_input.setPlaceholderText("Enter new username")
        self.change_username_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.change_username_input, 1, 0)

        self.confirm_username_input = QLineEdit(self)
        self.confirm_username_input.setPlaceholderText("Confirm new username")
        self.confirm_username_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.confirm_username_input, 2, 0)

        self.change_username_button = QPushButton("Change Username", self)
        self.change_username_button.setFixedSize(150, 40)
        self.change_username_button.clicked.connect(self.change_username)
        grid_layout.addWidget(self.change_username_button, 3, 0)

        # ---------- Change Password Section ----------
        password_label = QLabel("Change Password", self)
        password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(password_label, 0, 1)

        self.change_password_input = QLineEdit(self)
        self.change_password_input.setPlaceholderText("Enter new password")
        self.change_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.change_password_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.change_password_input, 1, 1)

        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setPlaceholderText("Confirm new password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.confirm_password_input, 2, 1)

        self.show_password_checkbox = QCheckBox("Show Password", self)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        grid_layout.addWidget(self.show_password_checkbox, 3, 1)

        self.change_password_button = QPushButton("Change Password", self)
        self.change_password_button.setFixedSize(150, 40)
        self.change_password_button.clicked.connect(self.change_password)
        grid_layout.addWidget(self.change_password_button, 4, 1)

        # ---------- Change Hint/Question Section ----------
        hint_label = QLabel("Security Question", self)
        hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(hint_label, 0, 2)

        self.change_hint_input = QLineEdit(self)
        self.change_hint_input.setPlaceholderText("Enter a security question")
        self.change_hint_input.setFixedSize(200, 40)
        self.change_hint_input.setText(self.user_data.get("hint", ""))  # Pre-fill with the existing hint
        grid_layout.addWidget(self.change_hint_input, 1, 2)

        self.change_answer_input = QLineEdit(self)
        self.change_answer_input.setPlaceholderText("Enter answer")
        self.change_answer_input.setFixedSize(200, 40)
        self.change_answer_input.setText(self.user_data.get("answer", ""))  # Pre-fill with the existing answer
        grid_layout.addWidget(self.change_answer_input, 2, 2)

        self.change_hint_button = QPushButton("Change Security Question", self)
        self.change_hint_button.setFixedSize(150, 40)
        self.change_hint_button.clicked.connect(self.change_security_question)
        grid_layout.addWidget(self.change_hint_button, 3, 2)

        # Add the grid layout to the main layout
        self.main_layout.addLayout(grid_layout)

        # Spacer for layout structure
        self.main_layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ---------- Bottom Layout for Reset Button ----------
        bottom_layout = QHBoxLayout()
        bottom_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.reset_button = QPushButton("Reset to Default", self)
        self.reset_button.setFixedSize(150, 40)
        self.reset_button.clicked.connect(self.reset_to_default)
        bottom_layout.addWidget(self.reset_button)

        self.main_layout.addLayout(bottom_layout)

        # Set the main layout for the widget
        self.setLayout(self.main_layout)

        # ---------- Position Home Button at Top-Left Corner ----------
        self.home_button = QPushButton("Home", self)
        self.home_button.setFixedSize(75, 25)
        self.home_button.clicked.connect(self.on_home_button_click)
        home_icon = QIcon("icons/home.svg")
        self.home_button.setIcon(home_icon)
        self.home_button.setGeometry(QRect(10, 20, 75, 40))

        # Method to clear all input fields

    def clear_all_fields(self):
        self.change_username_input.clear()
        self.confirm_username_input.clear()
        self.change_password_input.clear()
        self.confirm_password_input.clear()
        self.change_hint_input.clear()
        self.change_answer_input.clear()

        # Method to handle home button click

    def on_home_button_click(self):
        # Clear all input fields when the Home button is clicked
        self.clear_all_fields()

        # Call the back callback to go back to the previous screen
        self.back_callback()

    # Method to toggle password visibility
    def toggle_password_visibility(self, state):
        if state == 2:
            self.change_password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.change_password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)

    # Method to handle username change
    def change_username(self):
        new_username = self.change_username_input.text()
        confirm_username = self.confirm_username_input.text()
        if not new_username or not confirm_username:
            QMessageBox.warning(self, "Error", "Please fill both fields.")
            return
        if new_username == confirm_username:
            if not confirmation_dialog("Are you sure you want to change the username?", "Confirm Username Change", QMessageBox.Question):
                self.change_username_input.clear()
                self.confirm_username_input.clear()
                return
            self.user_data['username'] = new_username
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'], self.user_data.get('hint'), self.user_data.get('answer'))
            self.data_updated.emit()
            QMessageBox.information(self, "Success", f"Username changed successfully to {new_username}!")
            self.change_username_input.clear()
            self.confirm_username_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Usernames do not match!")

    # Method to handle password change
    def change_password(self):
        new_password = self.change_password_input.text()
        confirm_password = self.confirm_password_input.text()
        if not new_password or not confirm_password:
            QMessageBox.warning(self, "Error", "Please fill both fields.")
            return
        if new_password == confirm_password:
            if not confirmation_dialog("Are you sure you want to change the password?", "Confirm Password Change", QMessageBox.Question):
                self.change_password_input.clear()
                self.confirm_password_input.clear()
                return
            self.user_data['password'] = new_password
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'], self.user_data.get('hint'), self.user_data.get('answer'))
            self.data_updated.emit()
            QMessageBox.information(self, "Success", "Password changed successfully!")
            self.change_password_input.clear()
            self.confirm_password_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Passwords do not match!")

    # Method to handle the security question change
    def change_security_question(self):
        new_hint = self.change_hint_input.text()
        new_answer = self.change_answer_input.text()
        if not new_hint or not new_answer:
            QMessageBox.warning(self, "Error", "Please fill both fields for the security question.")
            return

        self.user_data['hint'] = new_hint
        self.user_data['answer'] = new_answer
        dataUtils.save_user_data(self.user_data['username'], self.user_data['password'], new_hint, new_answer)
        self.data_updated.emit()
        QMessageBox.information(self, "Success", "Security question and answer updated!")

        self.change_hint_input.clear()
        self.change_answer_input.clear()

    # Method to reset credentials to default
    def reset_to_default(self):
        if not confirmation_dialog("Are you sure you want to change to default credentials?", "Confirm Default Credentials", QMessageBox.Question):
            return
        default_username = "admin"
        default_password = "password"
        self.user_data['username'] = default_username
        self.user_data['password'] = default_password
        self.user_data['hint'] = ""
        self.user_data['answer'] = ""
        dataUtils.save_user_data(default_username, default_password, "", "")
        self.data_updated.emit()
        QMessageBox.information(self, "Reset Successful", "Credentials reset to default.")

