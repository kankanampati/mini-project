#This program gets two values from a DB into lineEdits.
import sys
import os
from idplf import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.ldetails)
     self.ui.pushButton_2.clicked.connect(self.tempdetails)
     self.ui.pushButton_3.clicked.connect(self.moistdetails)
     self.ui.pushButton_4.clicked.connect(self.limage)
     self.ui.pushButton_5.clicked.connect(self.pdetails)

  def ldetails(self):
    os.system("python ltype1.py")

  def pdetails(self):
    os.system("python ptype1.py")

  def tempdetails(self):
    os.system("python temprt1.py")

  def moistdetails(self):
    os.system("python moist1.py")

  def limage(self):
    os.system("python limage1.py")

  #def dimage(self):
	#os.system("python disease1.py")
       
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
