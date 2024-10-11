from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit, QSpacerItem, QTableView, QHeaderView
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
        self.delete_bar = QLineEdit(self)
        self.delete_button = QPushButton("Delete", self)
        self.save_changes_button = QPushButton("Save Changes", self)
        self.change_status_label = QLabel("Status: ")

        self.main_window = None

        self.database = self.create_connection()
        self.model = QSqlTableModel()
        self.model.setTable("products")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit) 
        self.model.setHeaderData(0, Qt.Horizontal, "Item Name")
        self.model.setHeaderData(1, Qt.Horizontal, "Item Price")
        self.model.setHeaderData(2, Qt.Horizontal, "Item Quantity")
        self.model.setHeaderData(3, Qt.Horizontal, "Barcode Number")

        self.model.select()

        self.initUI() 
        #self.create_connection()


    def initUI(self):  

        title_layout = QHBoxLayout()
        search_layout = QHBoxLayout()

        database_layout = QHBoxLayout()
        delete_layout = QHBoxLayout()
        changes_layout = QHBoxLayout()

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


#----------------------------------------------------------------------------------------------------------------------------------------        
        self.search_bar.setStyleSheet("font-size: 55px;"
                                      "font-family: Arial;"
                                      "background-color: white;"
                                      "border-style: solid;"
                                      "border-width: 2px;"
                                      "border-color: #0d4178;")
        self.search_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.search_bar.setFixedHeight(70)
        self.search_bar.setPlaceholderText("Search Item")
        

        self.search_button.setStyleSheet(
                                        """
                                        QPushButton {
                                        font-size: 50px;
                                        background-color: #a5a6a8;
                                        border-bottom: 3px solid #32353d;
                                        border-top: 3px solid #32353d;
                                        border-right: 3px solid #32353d;
                                        font-weight: bold;
                                        font-family: Comic Sans MS;
                                        color: white;
                                        }
                                        QPushButton:hover {
                                        background-color: #c5d7eb;
                                        border-bottom: 3px solid white;
                                        border-top: 3px solid white;
                                        border-right: 3px solid white; 
                                        color: #7d838a  
                                        }
                                        """
                                        )
        self.search_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.search_button.setFixedWidth(200)
        self.search_button.setFixedHeight(70) 
        self.search_button.clicked.connect(self.search_item)


#----------------------------------------------------------------------------------------------------------------------------------------

        self.table.setModel(self.model)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.setEditTriggers(QTableView.AllEditTriggers)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setStyleSheet("""
            QTableView {
                        background-color: #f0e7c7;
                        font-size: 30px;
                        border: 3px solid #0d4178;
                        alternating-row-color: #bf9a15;
                        font-family: Arial;                                    
                        }                            
            QHeaderView::section {
                        padding : 10px;
                        font-size: 30px;
                        font-weight: bold;
                        background-color: #a2a4b0;                                     
                        }
            QTableCornerButton::section {
                                 background-color: #2c2c30;
                                 }                     


                                    """
            
            
            
            
          )


#----------------------------------------------------------------------------------------------------------------------------------------

        self.delete_bar.setStyleSheet("font-size: 55px;"
                                      "font-family: Arial;"
                                      "background-color: white;"
                                      "border-style: solid;"
                                      "border-width: 2px;"
                                      "border-color: #0d4178;")
        self.delete_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.delete_bar.setFixedHeight(70)
        self.delete_bar.setPlaceholderText("Enter Item or Barcode Number to Delete")


        self.delete_button.setStyleSheet(
                                        """
                                        QPushButton {
                                        font-size: 50px;
                                        background-color: #940a0a;
                                        border-bottom: 3px solid #32353d;
                                        border-top: 3px solid #32353d;
                                        border-right: 3px solid #32353d;
                                        font-weight: bold;
                                        font-family: Comic Sans MS;
                                        color: white;
                                        }
                                        QPushButton:hover {
                                        background-color: #ff0000;
                                        border-bottom: 3px solid white;
                                        border-top: 3px solid white;
                                        border-right: 3px solid white; 
                                        color: white  
                                        }
                                        """
                                        )
        self.delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.delete_button.setFixedWidth(200)
        self.delete_button.setFixedHeight(70)
        self.delete_button.clicked.connect(self.delete_item) 

