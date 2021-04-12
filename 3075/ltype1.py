#This program gets two values from a DB into lineEdits.
import sys
import os
from ltype import *
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
     self.ui.pushButton.clicked.connect(self.insertvalues)
     #self.ui.pushButton_2.clicked.connect(self.temprtdetails) 


  def insertvalues(self):
    with con:
      cur = con.cursor()
      s4 = str(self.ui.lineEdit_4.text())
      s5 = str(self.ui.lineEdit_5.text())
      s6 = str(self.ui.lineEdit_6.text())
      s7 = str(self.ui.lineEdit_7.text())
      if (s4=='Y'):
        cur.execute('INSERT INTO ltype(leaftype) VALUES("unknown")')
      elif (s5=='Y'):
        cur.execute('INSERT INTO ltype(leaftype) VALUES("Younger")')
      elif (s6=='Y'):
        cur.execute('INSERT INTO ltype(leaftype) VALUES("Mid_Aged")')
      elif (s7=='Y'):
        cur.execute('INSERT INTO ltype(leaftype) VALUES("older")')
      con.commit()

  def temprtdetails(self):
    os.system("python temprt1.py")     

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
