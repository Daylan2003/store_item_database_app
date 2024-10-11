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
("Apples", "123456789012", 1.20, 100),
    ("Carrots", "123456789014", 0.80, 200),
    ("Potatoes", "123456789015", 1.00, 120),
    ("Tomatoes", "123456789016", 1.50, 80),
    ("Lettuce", "123456789017", 0.75, 60),
    ("Spinach", "123456789018", 1.00, 50),
    ("Broccoli", "123456789019", 1.30, 40),
    ("Onions", "123456789020", 0.90, 90),
    ("Garlic", "123456789021", 0.60, 70),
    ("Grapes", "123456789022", 2.00, 100),
    ("Oranges", "123456789023", 1.10, 110),
    ("Pineapple", "123456789024", 3.00, 30),
    ("Mango", "123456789025", 1.50, 25),
    ("Strawberries", "123456789026", 2.50, 60),
    ("Watermelon", "123456789027", 5.00, 20),
    ("Peaches", "123456789028", 1.75, 45),
    ("Blueberries", "123456789029", 3.50, 40),
    ("Kiwi", "123456789030", 2.00, 50),
    ("Cherries", "123456789031", 4.00, 30),
    ("Bell Peppers", "123456789032", 1.20, 75),
    ("Cucumbers", "123456789033", 0.80, 80),
    ("Zucchini", "123456789034", 1.00, 65),
    ("Pumpkin", "123456789035", 3.00, 20),
    ("Eggplant", "123456789036", 1.50, 35),
    ("Radishes", "123456789037", 0.70, 55),
    ("Cabbage", "123456789038", 1.20, 30),
    ("Celery", "123456789039", 1.00, 50),
    ("Beets", "123456789040", 0.90, 40),
    ("Cauliflower", "123456789041", 1.50, 30),
    ("Asparagus", "123456789042", 2.50, 25),
    ("Sweet Potatoes", "123456789043", 1.00, 50),
    ("Artichokes", "123456789044", 2.00, 20);
    """)



# Commit our command
connect.commit()

#Close our connection

connect.close()
