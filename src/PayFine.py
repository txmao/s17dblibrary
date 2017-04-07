'''
Created on Mar 13, 2017

@author: mdy
'''

import MySQLdb
from QList import *

class PayFine:
    def __init__(self, PayID, hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library'):
        self.isIDvalid = 0
        self.needtopaylist = []
        self.payforid(PayID, hst, usr, pwd, dtbs)
        return
    
    def payforid(self, PayID, hst, usr, pwd, dtbs):
        mydb = MySQLdb.connect(hst, usr, pwd, dtbs)
        csr = mydb.cursor()
        csr.execute(query14)
        for item in csr:
            self.needtopaylist.append(item[0])
            
        if PayID not in self.needtopaylist:
            return
        else:
            self.isIDvalid = 1
            csr.execute(update3, [PayID])
            mydb.commit()
            
        csr.close()
        mydb.close()
        return
    
if __name__=='__main__':
    pf = PayFine(3)
    print pf.needtopaylist
    print pf.isIDvalid
    
    
    