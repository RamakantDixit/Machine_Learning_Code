# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:46:12 2020

@author: Kanan
"""
#filter function syntax
#filter(function, iterable)
#lambda function syntax
#lambda arguments : expression
#x = lambda a : a + 10
#how to show vowels from list without for loop.

import re

str=['a','b','c','d','e','f']

vowel=list(filter(lambda x:re.search(r"^[aeiou]+$",x),str))

print("vowel list=",vowel)
 
#how to show consents from list without for loop.
consents=list(filter(lambda x:re.search(r"^[^aeiou]+$",x),str))
print("consents list=",consents)
 
#how to get all even numbers from a list
num=[1,3,5,6,7,89,43,22,90,65,45,92,93,77,73,75]
even=list(filter(lambda x:x%2==0,num))
print("even list= ",even)
 
#how to get all odd numbers from a list
odd=list(filter(lambda x:x%2!=0,num))
print("odd list= ",odd)

#in the given number list how to show every 5th element
for n in range(0,len(num),5):
    print(num[n])