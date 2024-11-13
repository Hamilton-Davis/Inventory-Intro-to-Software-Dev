import datetime
import os
import sqlite3

from PySide6.QtWidgets import QTableWidgetItem


# Function to create a database file with the current date or a specified date
def get_db_filename(date_offset=0):
    date = datetime.datetime.now() + datetime.timedelta(days=date_offset)
    date_str = date.strftime('%Y-%m-%d')
    db_filename = f'items_{date_str}.db'
    return db_filename

# Function to create the table if it doesn't exist
def create_table_if_not_exists(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT,
        quantity INTEGER,
        cost REAL,
        sale_price REAL,
        available BOOLEAN,
        date_stocked TEXT,
        contact TEXT
    )
    ''')
    conn.commit()

# Function to export table widget data to a database
def export_table(table, db_filename=get_db_filename()):
    new_file = not os.path.exists(db_filename)
    conn = sqlite3.connect(db_filename)

    if new_file:
        create_table_if_not_exists(conn)

    cursor = conn.cursor()
    headers, data = read_table(table)

    # Insert each row of data into the database
    for row in data:
        cursor.execute('''
        INSERT INTO items (name, category, quantity, cost, sale_price, available, date_stocked, contact)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

    conn.commit()
    conn.close()

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

# Function to import data from a database
def import_db(db_filename=get_db_filename()):
    if not os.path.exists(db_filename):
        print("Database file not found.")
        default_headers = ['Name', 'Category', 'Quantity', 'Cost', 'Sale Price', 'Available', 'Date Stocked', 'Contact']
        return default_headers, []

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    # Get header names
    cursor.execute("PRAGMA table_info(items)")
    headers = [info[1] for info in cursor.fetchall()]
    headers.remove('id')
    headers = [header.capitalize() for header in headers]
    print(headers)

    # Get data rows
    cursor.execute("SELECT name, category, quantity, cost, sale_price, available, date_stocked, contact FROM items")
    data = cursor.fetchall()

    conn.close()
    return headers, data

# Test data insertion
db_filename = get_db_filename()

# Example call to export and import functions (for testing)
# export_table_to_db(your_table_widget, db_filename)
# headers, data = import_from_db(db_filename)
# print("Headers:", headers)
# print("Data:", data)
