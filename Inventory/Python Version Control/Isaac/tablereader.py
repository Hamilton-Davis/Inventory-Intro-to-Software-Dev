from PySide6.QtWidgets import QTableWidgetItem
import openpyxl

# Exports a table widget's data to openpyxl workbook
def export_table(table):
    # Create workbook and select active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Read table
    (headers, data) = read_table(table)

    # Write headers to workbook
    ws.append(headers)

    # Write rows to workbook
    for row in data:
        ws.append(row)

    return wb

# Reads a table widget's data into a tuple in format ([headers], [data])
def read_table(table):
    headers = []
    # Get header names
    for column in range(table.columnCount()):
        if table.horizontalHeaderItem(column) is None:
            table.setHorizontalHeaderItem(column, QTableWidgetItem(""))
        headers.append(table.horizontalHeaderItem(column).text())

    # Get table data
    data = []
    for row in range(table.rowCount()):
        row_data = []
        for column in range(table.columnCount()):
            if table.item(row, column) is None:
                table.setItem(row, column, QTableWidgetItem(""))
            row_data.append(table.item(row, column).text())

        data.append(row_data)

    return headers, data

