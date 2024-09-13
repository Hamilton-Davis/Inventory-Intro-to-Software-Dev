from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#Slot (slots respond to signals) performs task when button clicked
def button_clicked():
    #Note that print will display on console, not on GUI window
    print("You clicked the button!")

#QApplication manages GUI app
app = QApplication()

#Set all details for GUI app before running
#Create main window and set name
window = QMainWindow()
window.setWindowTitle("Test Window")

#Create a click-able button and add to window
button = QPushButton("Press me to do something")
window.setCentralWidget(button)

#clicked is built-in signal for QPushButton, signal raised when button is clicked
#Connect signal to slot to have app call slot whenever signal is raised
button.clicked.connect(button_clicked)
#The following syntax will cause the slot to be called immediately. I don't know why
#button.clicked.connect(button_clicked())
#So just don't include parentheses after slot identifier

#Resize window to fit button. Uses button.size() to get QSize object as arg
window.resize(100, 100)

#Tell app to display main window
window.show()
#Run GUI app
app.exec()