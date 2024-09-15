from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import Qt


# Slot (slots respond to signals) performs task when button clicked
def button_clicked():
    print("You clicked the button!")


def exit_clicked():
    print("Closed Application")
    QApplication.quit()


# QApplication manages GUI app
app = QApplication()

# Create main window and set its title
window = QMainWindow()
window.setWindowTitle("Inventory Management")

# Create a central widget
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Create buttons and set their fixed sizes
button1 = QPushButton("Check Inventory", central_widget)
button1.setFixedSize(150, 150)  # Set the size of the button
button1.move(300, 390)  # Set the position of the button (x, y)

button2 = QPushButton("Sales Analysis", central_widget)
button2.setFixedSize(150, 150)
button2.move(600, 390)

button3 = QPushButton("Exit", central_widget)
button3.setFixedSize(75, 75)
button3.move(1000, 700)

# Connect buttons to slot
button1.clicked.connect(button_clicked)
button2.clicked.connect(button_clicked)
button3.clicked.connect(exit_clicked)

# Size the window
window.resize(1080, 1080)

# Show window
window.show()

# Run GUI application
app.exec()
