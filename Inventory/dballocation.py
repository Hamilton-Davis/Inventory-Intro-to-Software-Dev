import sqlite3
import datetime
import os

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

# Function to insert an item into a database
def save_to_db(db_filename, name, category, quantity, cost, sale_price, available, date_stocked, contact):
    new_file = not os.path.exists(db_filename)
    conn = sqlite3.connect(db_filename)

    if new_file:
        create_table_if_not_exists(conn)

    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO items (name, category, quantity, cost, sale_price, available, date_stocked, contact) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, category, quantity, cost, sale_price, available, date_stocked, contact))

    conn.commit()
    conn.close()

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

# Create the test database file and populate it with items
db_filename = get_db_filename()

for item in test_items:
    # Unpack item data and save to the database
    save_to_db(db_filename, *item)

print("Test database file created with 20 items.")
