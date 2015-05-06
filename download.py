# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
import threading
import Queue
import os

class download(threading.Thread):  
    def __init__(self,que):  
        threading.Thread.__init__(self)  
        self.que=que  
    def run(self):  
        while True:  
            if not self.que.empty():  
                name=self.que.get()
                nameArray = name.split('/')
                path='books/'+nameArray[-2]+'/'+nameArray[-1]
                os.makedirs(path)
                pdf = 'https://www.gitbook.com/download/pdf'
                epub = 'https://www.gitbook.com/download/epub'
                mobi = 'https://www.gitbook.com/download/mobi'
                print('-----%s------'%(self.name))  
                os.system('wget -O '+path+nameArray[-1]+'.pdf ' +pdf+name)  
                os.system('wget -O '+path+nameArray[-1]+'.epub '+epub+name)  
                os.system('wget -O '+path+nameArray[-1]+'.mobi '+mobi+name)
            else:
                break 

if __name__=='__main__':
    conn = MySQLdb.connect(user='gitbook', db='gitbook', passwd='yangyang', host='localhost', charset="utf8", cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute('select * from books')
    rs = cursor.fetchall()
    que=Queue.Queue() 
    for row in rs:
        bookname = row['rbookname']
        que.put(bookname)
        print que.qsize()
    for i in range(5):  
        d = download(que)
        d.start()
