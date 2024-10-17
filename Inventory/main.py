import sys

from PySide6.QtWidgets import QApplication

from ProgramStackedWidgets import MainWidget
from login import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create an instance of LoginWindow
    login_window = LoginWindow()
    if login_window.exec():  # Will block until login window is closed
        mainWidget = MainWidget()
        mainWidget.resize(800, 600)
        mainWidget.show()

    sys.exit(app.exec())
