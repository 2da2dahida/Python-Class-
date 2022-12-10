

import sys                           
from PyQt5.QtWidgets import *        
from PyQt5 import uic                
import pybithumb                     
from PyQt5.QtCore import *


tickers = ["BTC", "ETH", "XRP" , "ADA"]

form_class = uic.loadUiType("mywindow3.ui")[0]  

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

        
    def btn_clicked(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0 , item)

            price = pybithumb.get_current_price(ticker)
            self.tableWidget.setItem(i, 1 , QTableWidgetItem(str(price)))



app = QApplication(sys.argv) # 윈도우 창띄우기
window = MyWindow()
window.show()

app.exec_()