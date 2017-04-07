'''
Created on Mar 4, 2017
Parse the borrowers.csv for initial population 
@author: mdy
'''

import csv

class BorrowersInfo:
    def __init__(self, borrower_csv_path):
        self.f_path = borrower_csv_path
        # store the initial 9 column information
        # [id, ssn, fname, lname, email, address, city, state, phone]
        self.raw_info = []
        # the same with raw_info, but the column format are modified for the format
        self.raw_info1 = []
        # [id, ssn, bname, address, phone], 5 column format for insert
        self.borrower_info = []
        
        self.extract_info()
        return
    
    def extract_info(self):
        f_path = self.f_path
        with open(f_path) as fl:
            rd = csv.reader(fl)
            rows = [row for row in rd]
            
        self.raw_info = rows
        for i in range(1, len(rows)):
            ri0 = int(rows[i][0])
            ri1 = rows[i][1].replace('-', '')
            ri2 = rows[i][2]
            ri3 = rows[i][3]
            ri4 = rows[i][4]
            ri5 = rows[i][5]
            ri6 = rows[i][6]
            ri7 = rows[i][7]
            ri8 = rows[i][8].replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            ri_list = [ri0, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8]
            self.raw_info1.append(ri_list)
            # construct the insert value
            be0 = ri0
            be1 = ri1
            be2 = ri2+' '+ri3
            be3 = ri5+', '+ri6+', '+ri7
            be4 = ri8
            be_list = [be0, be1, be2, be3, be4]
            self.borrower_info.append(be_list)
            
        
        return
    
if __name__=='__main__':
    fp = '../Data/borrowers.csv'
    ber = BorrowersInfo(fp)
    
    print ber.raw_info[0]
    print ber.raw_info[1]
    print ber.raw_info1[0]
    print ber.borrower_info[800]
    
    
        
        
        
        
        