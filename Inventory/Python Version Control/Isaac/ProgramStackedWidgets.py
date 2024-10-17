import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem, QMainWindow
from PySide6.QtCore import QRect
from PySide6.QtGui import QFontMetrics
from InventoryScreen import InventoryScreen
from pathlib import Path
#Get files from Noah's folder
sys.path.append((Path(__file__).parent.parent.resolve() / 'Noah').resolve().__str__())

# Home Screen Class
class HomeScreen(QWidget):
    def __init__(self, switch_to_inventory, switch_to_sales):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Home Screen", self)
        layout.addWidget(self.label)

        # Buttons to switch screens
        self.inventoryButton = QPushButton("Go to Inventory", self)
        self.inventoryButton.clicked.connect(switch_to_inventory)
        layout.addWidget(self.inventoryButton)

        self.loginButton = QPushButton("Go to Sales", self)
        self.loginButton.clicked.connect(switch_to_sales)
        layout.addWidget(self.loginButton)

        self.setLayout(layout)


# Sales Screen Class
class SalesScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Sales Screen", self)
        layout.addWidget(self.label)
        self.setLayout(layout)


# Main Widget Class
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QStackedWidget to manage different screens
        self.stackedWidget = QStackedWidget()
        self.setWindowTitle("Inventory Program")

        # Create screens
        self.homeScreen = HomeScreen(self.show_inventory_screen, self.show_sales_screen)
        self.inventoryScreen = InventoryScreen(self.show_home_screen)
        self.salesScreen = SalesScreen()

        # Add screens to the QStackedWidget
        self.stackedWidget.addWidget(self.homeScreen)      # Index 0
        self.stackedWidget.addWidget(self.inventoryScreen) # Index 1
        self.stackedWidget.addWidget(self.salesScreen)     # Index 2

        # Set the initial screen (Home Screen)
        self.stackedWidget.setCurrentWidget(self.homeScreen)

        # Create layout to hold stacked widget
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.stackedWidget)
        self.setLayout(self.mainLayout)


    def show_home_screen(self):
        self.stackedWidget.setCurrentWidget(self.homeScreen)

    def show_inventory_screen(self):
        self.stackedWidget.setCurrentWidget(self.inventoryScreen)

    def show_sales_screen(self):
        self.stackedWidget.setCurrentWidget(self.salesScreen)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWidget = MainWidget()
    mainWidget.resize(800, 600)
    mainWidget.show()

    sys.exit(app.exec())
