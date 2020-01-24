#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:32:18 2020

@author: lu270
"""

def do_twice (f,x):
    f(x)
    f(x)
def print_spam():
    print('spam')
def print_twice(x):
    print (x)
    print (x)

do_twice (print_twice, 'spam')


def do_four (f,x):
    do_twice (f,x)
    do_twice (f,x)
    
do_four (print_twice, 'spam')
