import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 700, 700)
        self.setWindowTitle("가상화폐 트레이딩봇")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()