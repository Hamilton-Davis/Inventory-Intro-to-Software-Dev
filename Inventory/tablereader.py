import datetime
import os
import sqlite3
import pandas as pd
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
    else:
        # Clear the existing table to overwrite data
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items')

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
    headers = [header.replace('_', ' ') for header in headers] # Replace underscores with spaces
    headers = [header.title() for header in headers] # Put headers in Title Case


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

# takes two dates and returns every item in the table between the specified dates
def between_two_dates(db_filename, start_date, end_date):
    conn = sqlite3.connect(db_filename)
    # SQL likes dates in Year/month/day format
    query = f"""
            SELECT *
            FROM your_table
            WHERE strftime('%Y-%m-%d', Date_Entered) BETWEEN '{start_date}' AND '{end_date}'; 
            """
    # this query sorts from our stored month/day/year into SQL friendly year/month/day
    
    # stores our results in a dataframe to be returned
    dataframe = pd.read_sql_query(query, conn)
    conn.close()
    return dataframe

# this will return a dataframe with items grouped by name
# these should be formatted as
#   Item Name        Price                  Quantity                 Sales              Date Entered
#   item1       [price1, price2]        [count1, count2]        [sales1, sales2]      [entry1, entry2]
#   item2       [price1, price2]        [count1, count2]        [sales1, sales2]      [entry1, entry2]
#   item3       [price1, price2]        [count1, count2]        [sales1, sales2]      [entry1, entry2]
#
# this should allow us to pull by item name to new lists and keep all relavent data
# dataframe param is the dataframe created by filtering database table
def sales_data(dataframe):
   # Group by "Item Name" and specify aggregation for specific columns
    grouped_df = dataframe.groupby('Item Name').agg({
        'Price': list,                 # Aggregate Price into a list
        'Quantity': list,              # Aggregate Quantity into a list
        'Sales': list,                 # Aggregate Sales into a list
        'Date Entered': list,          # Aggregate Date Entered into a list
    }).reset_index()
    return grouped_df # returns our grouped dataframe


