import sqlite3
import os

# Get all .db files in the current directory
db_files = [f for f in os.listdir('.') if f.endswith('.db')]

if not db_files:
    print("No database files found.")
else:
    for db_file in db_files:
        print(f'\nReading data from: {db_file}')

        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # Check if the items table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='items'")
            table_exists = cursor.fetchone()

            if table_exists:
                # Fetch all data from the items table
                cursor.execute('SELECT * FROM items')
                items = cursor.fetchall()

                if items:
                    for item in items:
                        print(item)
                else:
                    print("No data found in the items table.")
            else:
                print("The 'items' table does not exist in this database.")

            # Close the connection
            conn.close()

        except sqlite3.Error as e:
            print(f"An error occurred while reading {db_file}: {e}")

print("\nFinished reading all database files.")
