import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
sys.path.append((Path(__file__).parent.parent.resolve() / 'Isaac').resolve().__str__())
sys.path.append((Path(__file__).parent.parent.resolve() / 'Noah').resolve().__str__())
from ProgramStackedWidgets import MainWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instance of MainWidget (contains ProgramStackedWidget with program's screens)
    mainWidget = MainWidget()
    mainWidget.resize(800, 600)
    mainWidget.show()

    sys.exit(app.exec())