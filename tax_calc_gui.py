import sys
from decimal import Decimal

from PyQt5 import QtCore, QtGui,QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton
from tax_calc import Ui_Tax_Calculator
from tax_calc import *

class MyWindow(QMainWindow,Ui_Tax_Calculator):
        def __init__(self):
                super().__init__()
                self.ui =Ui_Tax_Calculator()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.CalculateTax)
        def CalculateTax(self):
                price = Decimal(self.lineEdit_price.text())
                tax = Decimal(self.doubleSpinBox_rate.value())
                total_price = price + (price*(tax/100))
                total_price_str = "The tax inclusive price is : {:.2f}".format(total_price)
                self.textEdit_output.setText(total_price_str)
        



if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
