'''
Created on Mar 8, 2017

Main UI of Library Management System (LMS)

@author: mdy
'''

import sys
from PyQt4 import QtGui, QtCore
from UI.lms import Ui_LibraryUI
from BS_Query import BS_Query
from Boer_Insert import Boer_Insert
from CheckOut import CheckOut
from outBookSearch import outBookSearch
from CheckIn import CheckIn
from FINES_update import FINES_update
from PayFine import PayFine

class LMSui(QtGui.QMainWindow, Ui_LibraryUI):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_LibraryUI.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())#set a fixed size
        self.bsButton.clicked.connect(self.bsButtonOnClick)
        self.clearInfoButtonTab3.clicked.connect(self.clearInfoButtonTab3OnClick)
        self.createNewBorrowerButton.clicked.connect(self.createNewBorrowerButtonOnClick)
        self.coutclearButton.clicked.connect(self.coutclearButtonOnClick)
        self.coutdoButton.clicked.connect(self.coutdoButtonOnClick)
        self.loanSearchButton.clicked.connect(self.loanSearchButtonOnClick)
        self.checkInButton.clicked.connect(self.checkInButtonOnClick)
        self.fineclearButton.clicked.connect(self.fineclearButtonOnClick)
        self.fineinfoupdateButton.clicked.connect(self.fineinfoupdateButtonOnClick)
        self.finepayButton.clicked.connect(self.finepayButtonOnClick)
        return
    
    def finepayButtonOnClick(self):
        Indexes = self.finetableWidget.selectionModel().selectedRows()
        selected_id = []
        selected_id_yon = []
        for Index in Indexes:
            sid = self.finetableWidget.item(Index.row(), 2).text()
            sidyon = self.finetableWidget.item(Index.row(), 4).text()
            selected_id.append(int(sid))
            selected_id_yon.append(str(sidyon))
            
        #print selected_id
        #print selected_id_yon
        if 'no' in selected_id_yon:
            msg1 = 'Please Only Select In Stock (Returned) Books To Pay!'
            self.finetextEdit.setText(msg1)
            return
        else:
            for aid in selected_id:
                PayFine(aid)
                
            self.updateFineInformationList()
            return
        return
    
    def fineinfoupdateButtonOnClick(self):
        self.updateFineInformationList()
        return
    
    def updateFineInformationList(self):
        entered_text = str(self.finelineEdit.text())
        fupdt = FINES_update(entered_text)
        rst3 = fupdt.refre_list1
        #set selection mode for enter payment use
        self.finetableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.finetableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.finetableWidget.setColumnCount(7)
        self.finetableWidget.setHorizontalHeaderLabels(QtCore.QString('Card ID;Name;Loan ID;ISBN;In Stock?;Fine;Total Fine').split(';'))
        self.finetableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.finetableWidget.setRowCount(len(rst3))
        for i in range(len(rst3)):
            info0 = str(rst3[i][0])
            info1 = str(rst3[i][1])
            info2 = str(rst3[i][2])
            info3 = str(rst3[i][3])
            info4 = str(rst3[i][4])
            info5 = str(rst3[i][5])
            info6 = str(rst3[i][6])
            it0 = QtGui.QTableWidgetItem(info0)
            it0.setTextAlignment(QtCore.Qt.AlignCenter)
            it0.setBackgroundColor(QtCore.Qt.green)
            it2 = QtGui.QTableWidgetItem(info2)
            it2.setTextAlignment(QtCore.Qt.AlignRight)
            it4 = QtGui.QTableWidgetItem(info4)
            it4.setTextAlignment(QtCore.Qt.AlignCenter)
            self.finetableWidget.setItem(i, 0, it0)
            self.finetableWidget.setItem(i, 1, QtGui.QTableWidgetItem(info1))
            self.finetableWidget.setItem(i, 2, it2)
            self.finetableWidget.setItem(i, 3, QtGui.QTableWidgetItem(info3))
            self.finetableWidget.setItem(i, 4, it4)
            self.finetableWidget.setItem(i, 5, QtGui.QTableWidgetItem(info5))
            self.finetableWidget.setItem(i, 6, QtGui.QTableWidgetItem(info6))
            
        return
    
    def fineclearButtonOnClick(self):
        self.finelineEdit.clear()
        self.finetextEdit.clear()
        self.finetableWidget.clear()
        self.finetableWidget.setRowCount(0)
        self.finetableWidget.setColumnCount(0)
        return
    
    def checkInButtonOnClick(self):
        Indexes = self.loanSearchtableWidget.selectionModel().selectedRows()
        LID = []
        Ind_row = []
        indtoid = {}
        for Index in Indexes:
            Ind_row.append(Index.row())
            itm = self.loanSearchtableWidget.item(Index.row(), 0).text()
            LID.append(int(itm))
            indtoid.setdefault(Index.row(), int(itm))
            
        #print LID
        #print Ind_row
        #print indtoid
        if len(LID)==0 :
            m1 = 'Please select at least one row in the left table!'
            self.coutmessagetextEdit.setText(m1)
            return
        else:
            #selected not null, do check in
            #when multiple rows selected the key is in ascending order
            cnt = 0
            for key in indtoid:
                self.loanSearchtableWidget.removeRow(key-cnt)
                cnt += 1
                CheckIn(indtoid.get(key))
                
            m2 = 'Check in done for loan id: ' + str(LID)
            self.coutmessagetextEdit.setText(m2)
            pass
        
        return
    
    def loanSearchButtonOnClick(self):
        #self.refreshLoanSearchRst()
        
        str_entered = self.loanSearchlineEdit.text()
        obs = outBookSearch(str(str_entered))
        rst1 = obs.rst_list
        # support select multiple rows
        #self.loanSearchtableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        # select the whole row
        self.loanSearchtableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.loanSearchtableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.loanSearchtableWidget.setColumnCount(6)
        self.loanSearchtableWidget.setHorizontalHeaderLabels(QtCore.QString('Loan ID;Card ID;Name;ISBN;Title;Due Date').split(';'))
        self.loanSearchtableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.loanSearchtableWidget.setRowCount(len(rst1))
        for i in range(len(rst1)):
            linfo0 = str(rst1[i][0])
            linfo1 = str(rst1[i][1])
            linfo2 = rst1[i][2]
            linfo3 = rst1[i][3]
            linfo4 = rst1[i][4]
            linfo5 = rst1[i][5]
            itm0 = QtGui.QTableWidgetItem(linfo0)
            itm0.setTextAlignment(QtCore.Qt.AlignCenter)
            self.loanSearchtableWidget.setItem(i, 0, itm0)
            itm1 = QtGui.QTableWidgetItem(linfo1)
            itm1.setTextAlignment(QtCore.Qt.AlignCenter)
            itm1.setBackgroundColor(QtCore.Qt.yellow)
            self.loanSearchtableWidget.setItem(i, 1, itm1)
            self.loanSearchtableWidget.setItem(i, 2, QtGui.QTableWidgetItem(linfo2))
            self.loanSearchtableWidget.setItem(i, 3, QtGui.QTableWidgetItem(linfo3))
            self.loanSearchtableWidget.setItem(i, 4, QtGui.QTableWidgetItem(linfo4))
            self.loanSearchtableWidget.setItem(i, 5, QtGui.QTableWidgetItem(str(linfo5)))
            
        return
    
    def coutdoButtonOnClick(self):
        mycid = self.coutIDlineEdit.text()
        mycisbn = self.coutISBNlineEdit.text()
        #It is very important to convert mycid to integer values!
        newckot = CheckOut(mycisbn, int(mycid))
        if newckot.isIdGood==0:
            m1 = "Please Check Card Id, it may be invalid, or already borrowed 3 books!"
            self.coutmessagetextEdit.setText(m1)
            
        else:
            if newckot.isIsbnGood==0:
                m2 = "Please Check Isbn, it may be invalid, or not be returned!"
                self.coutmessagetextEdit.setText(m2)
                
            else:
                self.coutmessagetextEdit.setText("Check Out Successfully!")
                
        return
    
    def coutclearButtonOnClick(self):
        self.coutIDlineEdit.clear()
        self.coutISBNlineEdit.clear()
        self.coutmessagetextEdit.clear()
        self.loanSearchlineEdit.clear()
        self.loanSearchtableWidget.clear()
        self.loanSearchtableWidget.setRowCount(0)
        self.loanSearchtableWidget.setColumnCount(0)
        return
    
    def createNewBorrowerButtonOnClick(self):
        Bssn = self.ssn_in.toPlainText()
        Bname = self.name_in.toPlainText()
        Baddr = self.address_in.toPlainText()
        Bphone = self.phone_in.toPlainText()
        ssnf = filter(lambda ch: ch in '0123456789', str(Bssn))
        
        if len(ssnf)!=9 :
            msg1 = 'Input Format Error: Pay Attention to Ssn field!'
            self.message_box.setText(msg1)
            return
        
        if len(ssnf)==9 and len(Bphone)!=0:
            if len(Bphone)!=10:
                msg2 = 'Input Format Error: Pay Attention to Phone fields!'
                self.message_box.setText(msg2)
                return
        if len(str(Baddr))==0:
            msg3 = 'Please Enter Address!'
            self.message_box.setText(msg3)
            return
        
        msg = ''
        nid = 0
        if Bphone=='':
            new_boer_insert = Boer_Insert(Bssn, Bname, Baddr)
            nid = new_boer_insert.newid
            if new_boer_insert.isdistinct==1:
                msg = 'Insert Successful!'
                self.id_out.setText(str(nid))
            else:
                msg = 'Duplicate SSN!'
                
        else:
            new_boer_insert = Boer_Insert(Bssn, Bname, Baddr, Bphone)
            nid = new_boer_insert.newid
            if new_boer_insert.isdistinct==1:
                msg = 'Insert Successful!'
                self.id_out.setText(str(nid))
            else:
                msg = 'Duplicate SSN!'
                
        self.message_box.setText(msg)
        #self.id_out.setText()
        return
    
    def clearInfoButtonTab3OnClick(self):
        self.ssn_in.clear()
        self.name_in.clear()
        self.address_in.clear()
        self.phone_in.clear()
        self.id_out.clear()
        self.message_box.clear()
        return
    
    def bsButtonOnClick(self):
        #string for search
        self.bktableWidget.clearContents()
        enteredString = self.bsEdit.toPlainText()
        book_show_list = BS_Query(str(enteredString)).rst2
        #match
        #ISBN, Book Title, Book Author(s), Book Availability
        self.bktableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.bktableWidget.setColumnCount(4)
        self.bktableWidget.setHorizontalHeaderLabels(QtCore.QString('ISBN;Title;Author;Availability').split(';'))
        self.bktableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.bktableWidget.setRowCount(len(book_show_list))
        for i in range(len(book_show_list)):
            bf0 = book_show_list[i][0]
            bf1 = book_show_list[i][1]
            #bf2 = book_show_list[i][2]
            bf2 = ''
            if len(book_show_list[i][2])==1:
                bf2 += book_show_list[i][2][0]
                
            else:
                for j in range(len(book_show_list[i][2])):
                    if j < len(book_show_list[i][2])-1:
                        bf2 += book_show_list[i][2][j] +', '
                    else:
                        bf2 += book_show_list[i][2][j]
                    
            bf3 = book_show_list[i][3]
            #bf3 = 'yes'
            self.bktableWidget.setItem(i,0,QtGui.QTableWidgetItem(bf0))
            self.bktableWidget.setItem(i,1,QtGui.QTableWidgetItem(bf1))
            self.bktableWidget.setItem(i,2,QtGui.QTableWidgetItem(bf2))
            self.bktableWidget.setItem(i,3,QtGui.QTableWidgetItem(bf3))
            
        return
    
if __name__=='__main__':
    ap = QtGui.QApplication(sys.argv)
    wd = LMSui()
    wd.show()
    sys.exit(ap.exec_())
    
    