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


# List List comprehensions
old_list = [1, 0, -2, 4, -3]
new_list = [x**2 for x in old_list if x > 0]
print(new_list)

# remove all special char from string
str="as ramakant ## is %%^^^^&&&***@@@@ hero"
new_str=' '.join(list(filter(lambda x:x.isalnum(),str.split())))
print(new_str)


#print prime number till given number
num=100
for n in range(2,num):
    for i in range(2,n):
        if(n%i)==0:
            break
        else:
            print(n)
            break
# print Fibonacci till given number
n1,n2=0,1
count=0
num=20
while n1<=num:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1

#print Fibonacci till given term
n1,n2=0,1
count=0
num=20
while count<=num:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1

# reverse the given string
strs="I love my india"
strs_t=strs.split()
print(strs_t[::-1])

#print reverse string along with char
print(strs[::-1])

