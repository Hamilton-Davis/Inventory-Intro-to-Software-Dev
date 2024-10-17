from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


# CentralWidget class for main menu screen
class CentralWidget(QWidget):
    def __init__(self, parent, exit_callback):
        super().__init__(parent)
        self.exit_callback = exit_callback  # Callback function for exit button
        self.init_ui()  # Initialize UI elements

    def init_ui(self):
        # Clear any existing widgets before adding new ones
        self.clear()

        # Create main vertical layout that will hold all elements
        main_layout = QVBoxLayout(self)

        # Title Label at the top (centered)
        title_label = QLabel("Inventory Management", self)  # Create title label
        title_label.setFont(QFont("Arial", 60))  # Set font style and size
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center label horizontally in layout
        main_layout.addWidget(title_label)  # Add title label to main layout

        # Spacer to add space between title and buttons
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create horizontal layout to organize buttons in row
        button_layout = QHBoxLayout()

        # Inventory button
        button1 = QPushButton("Check Inventory", self)  # Create "Check Inventory" button
        button1.setFixedSize(150, 150)  # Set fixed size for button
        # Connect button click to message action (prints message to console)
        button1.clicked.connect(lambda: CentralWidget.message_action("Checking Inventory..."))
        button_layout.addWidget(button1)  # Add button to horizontal layout

        # Sales Analysis button
        button2 = QPushButton("Sales Analysis", self)
        button2.setFixedSize(150, 150)
        button2.clicked.connect(lambda: CentralWidget.message_action("Performing Sales Analysis..."))
        button_layout.addWidget(button2)

        # Settings button
        button3 = QPushButton("Settings", self)
        button3.setFixedSize(150, 150)
        button3.clicked.connect(lambda: CentralWidget.message_action("Editing Settings..."))
        button_layout.addWidget(button3)

        # Add horizontal button layout to main vertical layout
        main_layout.addLayout(button_layout)

        # Spacer to add space below buttons (centers buttons vertically)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Layout for exit button, positioned at bottom right
        exit_button_layout = QHBoxLayout()
        # Add spacer to push exit button to right
        exit_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Exit button
        button4 = QPushButton("Exit", self)
        button4.setFixedSize(75, 75)
        button4.clicked.connect(self.exit_callback)
        exit_button_layout.addWidget(button4)

        # Add exit button layout to main vertical layout
        main_layout.addLayout(exit_button_layout)

        # Set main layout as layout for this widget
        self.setLayout(main_layout)

    # Clears all existing widgets in layout
    def clear(self):
        # Delete all child widgets to ensure a fresh UI
        for child in self.children():
            child.deleteLater()

    @staticmethod  # Indicates this method not dependent on instance state
    # Function to handle button click actions by printing a message
    def message_action(message):
        print(message)
