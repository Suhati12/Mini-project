import sqlite3

conn = sqlite3.connect('food_order.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    items TEXT,
    total REAL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

menu_items = [
    ('Pizza', 250),
    ('Burger', 150),
    ('Pasta', 180),
    ('Momos', 120),
    ('Cold Coffee', 90),
    ('Sandwich', 130)
]

cursor.execute('SELECT COUNT(*) FROM menu')
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany('INSERT INTO menu (name, price) VALUES (?, ?)', menu_items)
    print("✅ Menu items added successfully!")
else:
    print("⚠️ Menu already exists. Skipping insert.")

conn.commit()
conn.close()
print("Database setup completed.")
