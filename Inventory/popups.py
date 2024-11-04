from PySide6.QtWidgets import QMessageBox

# Confirmation message for delete action
def delete_confirmation_dialog():
    msg = "This action cannot be undone. \nAre you sure you want to delete?"
    title = "Delete"
    icon = QMessageBox.Warning

    # Get confirmation
    return confirmation_dialog(msg, title, icon)

# Creates confirmation popup with yes/no options
def confirmation_dialog(msg, title="", icon=QMessageBox.NoIcon):
    popup = QMessageBox()
    if title: popup.setWindowTitle(title) # Add title if given
    popup.setText(msg)
    if icon: popup.setIcon(icon) # Add icon if given

    #Get response
    popup.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    popup.setDefaultButton(QMessageBox.No)
    response = popup.exec_()
    if response == QMessageBox.Yes:
        return True
    else:
        return False
