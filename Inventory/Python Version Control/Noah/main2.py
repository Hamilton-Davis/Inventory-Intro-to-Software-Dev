import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import CentralWidget  # Import CentralWidget from ui.py


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the window title
        self.setWindowTitle("Inventory Management")
        # Resize the main window
        self.resize(1080, 800)
        # Create an instance of CentralWidget and pass the exit method as a callback
        self.central_widget = CentralWidget(self, self.exit_application)
        self.setCentralWidget(self.central_widget)

    @staticmethod  # Indicates this method not dependent on instance state
    # Function to exit the application
    def exit_application():
        print("Closing Application")
        QApplication.quit()


if __name__ == "__main__":
    # Create the QApplication instance
    app = QApplication(sys.argv)
    # Create an instance of MainWindow
    window = MainWindow()
    # Show the main window
    window.show()
    # Start the application's event loop
    sys.exit(app.exec())

