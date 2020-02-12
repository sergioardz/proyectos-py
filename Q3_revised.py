#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:59:39 2020

@author: sergioardz
"""

# Implement the validate function, which accepts a username and returns true
# if it is acceptable and false if it is not.

# A username is valid if it satisfies the following rules:
# -- The username must be at least 4 characters long.
# -- The username must contain only letters, numbers and optionally one
#    underscore (_).
# -- The username must start with a letter, and must not end with an 
#    underscore (_).

# For example, validate("Mike Standish"); would return false because it
# contains a space.

user = 'Mike Standish'
user_2 = 'Mike_Standish'

def rule_1(username):
    """
    Input: a string representing a username
    Output: boolean value representing if the input meets conditions
    """
    # Checks is length is at least 4 chars long
    return len(username) >= 4

def rule_2(username):
    """
    Input: a string representing a username
    Output: boolean value representing if the input meets conditions
    """
    # Initiate state of response to true
    is_valid = True
    # Initiate a counter for underscores '_'s
    uscore = 0
    # Valid characters definition
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
0123456789_'
    # Iterate through the passed string and check valid chars
    for char in username:
        if char not in valid_chars:
            is_valid = False
    # Iterate through the passed string and check amount of '_'s
    for e in username:
        if e == '_':
            uscore += 1
    # Return if condition is met or not
    return is_valid and uscore <= 1

def rule_3(username):
    """
    Input: a string representing a username
    Output: boolean value representing if the input meets conditions
    """
    # All letters definition: lower and upper
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # First and Last Chars validation
    first = username[0] in letters
    last = username[-1] != '_'
    # Return if condition is met or not
    return first and last


def validate(username):
    """
    Input: a string representing a username
    Output: boolean value representing if the input meets conditions
    """
    # Use all three function rules validation and return if conditions are met or not
    return rule_1(username) and rule_2(username) and rule_3(username)

print(validate(user))
print(validate(user_2))
