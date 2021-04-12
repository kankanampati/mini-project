#This program gets two values from a DB into lineEdits.
import sys
import os
from ptype import *
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
     #self.ui.pushButton_2.clicked.connect(self.leafdetails)

  def insertvalues(self):
    with con:
      cur = con.cursor()
      s4 = str(self.ui.lineEdit_4.text())
      s5 = str(self.ui.lineEdit_5.text())
      s6 = str(self.ui.lineEdit_6.text())
      s7 = str(self.ui.lineEdit_7.text())
      s8 = str(self.ui.lineEdit_8.text())
      s9 = str(self.ui.lineEdit_9.text())
      s10 = str(self.ui.lineEdit_10.text())
      s11 = str(self.ui.lineEdit_11.text())
      s12 = str(self.ui.lineEdit_12.text())
      s13 = str(self.ui.lineEdit_13.text())
      if (s4=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("unknown")')
      elif (s5=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Blue Berries")')
      elif (s6=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Goji Berries")')
      elif (s7=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Black Berries")')
      elif (s8=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Straw Berries")')
      elif (s9=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Rasp Berries")')
      elif (s10=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Bil Berries")')
      elif (s11=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Acai Berries")')
      elif (s12=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Grape Berries")')
      elif (s13=='Y'):
        cur.execute('INSERT INTO ptype(planttype) VALUES("Cran Berries")')
      con.commit()

  def leafdetails(self):
    os.system("python ltype1.py")     

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
