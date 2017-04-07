'''
Created on Mar 11, 2017

Do Check, changes only happen in BOOK_LOANS, using Loan_id (primary key)

@author: mdy
'''

import MySQLdb
from QList import *
import datetime

class CheckIn:
    def __init__(self, CIloanid, hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library'):
        self.doCheckIn(CIloanid, hst, usr, pwd, dtbs)
        return
    
    def doCheckIn(self, CIloanid, hst, usr, pwd, dtbs):
        mydb = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtbs)
        csr = mydb.cursor()
        CIdate = datetime.datetime.now().strftime('%Y-%m-%d')
        update_info = [CIdate, CIloanid]
        csr.execute(update1, update_info)
        mydb.commit()
        csr.close()
        mydb.close()
        return
    
if __name__=='__main__':
    CheckIn(3)
    