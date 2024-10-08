from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Item Database")
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png"))

        self.title_label = QLabel("Store Item Database", self)
        self.add_item_button = QPushButton("Add Item", self)
        self.lookup_item_button = QPushButton("Lookup Item", self)
        self.initUI()

        self.add_window = None
        self.lookup_window = None

        window_width = self.width()
        window_height = self.height()

    def initUI(self):


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        button_layout = QHBoxLayout()
        main_layout = QVBoxLayout()

      

      
        self.add_item_button.setStyleSheet("font-size: 30px;"
                                           "background-color: #10ceeb;"
                                           "border-style: solid;"
                                           "border-color: black;"
                                           "border-width: 5px;")  
        self.add_item_button.clicked.connect(self.add_item_clicked) 
        self.add_item_button.setMinimumSize(300, 300)


    
        self.lookup_item_button.setStyleSheet("font-size: 30px;"
                                              "background-color: #10ceeb;"
                                              "border-style: solid;"
                                              "border-color: black;"
                                              "border-width: 5px;")
        self.lookup_item_button.clicked.connect(self.lookup_item_clicked)
        self.lookup_item_button.setMinimumSize(300, 300)
        

       
        self.title_label.setMinimumHeight(150)
        self.title_label.setStyleSheet("font-size: 24px;"
                                       "background-color: green;"
                                       "border-style: solid;"
                                       "border-color: black;"
                                       "border-width: 5px;")
        
       
        
        

        self.setStyleSheet("background-color: #e9f0ea;")

        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.title_label.setAlignment(Qt.AlignCenter)  

        # Set the main layout
        button_layout.addWidget(self.add_item_button)
        button_layout.addWidget(self.lookup_item_button)
        main_layout.addWidget(self.title_label, 0)  
        main_layout.addLayout(button_layout, 1) 
    

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





 








