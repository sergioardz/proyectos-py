#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:41:39 2020

@author: sergioardz
"""

# Return True if the substrings 'John' and 'Mary' appear the same number of
# times in the given string; otherwise return False.
# String comparison should be case insensitive.

def john_mary(str):
    """
    Input: String
    Output: Boolean
    Checks wether substrings 'John' and 'Mary' are present the same amount of
    times within the passed string. Case Insensitive.
    """
    # Start counters
    john = 0
    mary = 0
    # Iterate through string length minus 3 positions to accomodate last slice
    for i in range(len(str)-3):
        # Collect slices and manage case insensitivity converting all to lower
        aux = str[i:i+4]
        aux_lower = aux.lower()
        # Adjust counters accordingly
        if aux_lower == 'john':
            john += 1
        elif aux_lower == 'mary':
            mary += 1
    # Return boolean value
    return john == mary
    

print(john_mary('John&Mary'))
        