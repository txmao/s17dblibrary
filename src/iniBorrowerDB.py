'''
Created on Mar 4, 2017
using BorrowersInfo to initialize BORROWER
@author: mdy
'''
from BorrowersInfo import BorrowersInfo
import MySQLdb

class iniBorrowerDB:
    def __init__(self, fpath, myhost, myname, mypass):
        self.populizeBORROWER(fpath, myhost, myname, mypass)
        return
    
    def populizeBORROWER(self, fpath, myhost, myname, mypass):
        #
        borrower_info = BorrowersInfo(fpath)
        infos = borrower_info.borrower_info
        #
        mydb = MySQLdb.connect(myhost, myname, mypass, 'Library')
        csr = mydb.cursor()
        #
        for info in infos:
            csr.execute(
                "INSERT INTO BORROWER (Card_id, Ssn, Bname, Address, Phone) VALUES (%s, %s, %s, %s, %s)",
                info
                )
        
        mydb.commit()
        csr.close()
        
        return
    
if __name__=='__main__':
    fp = '../Data/borrowers.csv'
    myh = 'localhost'
    myn = 'mdy'
    mps = '123mdy'
    iniBorrowerDB(fp, myh, myn, mps)
    
    
    
    
        