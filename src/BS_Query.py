'''
Created on Mar 8, 2017

Query Used for Book Search and Availability

@author: mdy
'''

import mysql.connector
from QList import *
import copy

class BS_Query:
    def __init__(self, etstr, hst='localhost', usr='mdy', pwd='123mdy', dtbs='Library'):
        self.entered = etstr
        
        #group 1
        #only one author in one book in all_list in (u'XXX, u'XXX, u'XXX) format
        self.all_list = []
        #out of stock isbn
        self.out_list = []
        #only isbn and title information
        self.isbn_title = []
        self.isbn_title_as = []
        #
        self.itaa = []
        #
        self.rst_list = []
        #self.searchBK(hst, usr, pwd, dtbs)
        
        # this group use method2: searchBK1
        self.all_list1 = []
        # initial match
        self.initial_match = []
        self.initial_match_issn = []
        self.second_match = []
        self.rst2 = []
        self.outisbn = []
        self.searchBK1(hst, usr, pwd, dtbs)
        return
    
    
    def searchBK1(self, hst, usr, pwd, dtbs):
        mstr = self.entered.replace(' ', '').lower()
        cnx = mysql.connector.connect(host=hst, user=usr, passwd=pwd, database=dtbs)
        cursor = cnx.cursor()
        #***
        cursor.execute(query1)
        for item in cursor:
            self.all_list1.append(item)
            it0 = item[0]
            it1 = item[1]
            it2 = item[2]
            itt = it0 + it1 + it2
            itt1 = itt.replace(' ', '').lower()
            #print itt1
            if mstr in itt1:
                mit = [it0, it1, it2]
                self.initial_match.append(mit)
                if it0 not in self.initial_match_issn:
                    self.initial_match_issn.append(it0)
                
        #second iteration to combine information, combined based on issn
        imisbn = copy.deepcopy(self.initial_match_issn)
        cursor.execute(query1)
        for item in cursor:
            it0 = item[0]
            it1 = item[1]
            it2 = item[2]
            if it0 in imisbn:
                mit2 = [it0, it1, it2]
                self.second_match.append(mit2)
                
        #second_match stored all the information we need to construct the result
        smch = copy.deepcopy(self.second_match)
        for i in range(len(imisbn)):
            b0 = imisbn[i]
            #print b0
            b1 = ''
            b2 = []
            for j in range(len(smch)):
                sm0 = smch[j][0]
                sm1 = smch[j][1]
                sm2 = smch[j][2]
                if b0 == sm0:
                    b1 = sm1
                    b2.append(sm2)
                    
            bb = [b0, b1, b2, 'yes']
            self.rst2.append(bb)
            
        cursor.execute(query2)
        for item in cursor:
            self.outisbn.append(item[0])
            
        for j in range(len(self.rst2)):
            if self.rst2[j][0] in self.outisbn:
                self.rst2[j][3] = 'no'
            
        cursor.close()
        cnx.close()
        return
    
    
    def searchBK(self, hst, usr, pwd, dtbs):
        #the string used to match
        mstr = self.entered.replace(' ', '').lower()
        # construct the list
        cnx = mysql.connector.connect(host=hst, user=usr, passwd=pwd, database=dtbs)
        cursor = cnx.cursor()
        
        ###
        cursor.execute(query1)
        for item in cursor:
            self.all_list.append(item)
            isbn_and_titlet = []
            for i in range(2):
                isbn_and_titlet.append(item[i])
                
            author = item[2]
            if isbn_and_titlet not in self.isbn_title:
                self.isbn_title.append(isbn_and_titlet)
                ita = copy.deepcopy(isbn_and_titlet)
                ita.append([author])
                #ita = isbn_and_titlet.append([author])
                self.isbn_title_as.append(ita)
            else:
                k = self.isbn_title.index(isbn_and_titlet)
                self.isbn_title_as[k][2].append(author)
                pass
            
        ###
        
        ###
        cursor.execute(query2)
        for item in cursor:
            self.out_list.append(item)
            
        ###
        for bkinfo in self.isbn_title_as:
            str1 = bkinfo[0] + bkinfo[1]
            str2 = ''
            for ath in bkinfo[2]:
                str2 += ath
                
            str_total = str1 + str2
            str_total = str_total.replace(' ', '').lower()
            if mstr in str_total:
                if bkinfo[0] in self.out_list:
                    booki = bkinfo[0]
                    bookt = bkinfo[1]
                    bookas = bkinfo[2]
                    bookav = 'no'
                    bb = [booki, bookt, bookas, bookav]
                    self.itaa.append(bb)
                else:
                    booki = bkinfo[0]
                    bookt = bkinfo[1]
                    bookas = bkinfo[2]
                    bookav = 'Yes'
                    bb = [booki, bookt, bookas, bookav]
                    self.itaa.append(bb)
        
                    
        cursor.close()
        cnx.close()
        return
    
    
if __name__=='__main__':
    wrd = 'brave new'
    #host='localhost'
    #user='mdy'
    #passwd='123mdy'
    #database='Library'
    #bqr = BS_Query(wrd, host, user, passwd, database)
    '''
    bqr = BS_Query(wrd)
    for i in range(len(bqr.second_match)):
        print bqr.second_match[i]
    
    print '***'
    for i in range(len(bqr.rst2)):
        print bqr.rst2[i]
    '''
    
    #fro group 1
    '''
    print bqr.all_list[0]
    print bqr.isbn_title[0]
    print len(bqr.isbn_title_as)
    print bqr.isbn_title_as[0]
    print len(bqr.itaa)
    for i in range(len(bqr.itaa)):
        print bqr.itaa[i]
    
    '''    
        
        