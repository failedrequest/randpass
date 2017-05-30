#!/usr/bin/env python2.7
# Mark Saad 
# mark.saad@ymail.com
# 7July2016
# A Silly random password generator 

import linecache
import sys
from random import randint

nwords = sys.argv[1]
words = []

for i in xrange(int(nwords, 10)):
	words.append(linecache.getline('common-words.txt', randint(1,1000)).rstrip().title())

line = "".join(words)+str(randint(1000,9999)).rstrip()

print "Your random password is:", line

