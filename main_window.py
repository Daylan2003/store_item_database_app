from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Item Database")
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png"))

        self.label = QLabel("Choose an option", self)
        self.add_item_button = QPushButton("Add Item", self)
        self.lookup_item_button = QPushButton("Lookup Item", self)
        self.initUI()

        # Initialize window references
        self.add_window = None
        self.lookup_window = None

    def initUI(self):
        self.add_item_button.setGeometry(100, 200, 300, 300)
        self.add_item_button.setStyleSheet("font-size: 30px;")  
        self.add_item_button.clicked.connect(self.add_item_clicked)  

        self.lookup_item_button.setGeometry(600, 200, 300, 300)
        self.lookup_item_button.setStyleSheet("font-size: 30px;")
        self.lookup_item_button.clicked.connect(self.lookup_item_clicked)

        self.label.setGeometry(540, 50, 200, 50)
        self.label.setStyleSheet("font-size: 24px;")

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





 








