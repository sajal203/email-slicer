# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:44:47 2020

@author: sajal
"""


email = input('enter your email address:- ').strip()

'''using sting slicing, we are seprating the username before @'''

user_name = email[:email.index('@')]

'''same way after @ is the domain name'''

domain_name = email[email.index('@')+1:]

print('your username is ',user_name, 'and domain name is ',domain_name)
