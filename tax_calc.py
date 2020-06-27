# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dada\Documents\QT\tax\tax_calc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tax_Calculator(object):
    def setupUi(self, Tax_Calculator):
        Tax_Calculator.setObjectName("Tax_Calculator")
        Tax_Calculator.resize(800, 592)
        Tax_Calculator.setMinimumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Tax_Calculator.setFont(font)
        Tax_Calculator.setStyleSheet("QTextEdit#textEdit_output{\n"
"color:rgb(0, 0, 0);\n"
"background color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"color:rgb(0, 85, 127);\n"
"border: 2px rgb(170, 170, 255);\n"
"border-radius: 10px;\n"
"padding:0 8px;\n"
"background: qconicalgradient(cx:0.755682, cy:0.682, angle:5, stop:0 rgba(183, 131, 246, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"QLineEdit#lineEdit_price{\n"
"color:rgb(0, 0, 0);\n"
"border: 2px rgb(85, 0, 0);\n"
"border:10px  rgb(255, 85, 0) ;\n"
"border-radius: 10px;\n"
"padding:10 8px\n"
"}\n"
"QDoubleSpinBox#doubleSpinBox_rate{\n"
"color:rgb(0, 0, 0);\n"
"border: 2px rgb(170, 170, 255);\n"
"border:1px  rgb(170, 170, 255) ;\n"
"border-radius: 10px;\n"
"padding:0 8px\n"
"}\n"
"\n"
"*\n"
"{\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(106, 146, 246, 255), stop:0.488636 rgba(129, 79, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Tax_Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 70, 846, 604))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_EnterPrice = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_EnterPrice.setFont(font)
        self.label_EnterPrice.setObjectName("label_EnterPrice")
        self.gridLayout.addWidget(self.label_EnterPrice, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.lineEdit_price = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setAutoFillBackground(False)
        self.lineEdit_price.setStyleSheet("")
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.gridLayout.addWidget(self.lineEdit_price, 0, 4, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 8, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.label_TaxRate = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_TaxRate.setFont(font)
        self.label_TaxRate.setObjectName("label_TaxRate")
        self.gridLayout.addWidget(self.label_TaxRate, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 2)
        self.doubleSpinBox_rate = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.doubleSpinBox_rate.setFont(font)
        self.doubleSpinBox_rate.setMouseTracking(False)
        self.doubleSpinBox_rate.setMinimum(7.5)
        self.doubleSpinBox_rate.setSingleStep(0.01)
        self.doubleSpinBox_rate.setObjectName("doubleSpinBox_rate")
        self.gridLayout.addWidget(self.doubleSpinBox_rate, 2, 4, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 6, 1, 4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 4, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 7, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 5, 5, 1, 1)
        self.textEdit_output = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_output.sizePolicy().hasHeightForWidth())
        self.textEdit_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_output.setFont(font)
        self.textEdit_output.setLineWidth(2)
        self.textEdit_output.setObjectName("textEdit_output")
        self.gridLayout.addWidget(self.textEdit_output, 6, 4, 1, 5)
        spacerItem11 = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 7, 0, 1, 5)
        spacerItem12 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 7, 9, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 9, 5, 1, 1)
        Tax_Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tax_Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Tax_Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tax_Calculator)
        self.statusbar.setObjectName("statusbar")
        Tax_Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Tax_Calculator)
        QtCore.QMetaObject.connectSlotsByName(Tax_Calculator)

    def retranslateUi(self, Tax_Calculator):
        _translate = QtCore.QCoreApplication.translate
        Tax_Calculator.setWindowTitle(_translate("Tax_Calculator", "Tax Calculator"))
        self.label_EnterPrice.setText(_translate("Tax_Calculator", "ENTER PRICE"))
        self.label_TaxRate.setText(_translate("Tax_Calculator", "TAX RATE"))
        self.pushButton.setText(_translate("Tax_Calculator", "CALCULATE TAX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tax_Calculator = QtWidgets.QMainWindow()
    ui = Ui_Tax_Calculator()
    ui.setupUi(Tax_Calculator)
    Tax_Calculator.show()
    sys.exit(app.exec_())
