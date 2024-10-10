from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit, QSpacerItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main_window import MainWindow
import sqlite3
from add_to_database import create_database

class AddWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Item")
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png")) 

        self.spacer1 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)   
        self.spacer2 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)  
        self.spacer3 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)  
        self.spacer4 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)  
        self.spacer5 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)  

        self.add_title_label = QLabel("Add an item to the database", self)   
        self.back_button = QPushButton("Back", self) 

        self.item_name_label = QLabel("Item name: ")
        self.item_name_line_edit = QLineEdit(self)

        self.item_price_label = QLabel("Item price: ")
        self.item_price_line_edit = QLineEdit(self)

        self.item_quantity_label = QLabel("Item quantity: ")
        self.item_quantity_line_edit = QLineEdit(self)

        self.barcode_number_label = QLabel("Barcode number: ")
        self.item_barcode_number_line_edit = QLineEdit(self)

        self.add_button = QPushButton("Add Item", self)

        self.completion_status_label = QLabel("Completion Status: ")



        self.initUI() 
        create_database()

        self.main_window = None

    def initUI(self):  

        title_layout = QHBoxLayout()
        item_name_layout = QHBoxLayout()
        item_price_layout = QHBoxLayout()
        item_quantity_layout = QHBoxLayout()
        item_barcode_layout = QHBoxLayout()

        main_layout = QVBoxLayout()
        
         

        
        self.back_button.clicked.connect(self.go_back)
        self.back_button.setStyleSheet(
                                        """
                                        QPushButton {
                                        font-size: 75px;
                                        background-color: #7d838a;
                                        border-bottom: 5px solid #32353d;
                                        border-top: 5px solid #32353d;
                                        border-left: 5px solid #32353d;
                                        font-weight: bold;
                                        font-family: Comic Sans MS;
                                        color: white;
                                        }
                                        QPushButton:hover {
                                        background-color: #c5d7eb;
                                        border-bottom: 5px solid white;
                                        border-top: 5px solid white;
                                        border-left: 5px solid white; 
                                        color: #7d838a  
                                        }
                                        """
                                        )
        self.back_button.setCursor(Qt.PointingHandCursor) 
        self.back_button.setFixedHeight(140)  
        self.back_button.setFixedWidth(250) 


        self.add_title_label.setStyleSheet("font-size: 75px;"
                                           "background-color: #1256b0;"
                                           "border-style: solid;"
                                           "border-color: #32353d;"
                                           "border-width: 5px;"
                                           "font-weight: bold;"
                                           "font-family: Comic Sans MS;"
                                           "color: white")
        self.add_title_label.setAlignment(Qt.AlignCenter)
        self.add_title_label.setFixedHeight(140)


#----------------------------------------------------------------------------------------------------------------------------------------
        self.item_name_label.setStyleSheet("font-size: 55px;"
                                           "font-family: Comic Sans MS;")
        self.item_name_label.setFixedWidth(460)
        self.item_name_label.setAlignment(Qt.AlignLeft)
        self.item_name_label.setAlignment(Qt.AlignVCenter)


        self.item_name_line_edit.setStyleSheet("font-size: 50px;"
                                               "font-family: Arial;"
                                               "background-color: white;"
                                               "border-style: solid;"
                                               "border-width: 2px;"
                                               "border-color: #0d4178;")
        
        self.item_name_line_edit.setPlaceholderText("Enter Item Name")
        self.item_name_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       



#----------------------------------------------------------------------------------------------------------------------------------------
        self.barcode_number_label.setStyleSheet("font-size: 55px;"
                                           "font-family: Comic Sans MS;")
        self.barcode_number_label.setFixedWidth(460)
        self.barcode_number_label.setAlignment(Qt.AlignLeft)
        self.barcode_number_label.setAlignment(Qt.AlignVCenter)
        


        self.item_barcode_number_line_edit.setStyleSheet("font-size: 50px;"
                                                         "font-family: Arial;"
                                                         "background-color: white;"
                                                         "border-style: solid;"
                                                         "border-width: 2px;"
                                                         "border-color: #0d4178;")
        self.item_barcode_number_line_edit.setPlaceholderText("Enter Barcode Number")
        self.item_barcode_number_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
          


       
#--------------------------------------------------------------------------------------------------------------------------------------- 
        self.item_price_label.setStyleSheet("font-size: 55px;"
                                           "font-family: Comic Sans MS;")
        self.item_price_label.setFixedWidth(460)
        self.item_price_label.setAlignment(Qt.AlignLeft)
        self.item_price_label.setAlignment(Qt.AlignVCenter)

        self.item_price_line_edit.setStyleSheet("font-size: 50px;"
                                               "font-family: Arial;"
                                               "background-color: white;"
                                               "border-style: solid;"
                                               "border-width: 2px;"
                                               "border-color: #0d4178;")
        self.item_price_line_edit.setPlaceholderText("Enter Item Price")
        self.item_price_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       



#----------------------------------------------------------------------------------------------------------------------------------------
        self.item_quantity_label.setStyleSheet("font-size: 55px;"
                                           "font-family: Comic Sans MS;")
        self.item_quantity_label.setFixedWidth(460)
        self.item_quantity_label.setAlignment(Qt.AlignLeft)
        self.item_quantity_label.setAlignment(Qt.AlignVCenter)
        

        self.item_quantity_line_edit.setStyleSheet("font-size: 50px;"
                                                  "font-family: Arial;"
                                                  "background-color: white;"
                                                  "border-style: solid;"
                                                  "border-width: 2px;"
                                                  "border-color: #0d4178;")
        self.item_quantity_line_edit.setPlaceholderText("Enter Item Quantity")
        self.item_quantity_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       


