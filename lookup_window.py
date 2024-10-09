from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit, QSpacerItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main_window import MainWindow
import sqlite3

class LookupWindow(QWidget):  

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lookup Item")
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png"))  

        self.window_title_label = QLabel("Lookup an item", self) 
        self.back_button = QPushButton("Back", self)
        self.search_bar = QLineEdit(self)
        self.search_button = QPushButton("Search", self)

        self.main_window = None

        self.initUI() 
        self.create_connection()


    def initUI(self):  
        

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


        self.window_title_label.setStyleSheet("font-size: 75px;"
                                           "background-color: #1256b0;"
                                           "border-style: solid;"
                                           "border-color: black;"
                                           "border-width: 5px;"
                                           "font-weight: bold;"
                                           "font-family: Comic Sans MS;"
                                           "color: white")
        self.window_title_label.setAlignment(Qt.AlignCenter)
        self.window_title_label.setFixedHeight(140)

    def go_back(self):

        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.close()   