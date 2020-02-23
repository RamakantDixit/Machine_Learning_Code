# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:08:48 2020

@author: Kanan
"""

from sys import argv
print("First argument ={0}".format(argv[1]))
print("Second argument ={0}".format(argv[2]))
print("Third argument ={0}".format(argv[3]))
print("Fourth argument ={0}".format(argv[4]))
print("fifth argument ={0}".format(argv[5]))

def Find_Bigger(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print("{0} is biggest number".format(num1))
        else:
            print("{0} is biggest number".format(num3))
    else:
        if num2>num3:
            print("{0} is biggest number".format(num2))
        else:
            print("{0} is biggest number".format(num3))
    
Find_Bigger(argv[1],argv[2],argv[3])