#----------------------------------------------------------------------------------------------------------------------------------------
        self.add_button.clicked.connect(self.add_item)
        self.add_button.setStyleSheet("""
                                      QPushButton{
                                      font-size: 75px;
                                      background-color: #1256b0;
                                      border-style: solid;
                                      border-color: black;
                                      border-width: 5px;
                                      font-weight: bold;
                                      font-family: Comic Sans MS;
                                      color: white;
                                      }
                                      QPushButton:hover {
                                      color: #1256b0;
                                      background-color: #e1ebf5;
                                      border-color: white;
                                      }
                                    """)
        self.back_button.setCursor(Qt.PointingHandCursor) 
        self.add_button.setFixedHeight(140) 

        self.completion_status_label.setStyleSheet("font-size: 75px;"
                                                   "background-color: #1256b0;"
                                                   "border: 5px solid black;"
                                                   "font-weight: bold;"
                                                   "font-family: Comic Sans MS;"
                                                   "color: white") 
        self.completion_status_label.setFixedHeight(140)
        

        
#----------------------------------------------------------------------------------------------------------------------------------------
        title_layout.addWidget(self.back_button)
        title_layout.addWidget(self.add_title_label)

        title_layout.setSpacing(0)  # Space between back button and title label
        title_layout.setContentsMargins(0, 0, 0, 0)

        item_name_layout.addWidget(self.item_name_label)
        item_name_layout.addWidget(self.item_name_line_edit)
        item_name_layout.setContentsMargins(10, 10, 50, 10)

        item_price_layout.addWidget(self.item_price_label)
        item_price_layout.addWidget(self.item_price_line_edit)
        item_price_layout.setContentsMargins(10, 10, 50, 10)

        item_quantity_layout.addWidget(self.item_quantity_label)
        item_quantity_layout.addWidget(self.item_quantity_line_edit)
        item_quantity_layout.setContentsMargins(10, 10, 50, 10)

        item_barcode_layout.addWidget(self.barcode_number_label)
        item_barcode_layout.addWidget(self.item_barcode_number_line_edit)
        item_barcode_layout.setContentsMargins(10, 10, 50, 10)



     


        main_layout.addLayout(title_layout)
        main_layout.addItem(self.spacer1)
        main_layout.addLayout(item_name_layout)
        main_layout.addItem(self.spacer2)
        main_layout.addLayout(item_price_layout)
        main_layout.addItem(self.spacer3)
        main_layout.addLayout(item_quantity_layout)
        main_layout.addItem(self.spacer4)
        main_layout.addLayout(item_barcode_layout)
        main_layout.addItem(self.spacer5)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.completion_status_label)

        main_layout.setContentsMargins(0, 0, 0, 10)

        self.setLayout(main_layout)

        self.setStyleSheet("background-color: #b1c5de;")

    def go_back(self):

        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.close()    

    def add_item(self):   
        item_name = self.item_name_line_edit.text()

        item_quantity_input = self.item_quantity_line_edit.text()
        if item_quantity_input.strip() == "":
            item_quantity = -1
        else:
            try:
                item_quantity = int(item_quantity_input)
            except ValueError:
                self.completition_error()
                return

          

        try:
            item_price = round(float(self.item_price_line_edit.text()),2)
            barcode_number = int(self.item_barcode_number_line_edit.text())
        except ValueError:
            self.completition_error()
            return    

        inputs_correct = self.check_input(item_name, item_price, item_quantity, barcode_number)

        

        if inputs_correct:
            print(item_name)
            print(item_price)
            print(item_quantity)
            print(barcode_number)
            self.completion_status_label.setText("Completion Status: Item Added Successfully")    
            self.completion_status_label.setStyleSheet("font-size: 75px;"
                                                       "background-color: #079c05;"
                                                       "border-style: solid;"
                                                       "border-color: black;"
                                                       "border-width: 5px;"
                                                       "font-weight: bold;"
                                                       "font-family: Comic Sans MS;"
                                                       "color: white") 
            
            try:
                connect = sqlite3.connect('products.db')
                cursor = connect.cursor() 
                cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)", (item_name, item_price, item_quantity, barcode_number))
 
                connect.commit()
            except sqlite3.Error as e:
                self.completion_status_label.setText(f"Database Error: {e}")
            finally:
                connect.close()    
                       

        else:
            self.completition_error() 

          
        

    def check_input(self, name, price, quantity, number):
        correct_inputs = True
        if not isinstance(name, str):
            correct_inputs = False    
        if not isinstance(price, float) or price < 0:
            correct_inputs = False     
        if not isinstance(quantity, int) or quantity < -1:
            correct_inputs = False   
        if not isinstance(number, int):
            correct_inputs = False    

        return correct_inputs   


    def completition_error(self):
        self.completion_status_label.setText("Completion Status: Error, Item entered incorrectly.") 
        self.completion_status_label.setStyleSheet("font-size: 75px;"
                                                    "background-color: #f51d1d;"
                                                    "border-style: solid;"
                                                    "border-color: black;"
                                                    "border-width: 5px;"
                                                    "font-weight: bold;"
                                                    "font-family: Comic Sans MS;"
                                                    "color: white")          