'''
Created on Mar 5, 2017

@author: mdy
'''
import sys
from PyQt4 import QtGui, QtCore
from UI.myui1 import Ui_Library_MainWindow

class MyApp1(QtGui.QMainWindow, Ui_Library_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_Library_MainWindow.__init__(self)
        self.setupUi(self)
        self.Search_Button.clicked.connect(self.iop)
        
    def iop(self):
        p = self.Search_Box.toPlainText()
        self.test_my.setText(p)
        #self.Show_Table.setHorizontalHeaderLabels(QtCore.QString("fuck;milk;best;mine;").split(';'))
        self.Show_Table.setColumnCount(4)
        self.Show_Table.setHorizontalHeaderLabels(QtCore.QString("fuck;milk;best;mine;").split(';'))
        self.Show_Table.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.Show_Table.setRowCount(100)
        self.Show_Table.setItem(0,0,QtGui.QTableWidgetItem(p))
        self.Show_Table.setItem(0,1,QtGui.QTableWidgetItem("Sugi"))
        self.Show_Table.setItem(1,0,QtGui.QTableWidgetItem("hagi"))
        
        ind = self.Show_Table.selectionModel().selectedRows()
        for index in sorted(ind):
            #print index.row()
            itm = self.Show_Table.itemAt(index.row(), 0)
            print index.row()
            print itm.text()
        
if __name__=='__main__':
    ap = QtGui.QApplication(sys.argv)
    wd = MyApp1()
    wd.show()
    sys.exit(ap.exec_())