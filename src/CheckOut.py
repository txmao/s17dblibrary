'''
Created on Mar 9, 2017

module for check out a book, given Isbn and Card_id

1. Isbn wrong
2. Isbn right, but Isbn in BOOK_LOANS and Date_in is null
3. Isbn right, and Isbn not in BOOK_LOANS, or Isbn in BOOK_LOANS and Date_in not null

4. id wrong
5. id right, but id have 3 correspondence in BOOK_LOANS where Date_in not NULL
6. id right, id not in BOOK_LOANS, or id in BOOK_LOANS and have less 3 correspondence where Date_in not null

@author: mdy
'''

import MySQLdb
from QList import *
import copy
import datetime

class CheckOut:
    def __init__(self, coIsbn, coCid, hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library'):
        self.coIsbn = coIsbn
        self.coCid = coCid
        self.host = hst
        self.user = usr
        self.passwd = pwd
        self.db = dtbs
        self.all_isbn = []
        self.out_isbn = []
        self.isIsbnGood = 0
        self.all_id = []
        self.full_id = []
        self.isIdGood = 0
        self.maxLid = 0
        self.doCheckOut(coIsbn, coCid, hst, usr, pwd, dtbs)
        return
    
    def doCheckOut(self, coIsbn, coCid, hst, usr, pwd, dtbs):
        mydb = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtbs)
        cursor = mydb.cursor()
        
        cnt1 = 0
        cursor.execute(query4, [coIsbn])
        for item in cursor:
            cnt1 += 1
            
        #print cnt1
        
        cnt2 = 0
        cursor.execute(query5, [coIsbn])
        for item in cursor:
            cnt2 += 1
            
        #print cnt2
        
        cnt3 = 0
        cursor.execute(query6, [coCid])
        for item in cursor:
            cnt3 += 1
            
        #print cnt3
        
        cnt4 = 0
        cursor.execute(query7)
        for item in cursor:
            self.full_id.append(item[0])
        
        fid = copy.deepcopy(self.full_id)    
        if coCid in fid:
            cnt4 = 1
            
        #print cnt4
        
        cursor.execute(query8)
        for item in cursor:
            self.maxLid = item[0]
            
        #print self.maxLid
        if cnt1==1 and cnt2==0 :
            self.isIsbnGood = 1
            
        if cnt3==1 and cnt4==0 :
            self.isIdGood = 1
            
        
        if (self.isIdGood==1) and (self.isIsbnGood==1) :
            newLid = self.maxLid + 1
            newLisbn = coIsbn
            newLCid = coCid
            #time.strftime('%Y-%m-%d %H:%M:%S')
            #newLDout = time.strftime('%m-%d-%Y %H:%M:%S')
            newLDout = datetime.datetime.now().strftime('%Y-%m-%d')
            #newLDout = time.time()
            #set due date is one day latter for convenience!
            newLDdue = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            newtuple = (newLid, newLisbn, newLCid, newLDout, newLDdue, None)
            cursor.execute(insert2, newtuple)
            mydb.commit()
        else:
            pass
            
        
        cursor.close()
        mydb.close()
            
        return
        
    
if __name__=='__main__':
    CheckOut('0385508042', 1)
    CheckOut('0440241537', 1)
    CheckOut('0739302213', 1)
    print CheckOut('0940322587', 1).full_id[0]
    dt5 = CheckOut('0060194995', 1)
    print 0.25*9
    pass
