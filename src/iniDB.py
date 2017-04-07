'''
Created on Mar 13, 2017

@author: mdy
'''
from iniBookDB import iniBookDB
from iniBorrowerDB import iniBorrowerDB

if __name__=='__main__':
    # popularize book related relation
    book_csv_path = '../Data/books.csv'
    myhost = 'localhost'
    myuser = 'mdy'
    mypasswd = '123mdy'
    iniBookDB(book_csv_path, myhost, myuser, mypasswd)
    # popularize borrower related relation
    fp = '../Data/borrowers.csv'
    myh = 'localhost'
    myn = 'mdy'
    mps = '123mdy'
    iniBorrowerDB(fp, myh, myn, mps)