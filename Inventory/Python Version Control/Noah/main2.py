import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from ui import CentralWidget  # Import main UI for after login
from login import LoginWindow  # Import login screen UI
import dataUtils  # Import utility functions to load/save user data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")  # Set initial window title to "Login"

        # Main container widget that holds screens (Login and Main UI)
        self.container_widget = QWidget(self)
        self.layout = QVBoxLayout(self.container_widget)  # Vertical layout to hold login and main UI widgets
        self.setCentralWidget(self.container_widget)  # Set container widget as central widget of main window

        # Create login window (visible initially)
        self.login_window = LoginWindow(self)
        self.layout.addWidget(self.login_window)  # Add login window to layout

        # Create main content (hidden initially until after login)
        self.central_widget = CentralWidget(self, self.exit_application)
        self.central_widget.hide()  # Hide main content until login is successful
        self.layout.addWidget(self.central_widget)  # Add main content widget to layout

        # Connect login_success signal to display main content after login
        self.login_window.login_success.connect(self.show_main_menu)

    # Method to show main content after successful login
    def show_main_menu(self):
        self.login_window.hide()  # Hide login window after successful login
        self.central_widget.show()  # Show main content (central widget)
        self.setWindowTitle("Inventory Management")  # Update window title to "Inventory Management"

    # Method to handle logout and go back to login screen
    def logout(self):
        self.central_widget.hide()  # Hide central widget (main content)
        self.login_window.show()  # Show login window again
        self.setWindowTitle("Login")  # Reset window title to "Login"
        # Reset login fields so they can be entered again
        self.login_window.reset_login_fields()
        # Reload updated user data from file
        self.login_window.user_data = dataUtils.load_user_data()

    @staticmethod
    def exit_application():
        # Exit application
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create QApplication instance

    # Create and show main window
    window = MainWindow()
    window.resize(1080, 800)  # Set window size
    window.show()  # Show main window

    # Execute application event loop
    sys.exit(app.exec())