#----------------------------------------------------------------------------------------------------------------------------------------

        self.save_changes_button.setStyleSheet("""
                                      QPushButton{
                                      font-size: 50px;
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
        self.save_changes_button.setFixedHeight(140)  
        self.save_changes_button.setFixedWidth(350) 
        self.save_changes_button.clicked.connect(self.save_changes)


        self.change_status_label.setStyleSheet("font-size: 75px;"
                                           "background-color: #697480;"
                                           "border-style: solid;"
                                           "border-color: black;"
                                           "border-width: 5px;"
                                           "font-weight: bold;"
                                           "font-family: Comic Sans MS;"
                                           "color: white")
        self.change_status_label.setFixedHeight(140)

#----------------------------------------------------------------------------------------------------------------------------------------

        title_layout.addWidget(self.back_button)
        title_layout.addWidget(self.window_title_label)

        title_layout.setSpacing(0)  
        title_layout.setContentsMargins(0, 0, 0, 0)

        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)
        search_layout.setContentsMargins(20, 15, 20, 15)
        search_layout.setSpacing(0)

        database_layout.addWidget(self.table)
        #database_layout.setAlignment(Qt.AlignCenter)
        database_layout.setContentsMargins(250, 10, 250, 10)

        delete_layout.addWidget(self.delete_bar)
        delete_layout.addWidget(self.delete_button)
        delete_layout.setContentsMargins(20, 15, 20, 15)
        delete_layout.setSpacing(0)

        changes_layout.addWidget(self.save_changes_button)
        changes_layout.addWidget(self.change_status_label)
        changes_layout.setContentsMargins(20, 5, 20, 5)
    

        main_layout.addLayout(title_layout)
        main_layout.addLayout(search_layout)
        main_layout.addLayout(database_layout)
        main_layout.addLayout(delete_layout)
        main_layout.addLayout(changes_layout)

        main_layout.setContentsMargins(0, 0, 0, 10)
        

        self.setLayout(main_layout)


        self.setStyleSheet("background-color: #b1c5de;")

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
    
    def save_changes(self):

        for row in range(self.model.rowCount()):
            index = self.model.index(row, self.model.fieldIndex('item_quantity'))
            item_quantity_value = self.model.data(index)
            if not isinstance(item_quantity_value, int):
                self.save_fail()
                self.change_status_label.setText("Status: Error, Items edited incorrectly.") 

        if self.model.submitAll():
            self.save_success()
            self.change_status_label.setText("Status: Items edited Successfully")   
        else:
            self.save_fail()
            self.change_status_label.setText("Status: Error, Items edited incorrectly.")     
        
    def save_success(self):   
        self.change_status_label.setStyleSheet("font-size: 75px;"
                                                       "background-color: #079c05;"
                                                       "border-style: solid;"
                                                       "border-color: black;"
                                                       "border-width: 5px;"
                                                       "font-weight: bold;"
                                                       "font-family: Comic Sans MS;"
                                                       "color: white") 
    

    def save_fail(self):
        self.change_status_label.setStyleSheet("font-size: 75px;"
                                                    "background-color: #f51d1d;"
                                                    "border-style: solid;"
                                                    "border-color: black;"
                                                    "border-width: 5px;"
                                                    "font-weight: bold;"
                                                    "font-family: Comic Sans MS;"
                                                    "color: white") 

    def search_item(self):
        search_query = self.search_bar.text().strip()

        connect = sqlite3.connect('products.db')
        cursor = connect.cursor()

        filter_condition = f"item_name LIKE '{search_query}%' OR barcode_number LIKE '{search_query}'"
    
        self.model.setFilter(filter_condition)
    
        self.model.select()
 
        connect.commit()
        connect.close()

       

    
        

    def delete_item(self):
        delete_query = self.delete_bar.text().strip()

        connect = sqlite3.connect('products.db')
        cursor = connect.cursor()
        cursor.execute("DELETE FROM products WHERE item_name = ? OR barcode_number = ?", (delete_query, delete_query))  

        connect.commit()
        connect.close()
        self.delete_bar.clear()

        self.model.select()         
