'''
Created on Mar 11, 2017

Used to update FINES table

1. passed due but already returned, Date_in>Due_date
2. passed due and not returned, Date_in IS NULL and Today>Due_date
3. if Paid==1 in FINES, then these Loan_id will be ignored!

##
2 scenarios for update
 if Loan_id in FINES and Paid==0, update
 if Loan_id not in FINES, insert
##

@author: mdy
'''

import MySQLdb
import datetime
from QList import *

class FINES_update:
    def __init__(self, srchstr, hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library'):
        self.srch_str = srchstr
        self.late_info_list = []
        #update following into the FINES
        self.fine_info_list = []
        self.fine_amount_changed_id_list = []
        self.former_unpaid_id_list = []
        self.cardid_sumfine = {}
        self.refre_list = []
        self.refre_list1 = []
        self.fillFINES(hst, usr, pwd, dtbs)
        return
    
    def fillFINES(self, hst, usr, pwd, dtbs):
        #record the date of today
        #today_date = ( datetime.datetime.now() + datetime.timedelta(12) ).strftime('%Y-%m-%d')
        today_date = ( datetime.datetime.now() ).strftime('%Y-%m-%d')
        #print today_date
        mydb = MySQLdb.connect(hst, usr, pwd, dtbs)
        csr = mydb.cursor()
        csr.execute(query11, [today_date])
        for ite in csr:
            self.late_info_list.append(ite)
            lid = ite[0]
            self.fine_amount_changed_id_list.append(lid)
            lout = ite[1]
            ldue = ite[2]
            lin = ite[3] # shows whether in
            lfam = 0
            lpay = 0
            w_in = ''
            if lin!=None:
                w_in = 'yes'
                lpay = 0
                lfam = (lin - ldue).days * 0.25
            else:
                w_in = 'no'
                lpay = 0
                lfam = (datetime.datetime.strptime(today_date, '%Y-%m-%d').date() - ldue).days * 0.25
                
            fn_info = [lid, lfam, lpay]
            self.fine_info_list.append(fn_info)
            
        #loan_id in FINES but with Paid==0, the former state!
        
        csr.execute(query12)
        for item in csr:
            self.former_unpaid_id_list.append(item[0])
            
        for refresh_finfo in self.fine_info_list:
            if refresh_finfo[0] in self.former_unpaid_id_list:
                #UPDATE
                csr.execute(update2, [refresh_finfo[1], refresh_finfo[2], refresh_finfo[0]])
                mydb.commit()
                
            else:
                #INSERT
                csr.execute(insert3, [refresh_finfo[0], refresh_finfo[1], refresh_finfo[2]])
                mydb.commit()
            
        csr.execute(query13)
        for item in csr:
            card_id = item[0]
            b_name = item[1]
            loan_id = item[2]
            loan_isbn = item[3]
            fine_amt = item[4]
            d_in = item[5]
            #print d_in
            d_in_indicator = ''
            if d_in is None:
                d_in_indicator = 'no'
            else:
                d_in_indicator = 'yes'
                
            ite = [card_id, b_name, loan_id, loan_isbn, d_in_indicator, fine_amt]
            '''
            str_total = str(card_id) + str(b_name) + str(loan_id) + str(loan_isbn)
            str_total = str_total.replace(' ','').lower()
            #print str_total1
            my_entered = self.srch_str
            my_entered = my_entered.replace(' ', '').lower()
            if my_entered in str_total:
                self.refre_list.append(ite)
                self.cardid_sumfine.setdefault(card_id, 0)
            '''
            self.refre_list.append(ite)
            self.cardid_sumfine.setdefault(card_id, 0)
            
        for finfo in self.refre_list:
            cur_famt = self.cardid_sumfine.get(finfo[0])
            new_fsum = cur_famt + finfo[5]
            #sum the fine amount for a card id
            self.cardid_sumfine[finfo[0]] = new_fsum
            
        for i in range(len(self.refre_list)):
            cur_id = self.refre_list[i][0]
            sum_val = self.cardid_sumfine.get(cur_id)
            self.refre_list[i].append(sum_val)
            
        for i in range(len(self.refre_list)):
            cid = self.refre_list[i][0]
            bna = self.refre_list[i][1]
            lid = self.refre_list[i][2]
            lsn = self.refre_list[i][3]
            t_str = str(cid) + str(bna) + str(lid) + str(lsn)
            t_str.replace(' ', '').lower()
            m_str = self.srch_str
            m_str.replace(' ', '').lower()
            if m_str in t_str:
                self.refre_list1.append(self.refre_list[i])
            
        csr.close()
        mydb.close()
        return
    
if __name__=='__main__':
    fu = FINES_update('')
    print fu.refre_list1
    
    
    