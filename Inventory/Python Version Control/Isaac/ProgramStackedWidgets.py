import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem, QMainWindow
from PySide6.QtCore import QRect
from PySide6.QtGui import QFontMetrics
from InventoryScreen import InventoryScreen

# Home Screen Class
class HomeScreen(QWidget):
    def __init__(self, switch_to_inventory, switch_to_login):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Home Screen", self)
        layout.addWidget(self.label)

        # Buttons to switch screens
        self.inventoryButton = QPushButton("Go to Inventory", self)
        self.inventoryButton.clicked.connect(switch_to_inventory)
        layout.addWidget(self.inventoryButton)

        self.loginButton = QPushButton("Go to Login", self)
        self.loginButton.clicked.connect(switch_to_login)
        layout.addWidget(self.loginButton)

        self.setLayout(layout)

# Login Screen Class
class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Login Screen", self)
        layout.addWidget(self.label)
        self.setLayout(layout)

# Main Widget Class
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QStackedWidget to manage different screens
        self.stackedWidget = QStackedWidget()

        # Create instances of your screens
        self.homeScreen = HomeScreen(self.showInventoryScreen, self.showLoginScreen)
        self.inventoryScreen = InventoryScreen()
        self.loginScreen = LoginScreen()

        # Add screens to the QStackedWidget
        self.stackedWidget.addWidget(self.homeScreen)      # Index 0
        self.stackedWidget.addWidget(self.inventoryScreen) # Index 1
        self.stackedWidget.addWidget(self.loginScreen)     # Index 2

        # Set the initial screen (Home Screen)
        self.stackedWidget.setCurrentWidget(self.homeScreen)

        # Create a main layout to hold the stacked widget
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.stackedWidget)
        self.setLayout(mainLayout)

    def showHomeScreen(self):
        """ Switch to the Home Screen """
        self.stackedWidget.setCurrentWidget(self.homeScreen)

    def showInventoryScreen(self):
        """ Switch to the Inventory Screen """
        self.stackedWidget.setCurrentWidget(self.inventoryScreen)

    def showLoginScreen(self):
        """ Switch to the Login Screen """
        self.stackedWidget.setCurrentWidget(self.loginScreen)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Now the main widget is a QWidget
    mainWidget = MainWidget()
    mainWidget.resize(800, 600)
    mainWidget.show()

    app.exec()
