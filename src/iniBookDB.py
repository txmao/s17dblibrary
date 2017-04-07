'''
Created on Mar 2, 2017
using BooksInfo to Initialize BOOK, AUTHORS, BOOK_AUTHORS
@author: mdy
'''
import MySQLdb
from BooksInfo import BooksInfo
from pip._vendor.distlib import database

class iniBookDB:
    def __init__(self, books_csv_file_path, myhost, myuser, mypasswd):
        self.ini_populate_BOOK_related_table(books_csv_file_path, myhost, myuser, mypasswd)
        return
    
    def ini_populate_BOOK_related_table(self, books_csv_file_path, myhost, myuser, mypasswd):
        book_info = BooksInfo(books_csv_file_path)
        data_base = MySQLdb.connect(host=myhost, user=myuser, passwd=mypasswd, db='Library')
        cursor = data_base.cursor()
        isbntitle = book_info.isbn_title
        authoridname = book_info.authorid_name
        authoridisbn = book_info.authorid_isbn
        for row in isbntitle:
            cursor.execute(
                "INSERT INTO BOOK(Isbn, Title) VALUES(%s, %s)",
                row
                )
         
        for row in authoridname:
            cursor.execute(
                "INSERT INTO AUTHORS(Author_id, Name) VALUES(%s, %s)",
                row
                )
        
        for row in authoridisbn:
            cursor.execute(
                "INSERT INTO BOOK_AUTHORS(Author_id, Isbn) VALUES(%s, %s)",
                row
                )
            
        data_base.commit()
        cursor.close()
        return
    
if __name__=='__main__':
    book_csv_path = '../Data/books.csv'
    myhost = 'localhost'
    myuser = 'mdy'
    mypasswd = '123mdy'
    iniBookDB(book_csv_path, myhost, myuser, mypasswd)
    
        
        
        
        