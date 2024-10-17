from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QApplication


# Define CentralWidget class (inherit from QWidget)
class CentralWidget(QWidget):
    def __init__(self, switch_to_inventory, switch_to_sales, switch_to_settings):
        super().__init__()
        self.switch_to_inventory = switch_to_inventory
        self.switch_to_sales = switch_to_sales
        self.switch_to_settings = switch_to_settings
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
        button1.clicked.connect(self.switch_to_inventory)

        button2 = QPushButton("Sales Analysis", self)
        button2.setFixedSize(150, 150)
        button2.move(450, 390)
        button2.clicked.connect(self.switch_to_sales)

        button3 = QPushButton("Settings", self)
        button3.setFixedSize(150, 150)
        button3.move(750, 390)
        button3.clicked.connect(self.switch_to_settings)

        button4 = QPushButton("Exit", self)
        button4.setFixedSize(75, 75)
        button4.move(1000, 700)
        button4.clicked.connect(self.exit)

    def exit(self):
        print("Closing Application")
        QApplication.quit()

    # Event triggered by window resize, adjusts size and position of widgets
    def resizeEvent(self, event):
        # Get the current window width and height
        window_width = self.width()
        window_height = self.height()
        button_width = 150

        # Button positions
        button_x_start = window_width - button_width - 10
