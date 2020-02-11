#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:52:44 2020

@author: sergioardz
"""

#import re


def validate(username):
    if len(username) <= 0:
        return False
    else:
        valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        is_len_valid = False
        if len(username) >= 4:
            is_len_valid = True
        is_first_char_valid = False
        if username[0] in letters:
            is_first_char_valid = True
        is_last_char_valid = True
        if username[-1] == '_':
            is_last_char_valid = False
        is_valid_chars = True
        for char in username:
            if char not in valid_chars:
                is_valid_chars = False
        print(username)
        print('len', is_len_valid)
        print('first', is_first_char_valid)
        print('last', is_last_char_valid)
        print('chars', is_valid_chars)
        return is_len_valid and is_first_char_valid and is_last_char_valid and is_valid_chars

print(validate("Mike_Standish")) #Valid username
print(validate("Mike Standish")) #Invalid username
print(validate("sergioardz_"))
print(validate("_ergioardz"))
print(validate("5ergioardz_"))
print(validate("ser"))
print(validate("serg"))
print(validate("serg*"))
print(validate(""))



#def validate(username):
#    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
#    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#    is_valid_chars = True
#    is_len_valid = False
#    if len(username) >= 4:
#        is_len_valid = True
#    is_first_char_valid = True
#    if username[0] not in letters:
#        is_first_char_valid = False
#    is_last_char_valid = True
#    if username[-1] == '_':
#        is_last_char_valid = False
#    for char in username:
#        if char not in valid_chars:
#            is_valid_chars = False
#    return is_valid_chars and is_len_valid and is_first_char_valid and is_last_char_valid
#
#print(validate("Mike_Standish")) #Valid username
#print(validate("Mike Standish")) #Invalid username