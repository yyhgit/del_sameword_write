# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:51:02 2017
定义一个函数，打开文件并去除里面重复的单词，并关闭文件
@author: yyh
"""

def w_s():
    s=raw_input('input a str: ')
    word_list = s.split(' ')
    print word_list
    word_list = set(word_list)
    to_w = ' '.join(word_list)
    print word_list
    f=open('file.txt','w')
    f.write(to_w)
    f.close()
    
w_s()
