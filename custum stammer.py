# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:47:50 2020

@author: Kanan
"""

str="Ramakant is going wipro doing work does he get work starts enjoying"
stemer_list=['ing','es','s']
token_list=str.split()
new_str=[]
for token in token_list:
    stem_word=token
    for stem in stemer_list:
        word=token[-len(stem):len(token)]
        if word==stem:
            stem_word=token[:-len(stem)]
    new_str.append(stem_word)
print(' '.join(new_str))
