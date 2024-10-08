from PySide6.QtWidgets import QWidget, QPushButton, QTableWidget, QGridLayout, QApplication


#InventoryWidget extends QWidget
class InventoryWidget(QWidget):
    def __init__(self):
        super().__init__()

        #Create all buttons
        self.saveButton = QPushButton("Save")
        self.addItemButton = QPushButton("Add Item")
        self.editItemButton = QPushButton("Edit Item")
        self.removeItemButton = QPushButton("Remove Item")
        self.homeButton = QPushButton("Home")

        #Table to display items in inventory
        self.itemTable = QTableWidget() 

        #Layout all widgets in grid
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.saveButton)
        self.layout.addWidget(self.addItemButton)
        self.layout.addWidget(self.editItemButton)
        self.layout.addWidget(self.removeItemButton)
        self.layout.addWidget(self.homeButton)
        self.layout.addWidget(self.itemTable)


app = QApplication()
inventoryWidget = InventoryWidget()
inventoryWidget.show()

app.exec()