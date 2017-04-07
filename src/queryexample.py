'''
Created on Mar 5, 2017

@author: mdy
'''
import mysql.connector

cnx = mysql.connector.connect(host='localhost', user='mdy', passwd='123mdy' ,database='Library')
cursor = cnx.cursor()

query = ("SELECT * FROM BORROWER WHERE Card_id='1'")
query1 = (
    "SELECT BOOK.Isbn, BOOK.Title, AUTHORS.Name\
     FROM BOOK JOIN BOOK_AUTHORS JOIN AUTHORS ON BOOK.Isbn=BOOK_AUTHORS.Isbn AND BOOK_AUTHORS.Author_id=AUTHORS.Author_id\
     WHERE BOOK.Isbn='0195153448'"
    )

cursor.execute(query1)

for item in cursor:
    print item
    
cursor.close()
cnx.close()