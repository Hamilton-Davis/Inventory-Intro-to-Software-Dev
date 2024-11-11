import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget

from inventory import InventoryScreen, SalesLogScreen
from login import LoginWindow as LoginScreen
from sales import SalesScreen
from settings import SettingsWidget as SettingsScreen
from ui import CentralWidget as HomeScreen


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
        self.home_screen = HomeScreen(self.show_inventory_screen, self.show_sales_screen, self.show_login_screen, self.show_settings_screen)
        self.inventory_screen = InventoryScreen(self.show_home_screen)
        self.sales_screen = SalesScreen(self.show_home_screen, self.show_sales_log_screen)
        self.settings_screen = SettingsScreen(self, self.show_home_screen)
        self.login_screen = LoginScreen()

        # Add screens to the QStackedWidget
        self.stackedWidget.addWidget(self.login_screen)  # Index 0
        self.stackedWidget.addWidget(self.home_screen)  # Index 1
        self.stackedWidget.addWidget(self.inventory_screen)  # Index 2
        self.stackedWidget.addWidget(self.sales_screen)  # Index 3
        self.stackedWidget.addWidget(self.settings_screen)  # Index 4

        # Set the initial screen (Login screen)
        self.initialScreen = self.login_screen
        self.stackedWidget.setCurrentWidget(self.initialScreen)

        # Connect login_success signal to display main content after login
        self.login_screen.login_success.connect(self.show_home_screen)

    # Method to handle logout
    def logout(self):
        self.login_screen.reload()
        #self.setWindowTitle("Login")  # Reset window title to "Login"

    # Changes the displayed widget to home_screen
    def show_home_screen(self):
        self.stackedWidget.setCurrentWidget(self.home_screen)
        #self.stackedWidget.setLayout(self.homeScreen.main_layout)

    # Changes the displayed widget to inventory_screen
    def show_inventory_screen(self):
        self.stackedWidget.setCurrentWidget(self.inventory_screen)

    # Changes the displayed widget to sales_screen
    def show_sales_screen(self):
        self.stackedWidget.setCurrentWidget(self.sales_screen)

    # Changes the displayed widget to settings_screen
    def show_settings_screen(self):
        self.stackedWidget.setCurrentWidget(self.settings_screen)

    # Changes the displayed widget to login_screen
    # Refreshes login screen on use
    def show_login_screen(self):
        self.logout()
        self.stackedWidget.setCurrentWidget(self.login_screen)

    # Changes displayed widget to sales_log_screen
    def show_sales_log_screen(self):
        # Create temporary sales_log_screen (destroyed when switched away from)
        sales_log_screen = SalesLogScreen(self.show_home_screen)
        self.stackedWidget.addWidget(sales_log_screen)
        self.stackedWidget.setCurrentWidget(sales_log_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWidget = MainWidget()
    mainWidget.resize(800, 600)
    mainWidget.show()

    sys.exit(app.exec())
