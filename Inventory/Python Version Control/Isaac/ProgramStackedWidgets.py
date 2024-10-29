import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout
from InventoryScreen import InventoryScreen
from pathlib import Path
sys.path.append((Path(__file__).parent.parent.resolve() / 'Noah').resolve().__str__()) #Get files from Noah's folder
from login import LoginWindow as LoginScreen
from ui import CentralWidget as HomeScreen
from settings import SettingsWidget as SettingsScreen


# (Placeholder) Sales Screen Class
class SalesScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Sales Screen", self)
        layout.addWidget(self.label)
        self.setLayout(layout)

# MainWidget contains a StackedWidget, which allows easy switching of the displayed widget
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Constant home button at top of screen (remove this when all screens are finalized)
        self.homeButton = QPushButton("Go to Home", self)
        self.homeButton.clicked.connect(self.show_home_screen)

        # Create a QStackedWidget to manage different screens
        self.stackedWidget = QStackedWidget()
        self.setWindowTitle("Inventory Program")

        # Create layout to hold stacked widget
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.homeButton) # Remove this when all screens are finalized
        self.mainLayout.addWidget(self.stackedWidget)
        self.setLayout(self.mainLayout)

        # Add screens to widget
        self.setup_screens()

    # Creates screens, adds to StackedWidget, and sets initial screen
    # To add a new screen, follow the format:
    """
        (Step 1)
        # Create screens
        self.someScreen1 = ScreenConstructor(connect slots as needed)
        self.someScreen2 = ScreenConstructor(connect slots as needed)
        e.x. self.homeScreen = HomeScreen(self.show_inventory_screen, self.show_sales_screen) 
            connects signals/slots as defined in HomeScreen to MainWidget's functions
        
        (Step 2)
        # Add screens to the QStackedWidget
        self.stackedWidget.addWidget(self.someScreen1) 
            adds someScreen1 to stackedWidget at next index
            
        (Step 3)
        # Set the initial screen
        self.initialScreen = self.someScreen1
            will set the initial screen to someScreen1
    """
    def setup_screens(self):
        # Create screens
        self.homeScreen = HomeScreen(self.show_inventory_screen, self.show_sales_screen, self.show_login_screen, self.show_settings_screen)
        self.inventoryScreen = InventoryScreen(self.show_home_screen)
        self.salesScreen = SalesScreen()
        self.settingsScreen = SettingsScreen(self, self.show_home_screen)
        self.loginScreen = LoginScreen()

        # Add screens to the QStackedWidget
        self.stackedWidget.addWidget(self.loginScreen)  # Index 0
        self.stackedWidget.addWidget(self.homeScreen)  # Index 1
        self.stackedWidget.addWidget(self.inventoryScreen)  # Index 2
        self.stackedWidget.addWidget(self.salesScreen)  # Index 3
        self.stackedWidget.addWidget(self.settingsScreen)  # Index 4

        # Set the initial screen (Login screen)
        self.initialScreen = self.loginScreen
        self.stackedWidget.setCurrentWidget(self.initialScreen)

        # Connect login_success signal to display main content after login
        self.loginScreen.login_success.connect(self.show_home_screen)

    # Method to handle logout
    def logout(self):
        self.loginScreen.reload()
        #self.setWindowTitle("Login")  # Reset window title to "Login"

    # Changes the displayed widget to homeScreen
    def show_home_screen(self):
        self.stackedWidget.setCurrentWidget(self.homeScreen)
        #self.stackedWidget.setLayout(self.homeScreen.main_layout)

    # Changes the displayed widget to inventoryScreen
    def show_inventory_screen(self):
        self.stackedWidget.setCurrentWidget(self.inventoryScreen)

    # Changes the displayed widget to salesScreen
    def show_sales_screen(self):
        self.stackedWidget.setCurrentWidget(self.salesScreen)

    # Changes the displayed widget to settingsScreen
    def show_settings_screen(self):
        self.stackedWidget.setCurrentWidget(self.settingsScreen)

    # Changes the displayed widget to loginScreen
    # Refreshes login screen on use
    def show_login_screen(self):
        self.logout()
        self.stackedWidget.setCurrentWidget(self.loginScreen)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWidget = MainWidget()
    mainWidget.resize(800, 600)
    mainWidget.show()

    sys.exit(app.exec())

