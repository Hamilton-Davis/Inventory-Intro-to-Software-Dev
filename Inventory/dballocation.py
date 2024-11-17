import sqlite3
from datetime import datetime, timedelta
import random

# Test data generation
test_items = [
    ('Widget A', 'Gadgets', 10, 2.50, 5.00, True, '2024-11-11', 'contact1@example.com'),
    ('Widget B', 'Tools', 15, 3.00, 7.50, True, '2024-11-11', 'contact2@example.com'),
    ('Widget C', 'Electronics', 5, 20.00, 50.00, True, '2024-11-11', 'contact3@example.com'),
    ('Widget D', 'Home Goods', 25, 1.25, 2.75, True, '2024-11-11', 'contact4@example.com'),
    ('Widget E', 'Stationery', 100, 0.10, 0.50, True, '2024-11-11', 'contact5@example.com'),
    ('Widget F', 'Toys', 50, 4.00, 8.50, True, '2024-11-11', 'contact6@example.com'),
    ('Widget G', 'Outdoor', 20, 15.00, 35.00, True, '2024-11-11', 'contact7@example.com'),
    ('Widget H', 'Kitchen', 30, 2.00, 6.00, True, '2024-11-11', 'contact8@example.com'),
    ('Widget I', 'Clothing', 40, 5.50, 12.00, True, '2024-11-12', 'contact9@example.com'),
    ('Widget J', 'Footwear', 60, 10.00, 25.00, True, '2024-11-12', 'contact10@example.com'),
    ('Widget K', 'Accessories', 80, 3.50, 9.00, True, '2024-11-12', 'contact11@example.com'),
    ('Widget L', 'Books', 35, 7.00, 15.00, True, '2024-11-12', 'contact12@example.com'),
    ('Widget M', 'Music', 22, 6.00, 12.50, True, '2024-11-12', 'contact13@example.com'),
    ('Widget N', 'Health', 10, 1.50, 4.00, True, '2024-11-12', 'contact14@example.com'),
    ('Widget O', 'Beauty', 45, 3.25, 8.00, True, '2024-11-12', 'contact15@example.com'),
    ('Widget P', 'Automotive', 12, 14.00, 30.00, True, '2024-11-13', 'contact16@example.com'),
    ('Widget Q', 'Garden', 25, 2.75, 7.00, True, '2024-11-13', 'contact17@example.com'),
    ('Widget R', 'Hardware', 18, 5.00, 11.00, True, '2024-11-13', 'contact18@example.com'),
    ('Widget S', 'Furniture', 5, 50.00, 120.00, True, '2024-11-13', 'contact19@example.com'),
    ('Widget T', 'Pet Supplies', 55, 3.00, 7.50, True, '2024-11-13', 'contact20@example.com')
]


# Create multiple tables for a specified date range and insert items with random qnt_sold values.
def create_tables_and_insert_items(db_name, start_date, end_date, item_lists):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Generate tables for each date in the range
    current_date = start_date
    while current_date <= end_date:
        # Format the table name as "item_yyyy_MM_dd"
        table_name = f"items_{current_date.strftime('%Y_%m_%d')}"

        # Create the table if it doesn't already exist
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                name TEXT,
                category TEXT,
                quantity INTEGER,
                cost REAL,
                sale_price REAL,
                available INTEGER,
                date_stocked TEXT,
                contact TEXT,
                qnt_sold INTEGER
            )
        """)

        # Insert items into the table with a randomly generated qnt_sold value
        for item in item_lists:
            name, category, quantity, cost, sale_price, available, date_stocked, contact = item
            random_qnt_sold = random.randint(0, quantity)  # Generate a random qnt_sold value
            cursor.execute(f"""
                INSERT INTO {table_name} (name, category, quantity, cost, sale_price, available, date_stocked, contact, qnt_sold)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name, category, quantity, cost, sale_price, available, date_stocked, contact, random_qnt_sold))

        # Move to the next day
        current_date += timedelta(days=1)

    # Commit changes and close the database connection
    conn.commit()
    conn.close()

# Generate test tables
create_tables_and_insert_items("items.db", datetime.today() - timedelta(days=10), datetime.today(), test_items)