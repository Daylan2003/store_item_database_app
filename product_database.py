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

cursor.execute("""
	DROP TABLE IF EXISTS products;
	""")



#cursor.execute("""
#    INSERT INTO products (item_name, item_price, item_quantity, barcode_number) VALUES 
#
#    """)



# Commit our command
connect.commit()

#Close our connection

connect.close()
