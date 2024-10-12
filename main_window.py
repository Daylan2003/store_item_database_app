from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Item Database")
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\cart.png"))

        self.title_label = QLabel("Store Item Database", self)
        self.add_item_button = QPushButton(self)
        self.add_item_button.setIcon(QIcon('images\\more.png'))
        self.add_item_button.setIconSize(QSize(450, 450))
        self.lookup_item_button = QPushButton(self)
        self.lookup_item_button.setIcon(QIcon('images\\search.png'))
        self.lookup_item_button.setIconSize(QSize(450, 450))
        self.initUI()

        self.add_window = None
        self.lookup_window = None

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

      
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        

       
        self.title_label.setStyleSheet("font-size: 75px;"
                                       "background-color: #1256b0;"
                                       "border-style: solid;"
                                       "border-color: black;"
                                       "border-width: 5px;"
                                       "font-weight: bold;"
                                       "font-family: Comic Sans MS;"
                                       "color: white")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFixedHeight(140)  

     
        self.add_item_button.setStyleSheet("""                                        
                                           QPushButton{
                                           font-size: 60px;
                                           background-color: #10ceeb;
                                           border-style: solid;
                                           border-color: black;
                                           border-width: 15px;
                                           font-weight: bold; 
                                           border-radius: 75px;      
                                           }
                                           QPushButton:hover{
                                           background-color: #3a8fde;
                                           border-color: white;
                                           }
                                           QPushButton:pressed{
                                           border-color: black;
                                           }
                                           """)
        self.add_item_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.add_item_button.clicked.connect(self.add_item_clicked)
        self.add_item_button.setCursor(Qt.PointingHandCursor)  

        self.lookup_item_button.setStyleSheet("""                                        
                                           QPushButton{
                                           font-size: 60px;
                                           background-color: #10ceeb;
                                           border-style: solid;
                                           border-color: black;
                                           border-width: 15px; 
                                           font-weight: bold;  
                                           border-radius: 75px;        
                                           }
                                           QPushButton:hover{
                                           background-color: #3a8fde;
                                           border-color: white;
                                           }
                                           QPushButton:pressed{
                                           border-color: black;
                                           }
                                           """)
        self.lookup_item_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lookup_item_button.clicked.connect(self.lookup_item_clicked)
        self.lookup_item_button.setCursor(Qt.PointingHandCursor) 


        self.setStyleSheet("background-color: #b1c5de;")
       

        
        button_layout.addWidget(self.add_item_button)
        button_layout.addWidget(self.lookup_item_button)
        button_layout.setContentsMargins(75, 50, 75, 50)
        button_layout.setSpacing(75)

       
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(button_layout)
        main_layout.setContentsMargins(0, 0, 0, 10)

       
        central_widget.setLayout(main_layout)


    def add_item_clicked(self):
        print("Add item window open")  
        from add_window import AddWindow
        if self.add_window is None:  
            self.add_window = AddWindow()
        self.add_window.show()
        self.close()

    def lookup_item_clicked(self):
        print("Lookup item window open") 
        from lookup_window import LookupWindow 
        if self.lookup_window is None:  
            self.lookup_window = LookupWindow()
        self.lookup_window.show()
        self.close()






 








