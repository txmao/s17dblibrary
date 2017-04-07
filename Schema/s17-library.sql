/**
Library Schema
*/

DROP SCHEMA IF EXISTS Library;
CREATE SCHEMA Library;
USE Library;

DROP TABLE IF EXISTS BOOK;
CREATE TABLE BOOK (
	Isbn     CHAR(10)       NOT NULL,
	Title    VARCHAR(1000)   NOT NULL,
	CONSTRAINT pk_book 	PRIMARY KEY (Isbn)
);

DROP TABLE IF EXISTS AUTHORS;
CREATE TABLE AUTHORS (
	Author_id    INT            NOT NULL,
	Name         VARCHAR(300)   NOT NULL,
	CONSTRAINT pk_authors PRIMARY KEY (Author_id)
);

DROP TABLE IF EXISTS BOOK_AUTHORS;
CREATE TABLE BOOK_AUTHORS (
	Author_id    INT         NOT NULL,
	Isbn         CHAR(10)    NOT NULL,
	CONSTRAINT pk_book_authors PRIMARY KEY (Author_id, Isbn),
	CONSTRAINT fk_book_authors_book FOREIGN KEY (Isbn) REFERENCES BOOK (Isbn),
	CONSTRAINT fk_book_authors_authors FOREIGN KEY (Author_id) REFERENCES AUTHORS (Author_id)
);

DROP TABLE IF EXISTS BORROWER;
CREATE TABLE BORROWER (
	Card_id     INT           NOT NULL,
	Ssn         CHAR(9)       NOT NULL,
	Bname       VARCHAR(100)  NOT NULL,
	Address     VARCHAR(100)  NOT NULL,
	Phone       CHAR(10)      DEFAULT NULL,
	CONSTRAINT pk_borrower PRIMARY KEY (Card_id)
);

DROP TABLE IF EXISTS BOOK_LOANS;
CREATE TABLE BOOK_LOANS (
	Loan_id     INT         NOT NULL,
	Isbn        CHAR(10)    NOT NULL,
	Card_id     INT         NOT NULL,
	Date_out    DATE        NOT NULL,
	Due_date    DATE        NOT NULL,
	Date_in     DATE,
	CONSTRAINT pk_book_loans PRIMARY KEY (Loan_id),
	CONSTRAINT fk_book_loans_book FOREIGN KEY (Isbn) REFERENCES BOOK (Isbn),
	CONSTRAINT fk_book_loans_borrower FOREIGN KEY (Card_id) REFERENCES BORROWER (Card_id)
);

DROP TABLE IF EXISTS FINES;
CREATE TABLE FINES (
	Loan_id      INT              NOT NULL,
	Fine_amt     DECIMAL(10,2)    DEFAULT 0.00,
	Paid         INT              DEFAULT 0,
	CONSTRAINT pk_fines PRIMARY KEY (Loan_id),
	CONSTRAINT fl_fines_book_loans FOREIGN KEY (Loan_id) REFERENCES BOOK_LOANS (Loan_id)
);

