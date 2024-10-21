from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt


# Check buttons connect
def update_password():
    print("Update Password...")


# Check buttons connect
def update_username():
    print("Update Username...")


class SettingsWidget(QWidget):
    def __init__(self, parent, back_callback):
        super().__init__(parent)
        # Initialize button references and layout containers
        self.back_button = None
        self.back_button_layout = None
        self.update_password_button = None
        self.update_username_button = None
        self.title_label = None
        self.main_layout = None
        self.button_layout = None
        self.back_callback = back_callback  # Callback to return to main menu
        self.init_ui()

    def init_ui(self):
        # Create main vertical layout for settings screen
        self.main_layout = QVBoxLayout(self)

        # Create and configure title label
        self.title_label = QLabel("Settings", self)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # Add larger spacer at top to adjust vertical position of buttons
        self.main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create horizontal layout for buttons to be side by side
        self.button_layout = QHBoxLayout()

        # Create "Update Username" button
        self.update_username_button = QPushButton("Update Username", self)
        self.update_username_button.setFixedSize(200, 150)
        self.update_username_button.clicked.connect(update_username)  # Connect button to update_username function
        self.button_layout.addWidget(self.update_username_button)

        # Add space between two buttons
        self.button_layout.addSpacerItem(QSpacerItem(50, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Create the "Update Password" button
        self.update_password_button = QPushButton("Update Password", self)
        self.update_password_button.setFixedSize(200, 150)
        self.update_password_button.clicked.connect(update_password)  # Connect button to update_password function
        self.button_layout.addWidget(self.update_password_button)

        # Add horizontal spacers to position buttons in middle
        self.button_layout.insertStretch(0, 1)  # Add stretchable space before buttons
        self.button_layout.addStretch(1)  # Add stretchable space after buttons

        # Add horizontal button layout to main vertical layout
        self.main_layout.addLayout(self.button_layout)

        # Add smaller spacer below to push content upwards
        self.main_layout.addSpacerItem(QSpacerItem(200, 200, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create horizontal layout for "Home" button at bottom
        self.back_button_layout = QHBoxLayout()
        self.back_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.back_button = QPushButton("Home", self)
        self.back_button.setFixedSize(75, 75)
        self.back_button.clicked.connect(self.back_callback)
        self.back_button_layout.addWidget(self.back_button)
        self.main_layout.addLayout(self.back_button_layout)

        # Set main layout for widget
        self.setLayout(self.main_layout)
