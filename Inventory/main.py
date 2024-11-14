import sys
from PySide6.QtWidgets import QApplication
from mainwidget import MainWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instance of MainWidget (contains program's screens)
    mainWidget = MainWidget()
    mainWidget.resize(800, 600)
    mainWidget.show()

    sys.exit(app.exec())
