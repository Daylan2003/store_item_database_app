from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QIcon
from main_window import MainWindow

class AddWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Item")
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowIcon(QIcon("C:\\Users\\mahar\\Desktop\\price-tracker\\images\\Screenshot 2024-06-12 212403.png"))    

        self.add_title_label = QLabel("Add an item to the database", self)   
        self.back_button = QPushButton("Back", self) 

        self.initUI() 

        self.main_window = None

    def initUI(self):  
        self.add_title_label.setGeometry(50, 50, 400, 50)  

        self.back_button.setGeometry(0, 0, 100, 50)
        self.back_button.clicked.connect(self.go_back) 

    def go_back(self):

        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.close()    