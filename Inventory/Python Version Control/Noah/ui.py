from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton, QLabel


class CentralWidget(QWidget):
    def __init__(self, parent, exit_callback):
        super().__init__(parent)  # Call constructor of QWidget superclass
        self.exit_callback = exit_callback  # Store exit callback
        self.init_ui()   # Initialize user interface upon creation

    def init_ui(self):
        title_label = QLabel("Inventory Management", self)  # Title Label
        title_label.setFont(QFont("Arial", 60))  # Set font size and style
        title_label.move(160, 100)  # Position label

        # Create checking inventory button
        button1 = QPushButton("Check Inventory", self)
        button1.setFixedSize(150, 150)  # Set fixed size for the button
        button1.move(300, 390)  # Position the button
        button1.clicked.connect(lambda: CentralWidget.message_action("Checking Inventory..."))

        # Create sales analysis button
        button2 = QPushButton("Sales Analysis", self)
        button2.setFixedSize(150, 150)
        button2.move(600, 390)
        button2.clicked.connect(lambda: CentralWidget.message_action("Performing Sales Analysis..."))

        # Create exit button
        button3 = QPushButton("Exit", self)
        button3.setFixedSize(75, 75)
        button3.move(1000, 700)
        button3.clicked.connect(self.exit_callback)

    @staticmethod  # Indicates this method not dependent on instance state
    # Function to handle button click actions by printing a message
    def message_action(message):
        print(message)
