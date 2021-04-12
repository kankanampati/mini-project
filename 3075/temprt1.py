#This program gets two values from a DB into lineEdits.
import sys
import os
from temprt import *
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
     #self.ui.pushButton_2.clicked.connect(self.moistdetails) 

  def insertvalues(self):
    with con:
      cur = con.cursor()
      s4 = str(self.ui.lineEdit_4.text())
      s5 = str(self.ui.lineEdit_5.text())
      s6 = str(self.ui.lineEdit_6.text())
      s7 = str(self.ui.lineEdit_7.text())
      if (s4=='Y'):
        cur.execute('INSERT INTO temprt(temparature) VALUES("unknown")')
      elif (s5=='Y'):
        cur.execute('INSERT INTO temprt(temparature) VALUES("Low")')
      elif (s6=='Y'):
        cur.execute('INSERT INTO temprt(temparature) VALUES("Medium")')
      elif (s7=='Y'):
        cur.execute('INSERT INTO temprt(temparature) VALUES("High")')
      con.commit()

  def moistdetails(self):
    os.system("python moist1.py")     

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
