from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit, QSpacerItem, QTableView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main_window import MainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3

class LookupWindow(QWidget):  

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lookup Item")
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png"))  

        self.window_title_label = QLabel("Lookup/Edit an item", self) 
        self.back_button = QPushButton("Back", self)
        self.search_bar = QLineEdit(self)
        self.search_button = QPushButton("Search", self)
        self.table = QTableView()

        self.main_window = None

        self.database = self.create_connection()
        self.model = QSqlTableModel()
        self.model.setTable("products")
        self.model.select()

        self.initUI() 
        #self.create_connection()


    def initUI(self):  

        title_layout = QHBoxLayout()
        search_layout = QHBoxLayout()

        main_layout = QVBoxLayout()
        

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


        self.table.setModel(self.model)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.setEditTriggers(QTableView.AllEditTriggers)


        title_layout.addWidget(self.back_button)
        title_layout.addWidget(self.window_title_label)

        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        main_layout.addLayout(title_layout)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    def go_back(self):

        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.close()   


    def create_connection(self):
        database = QSqlDatabase.addDatabase('QSQLITE')   
        database.setDatabaseName('products.db')
        if not database.open():
            print("The database was unable to be opened")
        return database     