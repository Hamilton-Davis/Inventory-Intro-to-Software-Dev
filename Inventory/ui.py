from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton, QLabel


# Define CentralWidget class (inherit from QWidget)
class CentralWidget(QWidget):
    def __init__(self, parent, exit_callback):
        super().__init__(parent)  # Call parent QWidget constructor
        self.exit_callback = exit_callback  # Store exit callback for later use
        self.init_ui()  # Initialize user interface

    # Initialize the UI elements and define their actions
    def init_ui(self):
        # Create and configure the title label
        title_label = QLabel("Inventory Management", self)  # Create a QLabel with the title text
        title_label.setFont(QFont("Arial", 60))  # Set font of title label
        title_label.move(160, 100)  # Move label to a specific position

        # Create the "Check Inventory" button
        button1 = QPushButton("Check Inventory", self)  # Create a QPushButton with label "Check Inventory"
        button1.setFixedSize(150, 150)  # Set fixed size of button
        button1.move(150, 390)  # Move button to specific position
        # Connect button click to message_action, displaying a message
        button1.clicked.connect(lambda: CentralWidget.message_action("Checking Inventory..."))

        button2 = QPushButton("Sales Analysis", self)
        button2.setFixedSize(150, 150)
        button2.move(450, 390)
        button2.clicked.connect(lambda: CentralWidget.message_action("Performing Sales Analysis..."))

        button3 = QPushButton("Settings", self)
        button3.setFixedSize(150, 150)
        button3.move(750, 390)
        button3.clicked.connect(lambda: CentralWidget.message_action("Editing Settings..."))

        button4 = QPushButton("Exit", self)
        button4.setFixedSize(75, 75)
        button4.move(1000, 700)
        button4.clicked.connect(self.exit_callback)

    @staticmethod  # Indicates this method not dependent on instance state
    # Function to handle button click actions by printing a message
    def message_action(message):
        print(message)
