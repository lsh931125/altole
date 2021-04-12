# 비트코인 시세확인하기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("myWindow2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        # 코인시세 API 요청을 보내고 받은 값을 받아오기
        # print("조회 버튼 클릭")
        price = pykorbit.get_current_price("BTC")
        print(price)
        self.textBrowser.setText(str(price))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()