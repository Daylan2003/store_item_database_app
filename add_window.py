from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main_window import MainWindow

class AddWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Item")
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png"))    

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

        self.main_window = None

    def initUI(self):  

        title_layout = QHBoxLayout()
        item_name_layout = QHBoxLayout()
        item_price_layout = QHBoxLayout()
        item_quantity_layout = QHBoxLayout()
        item_barcode_layout = QHBoxLayout()

        main_layout = QVBoxLayout()
        
        self.add_title_label.setStyleSheet("font-size: 75px;"
                                           "background-color: #1256b0;"
                                           "border-style: solid;"
                                           "border-color: black;"
                                           "border-width: 5px;"
                                           "font-weight: bold;"
                                           "font-family: Comic Sans MS;"
                                           "color: white")
        self.add_title_label.setAlignment(Qt.AlignCenter)
        self.add_title_label.setFixedHeight(140) 

        
        self.back_button.clicked.connect(self.go_back)
        self.back_button.setStyleSheet("font-size: 75px;"
                                           "background-color: #7d838a;"
                                           "border-style: solid;"
                                           "border-color: black;"
                                           "border-width: 5px;"
                                           "font-weight: bold;"
                                           "font-family: Comic Sans MS;"
                                           "color: white")
        self.back_button.setFixedHeight(140)  
        self.back_button.setFixedWidth(250) 


#----------------------------------------------------------------------------------------------------------------------------------------
        self.item_name_label.setStyleSheet("font-size: 50px;"
                                           "font-family: Arial;")
        self.item_name_label.setFixedWidth(400)
        self.item_name_label.setAlignment(Qt.AlignLeft)
        self.item_name_label.setAlignment(Qt.AlignVCenter)


        self.item_name_line_edit.setStyleSheet("font-size: 50px;"
                                               "font-family: Arial;")
        self.item_name_line_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.item_name_line_edit.setMaximumHeight(70)



#----------------------------------------------------------------------------------------------------------------------------------------
        self.barcode_number_label.setStyleSheet("font-size: 50px;"
                                           "font-family: Arial;")
        self.barcode_number_label.setFixedWidth(400)
        self.barcode_number_label.setAlignment(Qt.AlignLeft)
        self.barcode_number_label.setAlignment(Qt.AlignVCenter)
        


        self.item_barcode_number_line_edit.setStyleSheet("font-size: 50px;"
                                               "font-family: Arial;")
        self.item_barcode_number_line_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.item_barcode_number_line_edit.setMaximumHeight(70)        


       
#--------------------------------------------------------------------------------------------------------------------------------------- 
        self.item_price_label.setStyleSheet("font-size: 50px;"
                                           "font-family: Arial;")
        self.item_price_label.setFixedWidth(400)
        self.item_price_label.setAlignment(Qt.AlignLeft)
        self.item_price_label.setAlignment(Qt.AlignVCenter)

        self.item_price_line_edit.setStyleSheet("font-size: 50px;"
                                               "font-family: Arial;")
        self.item_price_line_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.item_price_line_edit.setMaximumHeight(70)



#----------------------------------------------------------------------------------------------------------------------------------------
        self.item_quantity_label.setStyleSheet("font-size: 50px;"
                                           "font-family: Arial;")
        self.item_quantity_label.setFixedWidth(400)
        self.item_quantity_label.setAlignment(Qt.AlignLeft)
        self.item_quantity_label.setAlignment(Qt.AlignVCenter)
        

        self.item_quantity_line_edit.setStyleSheet("font-size: 50px;"
                                               "font-family: Arial;")
        self.item_quantity_line_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.item_quantity_line_edit.setMaximumHeight(70)


#----------------------------------------------------------------------------------------------------------------------------------------
        self.add_button.clicked.connect(self.add_item)
        self.add_button.setStyleSheet("font-size: 75px;"
                                      "background-color: #1256b0;"
                                      "border-style: solid;"
                                      "border-color: black;"
                                      "border-width: 5px;"
                                      "font-weight: bold;"
                                      "font-family: Comic Sans MS;"
                                      "color: white")
        self.add_button.setFixedHeight(140) 

        self.completion_status_label.setStyleSheet("font-size: 75px;"
                                                   "background-color: #1256b0;"
                                                   "border-style: solid;"
                                                   "border-color: black;"
                                                   "border-width: 5px;"
                                                   "font-weight: bold;"
                                                   "font-family: Comic Sans MS;"
                                                   "color: white") 
        self.completion_status_label.setMaximumHeight(140)

#----------------------------------------------------------------------------------------------------------------------------------------
        title_layout.addWidget(self.back_button, 0)
        title_layout.addWidget(self.add_title_label, 1)

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
        main_layout.addLayout(item_name_layout)
        main_layout.addLayout(item_price_layout)
        main_layout.addLayout(item_quantity_layout)
        main_layout.addLayout(item_barcode_layout)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.completion_status_label)

        self.setLayout(main_layout)

        self.setStyleSheet("background-color: #b1c5de;")

    def go_back(self):

        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.close()    

    def add_item(self):
        print("A new item has been entered into the database")    
        item_name = self.item_name_line_edit.text()
        item_price = self.item_price_line_edit.text()
        item_quantity = self.item_quantity_line_edit.text()
        print(item_name)
        print(item_price)
        print(item_quantity)
        self.completion_status_label.setText("Completion Status: Item Added Successfully") 