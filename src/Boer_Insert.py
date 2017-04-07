'''
Created on Mar 9, 2017

Used to insert Borrower into the Library Schema

@author: mdy
'''
import MySQLdb
from QList import *

class Boer_Insert:
    def __init__(self, Bssn, Bname, Baddr, Bphone=None, hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library'):
        self.InsertInfo = [Bssn, Bname, Baddr, Bphone]
        self.isdistinct = 1
        self.idisbn = []
        self.max_id = []
        self.newid = 0
        self.conductInsert(hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library')
        return
    
    def conductInsert(self, hst, usr, pwd, dtbs):
        info = self.InsertInfo
        mydb = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtbs)
        cursor = mydb.cursor()
        cursor.execute(query3)
        id_max = 0
        for item in cursor:
            self.idisbn.append(item)
            if item[0]>id_max:
                id_max = item[0]
                
            if item[1] == info[0]:
                self.isdistinct = 0
                
        self.max_id = id_max
        
        # if the insert ssn is distinct, then insert
        if self.isdistinct==1:
            new_id = self.max_id+1
            new_tp = [new_id, info[0], info[1], info[2], info[3]]
            self.newid = new_id
            #cursor.execute("INSERT INTO BORROWER (Card_id, Ssn, Bname, Address, Phone) VALUES (%s, %s, %s, %s, %s)", new_tp)
            cursor.execute(insert1, new_tp)
            
            pass
        
        mydb.commit()
        cursor.close()
        return
    
if __name__=='__main__':
    bist = Boer_Insert('666666666', 'D. Mao', 'UT Dallas')
    #bist = Boer_Insert('343434343', 'Harry Shum', 'White House')
    kk = '3456a'
    print len(filter(str.isalnum, kk))
    print len(kk)
    
    