# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:47:50 2020

@author: Kanan
"""

str="Ramakant is going wipro doing work does he get work starts enjoying"
word_token=str.split()
stem_list=['ing','es','s']
stammed_token=[]
for token in word_token:
    stammed=token
    for stem in stem_list:
        word=token[-len(stem):len(token)]
        if word==stem:
            stammed=token[:-len(stem):]
            break
        
    stammed_token.append(stammed)
print(stammed_token)