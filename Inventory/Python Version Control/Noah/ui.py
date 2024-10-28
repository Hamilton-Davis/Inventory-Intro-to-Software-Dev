from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from settings import SettingsWidget  # Import settings screen


class CentralWidget(QWidget):
    def __init__(self, inventory_callback, sales_callback, logout_callback, settings_callback):
        super().__init__()  # Initialize parent QWidget
        # Initialize button references and layout containers
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
        self.exit_button_layout = None
        self.button_layout = None
        self.main_layout = None
        self.title_label = None
        self.logout_callback = logout_callback  # Callback for exit button
        self.inventory_callback = inventory_callback
        self.sales_callback = sales_callback
        self.settings_callback = settings_callback
        self.settings_widget = None  # Initialize settings widget reference
        self.init_ui()  # Call UI setup method

    def init_ui(self):
        # Create main vertical layout for widget
        self.main_layout = QVBoxLayout(self)

        # Create and configure title label
        self.title_label = QLabel("Main Menu", self)
        self.title_label.setFont(QFont("Arial", 60))  # Set font and size
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center align text
        self.main_layout.addWidget(self.title_label)  # Add title label to layout

        # Add spacer to push buttons down
        self.main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create horizontal layout for buttons
        self.button_layout = QHBoxLayout()

        # Initialize and configure buttons
        self.button1 = QPushButton("Check Inventory", self)
        self.button1.setFixedSize(200, 150)  # Set button size
        # Connect button click to message action (prints message to console)
        self.button1.clicked.connect(self.inventory_callback)
        self.button_layout.addWidget(self.button1)  # Add button to layout

        self.button2 = QPushButton("Sales Analysis", self)
        self.button2.setFixedSize(200, 150)
        self.button2.clicked.connect(self.sales_callback)
        self.button_layout.addWidget(self.button2)

        self.button3 = QPushButton("Settings", self)
        self.button3.setFixedSize(200, 150)
        self.button3.clicked.connect(self.settings_callback)  # Connect to show settings screen
        self.button_layout.addWidget(self.button3)

        # Add button layout to main layout
        self.main_layout.addLayout(self.button_layout)

        # Add spacer to push exit button down
        self.main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create layout for the logout button
        self.exit_button_layout = QHBoxLayout()
        self.exit_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Add left spacer
        self.button4 = QPushButton("Logout", self)  # Create logout button
        self.button4.setFixedSize(75, 75)  # Set button size
        self.button4.clicked.connect(self.logout_callback)  # Connect logout button to the logout method
        self.exit_button_layout.addWidget(self.button4)  # Add button to exit layout

        # Add exit button layout to main layout
        self.main_layout.addLayout(self.exit_button_layout)

    def show_settings(self):
        # Hide all main menu widgets (title and buttons)
        self.title_label.hide()
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.hide()

        # Create and display settings widget
        if not self.settings_widget:
            self.settings_widget = SettingsWidget(self, self.back_to_main_menu)  # Pass callback to return to main menu
            self.main_layout.addWidget(self.settings_widget)  # Add settings widget to layout

        self.settings_widget.show()  # Show settings widget

    def back_to_main_menu(self):
        # Hide settings widget and show main menu widgets (title and buttons)
        self.settings_widget.hide()
        self.title_label.show()  # Show title label
        self.button1.show()  # Show first button
        self.button2.show()  # Show second button
        self.button3.show()  # Show settings button
        self.button4.show()  # Show logout button

    @staticmethod  # Indicates this method not dependent on instance state
    # Function to handle button click actions by printing a message
    def message_action(message):
        print(message)
