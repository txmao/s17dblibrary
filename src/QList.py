'''
Created on Mar 8, 2017

Command Lists Used in this

@author: mdy
'''

#Search all the isbn, title, author of the book
query1 = (
    "SELECT BOOK.Isbn, BOOK.Title, AUTHORS.Name\
     FROM BOOK JOIN BOOK_AUTHORS JOIN AUTHORS ON BOOK.Isbn=BOOK_AUTHORS.Isbn AND BOOK_AUTHORS.Author_id=AUTHORS.Author_id\
     ;"
    )

#select distinct Isbn from BOOK_LOANS Table
query2 = (
    "SELECT Isbn\
     FROM BOOK_LOANS\
     WHERE Date_in IS NULL;"
    )

#search a ssn in the BORROWER
query3 = (
    "SELECT Card_id, Ssn\
     FROM BORROWER\
     ;"
    )

insert1 = (
    "INSERT INTO BORROWER (Card_id, Ssn, Bname, Address, Phone) VALUES (%s, %s, %s, %s, %s)"
    )


# for check out
query4 = (
    "SELECT Isbn FROM BOOK WHERE Isbn=%s"
    )

query5 = (
    "SELECT Isbn\
     FROM BOOK_LOANS\
     WHERE Date_in IS NULL AND Isbn=%s\
    "
    )

query6 = (
    "SELECT Card_id\
     FROM BORROWER\
     WHERE Card_id=%s"
    )

query7 = (
    "SELECT Card_id\
     FROM BOOK_LOANS\
     WHERE Date_in IS NULL\
     GROUP BY Card_id\
     HAVING COUNT(*)>=3\
     ;"
    )

query8 = (
    "SELECT COUNT(*)\
     FROM BOOK_LOANS\
     ;"
    )

# for insert to BOOK_LOANS
insert2 = (
    "INSERT INTO BOOK_LOANS (Loan_id, Isbn, Card_id, Date_out, Due_Date, Date_in) VALUES (%s, %s, %s, %s, %s, %s)"
    )

#do check in, update the Date_in attribute
update1 = (
    "UPDATE BOOK_LOANS SET Date_in=%s WHERE Loan_id=%s"
    )

#search the out of stock book
query9 = (
    "SELECT BL.Loan_id, BL.Card_id, BR.Bname, BL.Isbn, BK.Title, BL.Due_date\
     FROM BOOK_LOANS AS BL JOIN BORROWER AS BR JOIN BOOK AS BK ON BL.Card_id=BR.Card_id AND BL.Isbn=BK.Isbn\
     WHERE BL.Date_in IS NULL\
     ORDER BY BL.Card_id"
    )

#used to determine which Loan_id is a passed due one
query11 = (
    "SELECT B.Loan_id, B.Date_out, B.Due_date, B.Date_in\
     FROM BOOK_LOANS AS B\
     WHERE (B.Date_in>B.Due_date OR B.Date_in IS NULL AND B.Due_date<%s)\
     AND B.Loan_id NOT IN (SELECT F.Loan_id FROM FINES AS F WHERE F.Paid=1)"
    )

#all the unpaid Loan(Loan_id) in FINES
query12 = ("SELECT Loan_id FROM FINES WHERE Paid=0")

#update FINES where paid==0
update2 = (
    "UPDATE FINES SET Fine_amt=%s, Paid=%s WHERE Loan_id=%s"
    )

#insert new FINES id
insert3 = (
    "INSERT INTO FINES (Loan_id, Fine_amt, Paid) VALUES (%s, %s, %s)"
    )

#view the final results after update the whole, last step in FINES_update
query13 = (
    "SELECT BO.Card_id, BO.Bname, BL.Loan_id, BL.Isbn, F.Fine_amt, BL.Date_in\
     FROM BORROWER AS BO, BOOK_LOANS AS BL, FINES AS F\
     WHERE BO.Card_id=BL.Card_id AND BL.Loan_id=F.Loan_id AND F.Paid=0\
     GROUP BY BL.Card_id, BL.Loan_id\
     ORDER BY BL.Card_id"
    )

#query for fine unpaid but checked in books
query14 = (
    "SELECT Loan_id\
     FROM BOOK_LOANS\
     WHERE Date_in>Due_date AND Loan_id IN (SELECT Loan_id FROM FINES WHERE Paid=0)"
    )

#pay for a specific id
update3 = (
    "UPDATE FINES SET Paid=1 WHERE Loan_id=%s"
    )

