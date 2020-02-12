#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:31:32 2020

@author: sergioardz
"""

#def john_mary(str):
#    john = ['John', 'john'] 
#    #john = 'John'
#    mary = ['Mary', 'mary']
#    #mary = 'Mary'
#    c_john = 0
#    c_mary = 0
#    #aux_john = john in str
#    #aux_mary = mary in str
#    for element in john:
#        if element in str:
#            c_john += 1
#    for element in mary:
#        if element in str:
#            c_mary += 1
#    print(c_john, c_mary)
#    return c_john == c_mary
#
#print(john_mary('John&Mary'))

def john_mary(str):
    john = 'John'
    mary = 'Mary'
    c_john = 0
    c_mary = 0
    aux_john = john in str
    aux_mary = mary in str
    if aux_john:
        c_john += 1
    if aux_mary:
        c_mary += 1
    return c_john == c_mary

print(john_mary('John&Mary'))