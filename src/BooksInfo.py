'''
Created on Mar 2, 2017
Collect the information in books.csv
@author: mdy
'''

import csv
import copy

class BooksInfo:
    def __init__(self, books_csv_file_path):
        self.f_path = books_csv_file_path
        self.b_rows = []
        self.row_list = []
        # the name of the column of books.csv
        self.title_list = []
        # exactly 6 '\t' information
        self.ifo24949_list_total = []
        # ['ISBN10', 'ISBN13', 'Title', 'Author', 'Cover', 'Publisher', 'Pages'], the author is splitted
        self.infor_list = []
        # ['ISBN10', 'Title', 'Author']
        self.infor_list1 = []
        # ['ISBN10', 'Title', 'Author_id']
        self.infor_list2 = []
        
        self.extract_books_info()
        # the index of author name in distinct_author_list is just the number of Author_id
        self.distinct_author_list = []
        # author name to id(integer)
        self.author_dict = {}
        self.extract_authors_info()
        self.construct_list2()
        
        #for insert to tables
        self.isbn_title = []
        self.authorid_name = []
        self.authorid_isbn = []
        self.construct_insert_values()
        
        return
    
    def extract_books_info(self):
        f_path = self.f_path
        with open(f_path) as f:
            rd = csv.reader(f)
            rows = [row for row in rd]
            
            
        self.b_rows = rows
        
        f.close()
        #total_infor_list = []
        for ln in range(len(rows)):
            self.row_list.append(rows[ln])
            if ln>0:
                infor = []
                ifo24949 = ''
                for i in range(len(rows[ln])):
                    ifo24949 += rows[ln][i]
                    
                ifo24949_list = ifo24949.split('\t')
                self.ifo24949_list_total.append(ifo24949_list)
                
                for i in range(len(rows[ln])):
                    infor_i = rows[ln][i].split('\t')
                    infor.extend(infor_i)
                    
                infor_i_correct = []
                infor_i_correct.append(ifo24949_list[0])
                infor_i_correct.append(ifo24949_list[1])
                infor_i_correct.append(ifo24949_list[2])
                
                for kk in range(len(infor)):
                    if infor[kk] in ifo24949_list[3] and infor[kk]!='':
                        infor_i_correct.append(infor[kk])
                        
                infor_i_correct.append(ifo24949_list[4])
                infor_i_correct.append(ifo24949_list[5])
                infor_i_correct.append(ifo24949_list[6])
                
                    
                #total_infor_list.append(infor)
                #infor = []
                #infor = infor_i_correct
                self.infor_list.append(infor_i_correct)
                b_isbn10 = infor_i_correct[0]
                #b_isbn13 = infor[1]
                b_title = infor_i_correct[2]
                b_author = []
                for j in range(3, len(infor_i_correct)):
                    if 'http' in infor_i_correct[j]:
                        break
                    else:
                        b_author.append(infor_i_correct[j])
                
                if len(b_author) == 0:
                    b_author.append('Unknown')
                            
                book_infor = [b_isbn10, b_title, b_author]
                self.infor_list1.append(book_infor)    
              
                           
        title = self.row_list[0][0].split('\t')
        self.title_list = title
            
        return
    
    def extract_authors_info(self):
        cp_info_list1 = copy.deepcopy(self.infor_list1)
        total_book_author = []
        for bkinfo in cp_info_list1:
            bk_author = bkinfo[2]
            for author1 in bk_author:
                if author1 not in total_book_author:
                    total_book_author.append(author1)
                    
        self.distinct_author_list = total_book_author
        
        for j in range(len(total_book_author)):
            self.author_dict.setdefault(total_book_author[j], j)
                
        return
    
    def construct_list2(self):
        list1 = copy.deepcopy(self.infor_list1)
        authordict = copy.deepcopy(self.author_dict)
        for i in range(len(list1)):
            itaid = []
            itaid.append(list1[i][0])
            itaid.append(list1[i][1])
            
            aid = []
            for j in range(len(list1[i][2])):
                aid.append(authordict.get(list1[i][2][j]))
                
            itaid.append(aid)
            
            self.infor_list2.append(itaid)
                
        return
    
    def construct_insert_values(self):
        name_to_id = copy.deepcopy(self.author_dict)
        i_t_aid = copy.deepcopy(self.infor_list2)
        for i in range(len(i_t_aid)):
            isbntitle = i_t_aid[i][:2]
            self.isbn_title.append(isbntitle)
            for j in range(len(i_t_aid[i][2])):
                aidisbn = [i_t_aid[i][2][j], i_t_aid[i][0]]
                if aidisbn not in self.authorid_isbn:
                    self.authorid_isbn.append(aidisbn)
            
        for key in name_to_id.iterkeys():
            #aidname = [key, name_to_id.get(key)]
            aidname = [name_to_id.get(key), key]
            self.authorid_name.append(aidname)
            
        
        return
    
    
if __name__=='__main__':
    fp = '../Data/books.csv'
    bk = BooksInfo(fp)
    print len(bk.authorid_isbn)
    #print len(set(bk.authorid_isbn))
    
    
    
        