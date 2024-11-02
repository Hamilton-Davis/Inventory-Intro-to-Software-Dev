from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, \
    QLineEdit, QMessageBox, QCheckBox
from PySide6.QtCore import Qt, Signal
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
        self.main_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Horizontal layout to hold username and password sections
        horizontal_layout = QHBoxLayout()

        # Set a fixed width for consistency across both sections
        section_width = 300

        # ---------- Change Username Section ----------
        username_layout = QVBoxLayout()

        # Spacer to adjust alignment with password section
        username_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Title for username change section
        username_label = QLabel("Change Username", self)
        username_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        username_layout.addWidget(username_label)

        # Input for new username
        self.change_username_input = QLineEdit(self)
        self.change_username_input.setPlaceholderText("Enter new username")
        self.change_username_input.setFixedSize(section_width, 50)
        username_layout.addWidget(self.change_username_input)

        # Input for confirming username
        self.confirm_username_input = QLineEdit(self)
        self.confirm_username_input.setPlaceholderText("Confirm new username")
        self.confirm_username_input.setFixedSize(section_width, 50)
        username_layout.addWidget(self.confirm_username_input)

        # Button to trigger username change
        self.change_username_button = QPushButton("Change Username", self)
        self.change_username_button.setFixedSize(150, 40)
        self.change_username_button.clicked.connect(self.change_username)
        username_layout.addWidget(self.change_username_button)

        # Add username section to horizontal layout
        horizontal_layout.addLayout(username_layout)

        # Spacer between sections for alignment
        horizontal_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ---------- Change Password Section ----------
        password_layout = QVBoxLayout()

        # Title for password change section
        password_label = QLabel("Change Password", self)
        password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        password_layout.addWidget(password_label)

        # Input for new password
        self.change_password_input = QLineEdit(self)
        self.change_password_input.setPlaceholderText("Enter new password")
        self.change_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.change_password_input.setFixedSize(section_width, 50)
        password_layout.addWidget(self.change_password_input)

        # Input for confirming password
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setPlaceholderText("Confirm new password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setFixedSize(section_width, 50)
        password_layout.addWidget(self.confirm_password_input)

        # Checkbox to toggle password visibility, placed below confirm password
        self.show_password_checkbox = QCheckBox("Show Password", self)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        password_layout.addWidget(self.show_password_checkbox)

        # Button to trigger password change
        self.change_password_button = QPushButton("Change Password", self)
        self.change_password_button.setFixedSize(150, 40)
        self.change_password_button.clicked.connect(self.change_password)
        password_layout.addWidget(self.change_password_button)

        # Add password section to horizontal layout
        horizontal_layout.addLayout(password_layout)

        # Add horizontal layout (username and password sections) to main layout
        self.main_layout.addLayout(horizontal_layout)

        # Spacer for layout structure
        self.main_layout.addSpacerItem(QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Layout for back button and reset button
        bottom_layout = QHBoxLayout()
        bottom_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Reset to Default button
        self.reset_button = QPushButton("Reset to Default", self)
        self.reset_button.setFixedSize(150, 40)
        self.reset_button.clicked.connect(self.reset_to_default)
        bottom_layout.addWidget(self.reset_button)

        # Back button to return to previous screen
        self.back_button = QPushButton("Home", self)
        self.back_button.setFixedSize(75, 75)
        self.back_button.clicked.connect(self.back_callback)
        bottom_layout.addWidget(self.back_button)

        # Add bottom layout to main layout
        self.main_layout.addLayout(bottom_layout)

        self.setLayout(self.main_layout)  # Set layout for settings screen

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
            self.user_data['username'] = new_username
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'])
            self.data_updated.emit()
            QMessageBox.information(self, "Success", f"Username changed successfully to {new_username}!")
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
            self.user_data['password'] = new_password
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'])
            self.data_updated.emit()
            QMessageBox.information(self, "Success", "Password changed successfully!")
        else:
            QMessageBox.warning(self, "Error", "Passwords do not match!")

    # Method to reset credentials to default
    def reset_to_default(self):
        default_username = "admin"
        default_password = "password"
        self.user_data['username'] = default_username
        self.user_data['password'] = default_password
        dataUtils.save_user_data(default_username, default_password)
        self.data_updated.emit()
        QMessageBox.information(self, "Reset Successful",
                                "Credentials reset to default (username: admin, password: password).")
