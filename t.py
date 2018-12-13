#!/usr/bin/env python2.7
# Mark Saad 
# mark.saad@ymail.com
# 12Dec2018
# A Silly random password generator 

import linecache
from random import randint


def getword():
    word = linecache.getline('common-words.txt', randint(1,1000))
    return word.strip()


print("Your random password is: {}{}{}{}").format(getword(),getword().title(),getword().title(),randint(1000,9999))

