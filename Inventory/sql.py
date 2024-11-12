import sqlite3

# Connect to the SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect('test_items.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table with the specified characteristics
cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    stock INTEGER,
    price REAL,
    category TEXT,
    item TEXT,
    in_stock BOOLEAN,
    purchased INTEGER,
    availability TEXT,
    link TEXT,
    entry_date TEXT
)
''')

# Insert a sample item into the table
cursor.execute('''
INSERT INTO items (name, stock, price, category, item, in_stock, purchased, availability, link, entry_date) 
VALUES 
('Example Item', 50, 19.99, 'Electronics', 'Gadget', 1, 20, 'Available', 'https://example.com/item', '2024-11-11')
''')

# Commit the changes and close the connection
conn.commit()

# Query and display all items in the table
cursor.execute('SELECT * FROM items')
items = cursor.fetchall()

print('Stored items:')
for item in items:
    print(item)

# Close the connection
conn.close()
