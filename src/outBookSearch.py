'''
Created on Mar 11, 2017

search the books that are checked out (not in library) now
Loan_id, Card_id, Bname, Title, Isbn

@author: mdy
'''

import MySQLdb
from QList import *

class outBookSearch:
    def __init__(self, enteredcontent, hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library'):
        self.ent_str = enteredcontent
        self.raw_list = []
        self.rst_list = []
        self.doSearch(hst, usr, pwd, dtbs)
        return
    
    def doSearch(self, hst, usr, pwd, dtbs):
        etstr = self.ent_str.replace(' ', '').lower()
        #print etstr
        mydb = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtbs)
        cursor = mydb.cursor()
        cursor.execute(query9)
        for item in cursor:
            self.raw_list.append(item)
            itemstr = ''
            for ite in item:
                itemstr += str(ite)
                
            itemstr = itemstr.replace(' ', '').lower()
            #print itemstr
            if etstr in itemstr:
                self.rst_list.append(item)
                
            pass
        
        cursor.close()
        mydb.close()
        return
    
if __name__=='__main__':
    myet = ''
    mo = outBookSearch(myet)
    print mo.rst_list[0]
    
    
    