from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
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

        self.add_button.setGeometry(0, 500, 100, 50)
        self.add_button.clicked.connect(self.add_item)

    def go_back(self):

        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.close()    

    def add_item(self):
        print("A new item has been entered into the database")    