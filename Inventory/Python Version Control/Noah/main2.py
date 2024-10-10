import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import CentralWidget  # Import CentralWidget from ui.py
from login import LoginWindow  # Import LoginWindow from login.py


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call parent QMainWindow constructor
        self.setWindowTitle("Inventory Management")  # Set window title
        self.resize(1080, 800)  # Set main window size

        # Create an instance of CentralWidget and pass the exit method as a callback
        self.central_widget = CentralWidget(self, self.exit_application)
        self.setCentralWidget(self.central_widget)  # Set central widget for main window

    @staticmethod
    def exit_application():
        print("Closing Application")
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create an instance of LoginWindow
    login_window = LoginWindow()
    if login_window.exec():  # Will block until login window is closed
        main_window = MainWindow()
        main_window.show()  # Show main window

    sys.exit(app.exec())
