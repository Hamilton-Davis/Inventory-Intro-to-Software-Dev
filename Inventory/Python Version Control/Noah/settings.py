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

        # ---------- Change Username Section ----------
        username_layout = QVBoxLayout()
        # Label for username change section
        username_label = QLabel("Change Username", self)
        username_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        username_layout.addWidget(username_label)

        # Input for new username
        self.change_username_input = QLineEdit(self)
        self.change_username_input.setPlaceholderText("Enter new username")
        self.change_username_input.setFixedSize(300, 50)
        username_layout.addWidget(self.change_username_input)

        # Input for confirming username
        self.confirm_username_input = QLineEdit(self)
        self.confirm_username_input.setPlaceholderText("Confirm new username")
        self.confirm_username_input.setFixedSize(300, 50)
        username_layout.addWidget(self.confirm_username_input)

        # Button to trigger username change
        self.change_username_button = QPushButton("Change Username", self)
        self.change_username_button.setFixedSize(150, 40)
        self.change_username_button.clicked.connect(self.change_username)
        username_layout.addWidget(self.change_username_button)

        # Add username section to horizontal layout
        horizontal_layout.addLayout(username_layout)

        # ---------- Change Password Section ----------
        password_layout = QVBoxLayout()
        # Label for password change section
        password_label = QLabel("Change Password", self)
        password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        password_layout.addWidget(password_label)

        # Input for new password
        self.change_password_input = QLineEdit(self)
        self.change_password_input.setPlaceholderText("Enter new password")
        self.change_password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Mask password input
        self.change_password_input.setFixedSize(300, 50)
        password_layout.addWidget(self.change_password_input)

        # Input for confirming password
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setPlaceholderText("Confirm new password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Mask password input
        self.confirm_password_input.setFixedSize(300, 50)
        password_layout.addWidget(self.confirm_password_input)

        # Checkbox to toggle password visibility
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
        self.main_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Back button layout (aligned to right side)
        self.back_button_layout = QHBoxLayout()
        self.back_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        # Back button to return to previous screen
        self.back_button = QPushButton("Home", self)
        self.back_button.setFixedSize(75, 75)
        self.back_button.clicked.connect(self.back_callback)
        self.back_button_layout.addWidget(self.back_button)
        self.main_layout.addLayout(self.back_button_layout)

        self.setLayout(self.main_layout)  # Set layout for settings screen

    # Method to toggle password visibility
    def toggle_password_visibility(self, state):
        print(f"Toggle state changed to: {state}")  # Debug

        # Show or mask password based on checkbox state
        if state == 2:  # If checked, show password
            self.change_password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            print("Passwords should now be visible")  # Debug
        else:  # If unchecked, mask password
            self.change_password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
            print("Passwords should now be masked")  # Debug

    # Method to handle username change
    def change_username(self):
        new_username = self.change_username_input.text()
        confirm_username = self.confirm_username_input.text()

        # Validation to ensure both fields are filled
        if not new_username or not confirm_username:
            QMessageBox.warning(self, "Error", "Please fill both fields.")
            return

        # Check if new username matches confirmation
        if new_username == confirm_username:
            self.user_data['username'] = new_username
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'])
            self.data_updated.emit()  # Emit signal to indicate data update
            QMessageBox.information(self, "Success", f"Username changed successfully to {new_username}!")
        else:
            QMessageBox.warning(self, "Error", "Usernames do not match!")

    # Method to handle password change
    def change_password(self):
        new_password = self.change_password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Validation to ensure both fields are filled
        if not new_password or not confirm_password:
            QMessageBox.warning(self, "Error", "Please fill both fields.")
            return

        # Check if new password matches confirmation
        if new_password == confirm_password:
            self.user_data['password'] = new_password
            dataUtils.save_user_data(self.user_data['username'], self.user_data['password'])
            self.data_updated.emit()  # Emit signal to indicate data update
            QMessageBox.information(self, "Success", "Password changed successfully!")
        else:
            QMessageBox.warning(self, "Error", "Passwords do not match!")
