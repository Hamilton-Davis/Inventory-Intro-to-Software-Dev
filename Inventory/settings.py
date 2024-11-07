from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, Signal, QSize, QRect
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, \
    QLineEdit, QMessageBox, QCheckBox, QGridLayout
from popups import confirmation_dialog  # Import confirmation dialog function
import dataUtils  # Import utility functions


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

        # Grid layout to align username and password sections
        grid_layout = QGridLayout()

        # ---------- Change Username Section ----------
        # Title for username section
        username_label = QLabel("Change Username", self)
        username_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(username_label, 0, 0)

        # Input for new username
        self.change_username_input = QLineEdit(self)
        self.change_username_input.setPlaceholderText("Enter new username")
        self.change_username_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.change_username_input, 1, 0)

        # Input for confirming username
        self.confirm_username_input = QLineEdit(self)
        self.confirm_username_input.setPlaceholderText("Confirm new username")
        self.confirm_username_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.confirm_username_input, 2, 0)

        # Button to trigger username change
        self.change_username_button = QPushButton("Change Username", self)
        self.change_username_button.setFixedSize(150, 40)
        self.change_username_button.clicked.connect(self.change_username)
        grid_layout.addWidget(self.change_username_button, 3, 0)

        # ---------- Change Password Section ----------
        # Title for password section
        password_label = QLabel("Change Password", self)
        password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(password_label, 0, 1)

        # Input for new password
        self.change_password_input = QLineEdit(self)
        self.change_password_input.setPlaceholderText("Enter new password")
        self.change_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.change_password_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.change_password_input, 1, 1)

        # Input for confirming password
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setPlaceholderText("Confirm new password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setFixedSize(200, 40)
        grid_layout.addWidget(self.confirm_password_input, 2, 1)

        # Show password checkbox
        self.show_password_checkbox = QCheckBox("Show Password", self)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        grid_layout.addWidget(self.show_password_checkbox, 3, 1)

        # Button to trigger password change, directly below checkbox
        self.change_password_button = QPushButton("Change Password", self)
        self.change_password_button.setFixedSize(150, 40)
        self.change_password_button.clicked.connect(self.change_password)
        grid_layout.addWidget(self.change_password_button, 4, 1)

        # Add the grid layout to the main layout
        self.main_layout.addLayout(grid_layout)

        # Spacer for layout structure
        self.main_layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ---------- Bottom Layout for Reset Button ----------
        bottom_layout = QHBoxLayout()

        # Spacer to align Reset button to the right
        bottom_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Reset to Default button
        self.reset_button = QPushButton("Reset to Default", self)
        self.reset_button.setFixedSize(150, 40)
        self.reset_button.clicked.connect(self.reset_to_default)
        bottom_layout.addWidget(self.reset_button)

        # Add bottom layout to main layout
        self.main_layout.addLayout(bottom_layout)

        # Set the main layout for the widget
        self.setLayout(self.main_layout)

        # ---------- Position Home Button at Top-Left Corner ----------
        self.home_button = QPushButton("Home", self)
        self.home_button.setFixedSize(75, 25)
        self.home_button.clicked.connect(self.back_callback)  # Callback to go to the home screen
        home_icon = QIcon("icons/home.svg")
        self.home_button.setIcon(home_icon)
        self.home_button.setGeometry(QRect(10, 20, 75, 40))

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
            # Confirmation prompt
            if not confirmation_dialog("Are you sure you want to change the username?", "Confirm Username Change"):
                # Clear the input fields
                self.change_username_input.clear()
                self.confirm_username_input.clear()
                return  # Exit if the user cancels

            self.user_data['username'] = new_username
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'])
            self.data_updated.emit()
            QMessageBox.information(self, "Success", f"Username changed successfully to {new_username}!")

            # Clear the input fields
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
            # Confirmation prompt
            if not confirmation_dialog("Are you sure you want to change the password?", "Confirm Password Change"):
                # Clear the input fields
                self.change_password_input.clear()
                self.confirm_password_input.clear()
                return  # Exit if the user cancels

            self.user_data['password'] = new_password
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'])
            self.data_updated.emit()
            QMessageBox.information(self, "Success", "Password changed successfully!")

            # Clear the input fields
            self.change_password_input.clear()
            self.confirm_password_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Passwords do not match!")

    # Method to reset credentials to default
    def reset_to_default(self):
        if not confirmation_dialog("Are you sure you want to change to default credentials?", "Confirm Default Credentials"):
            return  # Exit if the user cancels
        default_username = "admin"
        default_password = "password"
        self.user_data['username'] = default_username
        self.user_data['password'] = default_password
        dataUtils.save_user_data(default_username, default_password)
        self.data_updated.emit()
        QMessageBox.information(self, "Reset Successful",
                                "Credentials reset to default (username: admin, password: password).")
