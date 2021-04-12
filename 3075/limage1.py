#This program gets two values from a DB into lineEdits.
import sys
import os
from limage import *

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'idplf1'); 
import sqlite3
con = sqlite3.connect('idplf1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.analyse)


  def analyse(self):
    s1 = str(self.ui.lineEdit.text())
    
    if (s1=='eblight.jpg'):
      os.system("python ima_match1.py")
    elif (s1=='anthracnose.jpg'):
      os.system("python ima_match2.py")
    elif (s1=='downy.jpg'):
      os.system("python ima_match3.py")
    elif (s1=='lblight.jpg'):
      os.system("python ima_match4.py")
    elif (s1=='lspot.jpg'):
       os.system("python ima_match5.py") 
           

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
