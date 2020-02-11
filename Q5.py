#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:29:23 2020

@author: sergioardz
"""

#def fibonacci(a):
#    res = 0
#    n = 0
#    while n > a:
#        if a == 0 or a == 1:
#            return 1
#        else:
#            res += fibonacci(a - 1)
#            print(res)
#    return res;
#
#print(fibonacci(0))

def fibonacci(a):
    if a == 0 or a == 1:
        return 1
    else:
        fibo = [1, 1]
        for i in range(2, a+1):
            aux = fibo[i-2] + fibo[i-1]
            fibo.append(aux)
    print(fibo)
    return fibo[a-1]

print(fibonacci(12))
print(fibonacci(14))

#a = 12
#fibo = []
#for i in range(1, 13):
#    aux = i - 1
#    fibo.append(i + aux)
#print(fibo)


#def fibonacci(a):
#    if a == 0:
#        return 1
#    fibo = []
#    else:
#        res = 0
#        while a < 1:
#            res += 


## SOLUCION EDGAR LOPEZ
#    first =0
#    second = 1
#    for i in range(a):
#        first,second = second,first+second
#    return second



















    