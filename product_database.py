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
('Apple', 0.50, 100, '123456789012'),
('Banana', 0.30, 150, '234567890123'),
('Orange', 0.80, 200, '345678901234'),
('Grapes', 2.00, 75, '456789012345'),
('Strawberries', 3.50, 50, '567890123456'),
('Blueberries', 4.00, 60, '678901234567'),
('Mango', 1.50, 80, '789012345678'),
('Pineapple', 3.00, 40, '890123456789'),
('Peach', 0.90, 90, '901234567890'),
('Watermelon', 5.00, 30, '012345678901'),
('Lettuce', 1.20, 120, '098765432109'),
('Tomato', 0.75, 110, '876543210987'),
('Carrot', 0.60, 130, '765432109876'),
('Cucumber', 0.85, 140, '654321098765'),
('Bell Pepper', 1.25, 70, '543210987654'),
('Broccoli', 1.75, 50, '432109876543'),
('Onion', 0.40, 200, '321098765432'),
('Garlic', 0.50, 160, '210987654321'),
('Sweet Potato', 0.90, 100, '098765432198'),
('Eggplant', 1.60, 45, '123456789099'),
('Zucchini', 1.00, 80, '234567890988'),
('Chicken Breast', 7.00, 60, '345678901877'),
('Ground Beef', 5.00, 70, '456789012766'),
('Pork Chops', 6.00, 55, '567890123655'),
('Salmon Fillet', 10.00, 30, '678901234544'),
('Shrimp', 12.00, 25, '789012345433'),
('Tofu', 2.50, 90, '890123456322'),
('Rice', 1.00, 150, '901234567211'),
('Pasta', 1.20, 110, '012345678100'),
('Bread', 2.00, 100, '098765432199'),
('Milk', 1.50, 80, '876543210988'),
('Cheese', 3.00, 70, '765432109877'),
('Yogurt', 0.80, 90, '654321098766'),
('Butter', 2.50, 40, '543210987655'),
('Eggs', 3.50, 60, '432109876544'),
('Olive Oil', 5.00, 50, '321098765433'),
('Vinegar', 2.00, 30, '210987654322'),
('Soy Sauce', 2.50, 70, '109876543211'),
('Honey', 6.00, 20, '098765432190'),
('Sugar', 1.00, 150, '123456789988'),
('Flour', 0.50, 200, '234567890877'),
('Baking Powder', 1.20, 60, '345678901766'),
('Chocolate Chips', 3.00, 40, '456789012655'),
('Nuts Mix', 4.50, 30, '567890123544'),
('Cereal', 2.00, 50, '678901234433'),
('Granola Bars', 1.50, 60, '789012345322');
    """)



# Commit our command
connect.commit()

#Close our connection

connect.close()
