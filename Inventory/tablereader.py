import datetime
import sqlite3
import pandas as pd
from enum import Enum


class HeaderIndex(Enum):
    NAME = 0
    CATEGORY = 1
    QUANTITY = 2
    COST = 3
    SALE_PRICE = 4
    AVAILABLE = 5
    DATE_STOCKED = 6
    CONTACT = 7
    LOG_QNT_SOLD = 4

class DatabaseManager:
    DB_FILE = 'items.db'

    @staticmethod
    def connect():
        return sqlite3.connect(DatabaseManager.DB_FILE)

    @staticmethod
    def create_table(date=None):
        table_name = DatabaseManager.get_table_name(date)
        conn = DatabaseManager.connect()
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT,
                quantity INTEGER,
                cost REAL,
                sale_price REAL,
                available BOOLEAN,
                date_stocked TEXT,
                contact TEXT,
                qnt_sold INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def get_table_name(date=None):
        if date is None:
            date = datetime.datetime.now()
        return f"items_{date.strftime('%Y_%m_%d')}"


    @staticmethod
    def get_most_recent_table():
        conn = DatabaseManager.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'items_%' ORDER BY name DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None


    @staticmethod
    def export_table(table, date=None):
        table_name = DatabaseManager.get_table_name(date)
        DatabaseManager.create_table(date)
        conn = DatabaseManager.connect()
        cursor = conn.cursor()
        headers, data = DatabaseManager.read_table(table)

        # Clear existing table data before exporting
        cursor.execute(f'DELETE FROM {table_name}')

        for row in data:
            cursor.execute(f'''
                INSERT INTO {table_name} (name, category, quantity, cost, sale_price, available, date_stocked, contact, qnt_sold)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', row)

        conn.commit()
        conn.close()


    @staticmethod
    def read_table(table):
        headers = [table.horizontalHeaderItem(col).text() if table.horizontalHeaderItem(col) else "" for col in range(table.columnCount())]
        data = [[table.item(row, col).text() if table.item(row, col) else "" for col in range(table.columnCount())] for row in range(table.rowCount())]
        return headers, data


    @staticmethod
    def import_db(date=None):
        table_name = DatabaseManager.get_table_name(date)
        conn = DatabaseManager.connect()
        cursor = conn.cursor()

        # Check if the table exists in the database
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        table_exists = cursor.fetchone() is not None

        # Default headers and empty data to return if table does not exist
        default_headers = ['Name', 'Category', 'Quantity', 'Cost ($)', 'Sale Price ($)', 'Available', 'Date Stocked',
                           'Contact', 'Qnt Sold']

        if not table_exists:
            # If the table does not exist, return headers and empty data
            conn.close()
            return default_headers, []

        # If the table exists, retrieve data from it
        cursor.execute(
            f"SELECT name, category, quantity, cost, sale_price, available, date_stocked, contact, qnt_sold FROM {table_name}")
        data = cursor.fetchall()

        conn.close()
        return default_headers, data


    @staticmethod
    def between_two_dates(start_date, end_date):
        table_name = DatabaseManager.get_table_name()
        conn = DatabaseManager.connect()
        query = f"""
            SELECT * FROM {table_name}
            WHERE strftime('%Y-%m-%d', date_stocked) BETWEEN '{start_date}' AND '{end_date}';
        """
        dataframe = pd.read_sql_query(query, conn)
        conn.close()
        return dataframe


    @staticmethod
    def sales_data(dataframe):
        grouped_df = dataframe.groupby('name').agg({
            'cost': list,
            'quantity': list,
            'sale_price': list,
            'date_stocked': list,
        }).reset_index()
        return grouped_df
