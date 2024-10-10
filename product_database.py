import sqlite3
from add_window import AddWindow

connect = sqlite3.connect('products.db')

#Create a cursor
cursor = connect.cursor()


#Create a table
#cursor.execute("""
#	CREATE TABLE products (
#		Item_name TEXT,
#		Item_price REAL,
#		Item_Quantity INTEGER,
#		Barcode_number INTEGER
#		)
#
#	""")
#--------------------------------------------------------------------------------------------------------------------------
#                                                           DATABASE CREATED

#cursor.execute("""
#	DROP TABLE IF EXISTS products;
#	""")



cursor.execute("""
    INSERT INTO products (item_name, item_price, item_quantity, barcode_number) VALUES 
('Bananas', 0.79, 50, 1000002),
('Milk', 2.50, 30, 1000003),
('Bread', 1.99, 15, 1000004),
('Eggs', 3.49, 40, 1000005),
('Chicken Breast', 8.99, 10, 1000006),
('Orange Juice', 4.99, 25, 1000007),
('Rice', 12.99, 35, 1000008),
('Cheese', 5.99, 12, 1000009),
('Yogurt', 1.50, 45, 1000010);
    """)



# Commit our command
connect.commit()

#Close our connection

connect.close()
