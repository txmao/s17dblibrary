'''
Created on Mar 13, 2017

@author: mdy
'''
import sys
from PyQt4 import QtGui
from LMSui import LMSui

if __name__=='__main__':
    ap = QtGui.QApplication(sys.argv)
    wd = LMSui()
    wd.show()
    sys.exit(ap.exec_())