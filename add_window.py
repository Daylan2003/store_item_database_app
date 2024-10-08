from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main_window import MainWindow

class AddWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Item")
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png"))    

        self.add_title_label = QLabel("Add an item to the database", self)   
        self.back_button = QPushButton("Back", self) 

        self.item_name_label = QLabel("Item name: ")
        self.item_name_line_edit = QLineEdit(self)

        self.item_price_label = QLabel("Item price: ")
        self.item_price_line_edit = QLineEdit(self)

        self.item_quantity_label = QLabel("Item quantity: ")
        self.item_quantity_line_edit = QLineEdit(self)

        self.add_button = QPushButton("Add Item", self)



        self.initUI() 

        self.main_window = None

    def initUI(self):  
        
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

        self.back_button.setGeometry(0, 0, 100, 50)
        self.back_button.clicked.connect(self.go_back) 

        self.item_name_line_edit.setGeometry(0, 200, 400, 30)
        self.item_name_line_edit.setStyleSheet("font-size: 20px;"
                                               "font-family: Arial;")


        self.item_price_line_edit.setGeometry(0, 300, 400, 30)
        self.item_price_line_edit.setStyleSheet("font-size: 20px;"
                                               "font-family: Arial;")


        self.item_quantity_line_edit.setGeometry(0, 400, 400, 30)
        self.item_quantity_line_edit.setStyleSheet("font-size: 20px;"
                                               "font-family: Arial;")



        self.add_button.setGeometry(0, 500, 100, 50)
        self.add_button.clicked.connect(self.add_item)

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