from PySide6.QtWidgets import QMessageBox

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


# Confirmation message for delete action
def delete_confirmation_dialog():
    msg = "This action cannot be undone. \nAre you sure you want to delete?"
    title = "Delete"
    icon = QMessageBox.Warning

    # Get confirmation
    return confirmation_dialog(msg, title, icon)


# Confirmation for cancel/discard action
def cancel_confirmation_dialog():
    msg = "Unsaved changes will be discarded. \nAre you sure you want to continue?"
    title = "Cancel"
    icon = QMessageBox.Warning

    # Get confirmation
    return confirmation_dialog(msg, title, icon)

# Confirmation for save action
def save_confirmation_dialog():
    msg = "Saving will close this screen. \nAre you sure the entered sales are correct?"
    title = "Save"
    icon = QMessageBox.Question

    # Get confirmation
    return confirmation_dialog(msg, title, icon)
