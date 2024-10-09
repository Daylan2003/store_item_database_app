import sqlite3
from add_window import AddWindow


def create_database():
    connect = sqlite3.connect('products.db')

#Create a cursor
    cursor = connect.cursor()

    cursor.execute ("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            item_price REAL,
            item_quantity INTEGER,
            barcode_number INTEGER                                        
                )
    """)

    connect.commit()
    connect.close()    

