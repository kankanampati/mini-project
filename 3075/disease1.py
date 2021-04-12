#This program gets two values from a DB into lineEdits.
import sys
import os
from disease import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('idplf1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'idplf1'); 

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.leafimage)    

  def leafimage(self):
    os.system("python limage1.py")     

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
