from PySide6.QtWidgets import QMessageBox

# Confirmation message for delete action
def delete_confirmation_dialog():
    #Create message
    msg = QMessageBox()
    msg.setWindowTitle("Delete")
    msg.setText("This action cannot be undone. \nAre you sure you want to delete?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    #Get response
    msg.setDefaultButton(QMessageBox.No)
    response = msg.exec_()
    if response == QMessageBox.Yes:
        return True
    else:
        return False