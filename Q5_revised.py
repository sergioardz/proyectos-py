#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:22:20 2020

@author: sergioardz
"""

# You already saw a simple recursive solution for Fibonacci.
# Implement below an iterative solution for the same problem.

# Remember:
# -- fibonacci(0) = 1
# -- fibonacci(1) = 1
# -- fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

def fibonacci(a):
    """
    Input: an integer representing the position in the fibonacci sequence
    Output: the actual value of such position in the fibonacci sequence
    """
    # Initiate a list with sequence numbers starting with 1, 1 for 0 and 1
    # respectively
    fibo = [1, 1]
    # Iterate either until a or a+1 depending on position definition
    # i.e. F12 = 144 or F12 = 233
    for i in range(2, a+1):
        # Calculate new number sequence
        aux = fibo[i-1] + fibo[i-2]
        # Append new number
        fibo.append(aux)
    # Return last number
    return fibo[-1]

print(fibonacci(12))
print(fibonacci(14))