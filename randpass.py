#!/usr/bin/env python2.7
# Mark Saad
# mark.saad@ymail.com
# 7July2016
# A Silly random password generator

import linecache
import sys
import argparse
from random import randint
from random import sample

parser = argparse.ArgumentParser(description='Generate a random password')
parser.add_argument('-w', metavar='words', type=int, nargs='?', help='number of random words', default=3)
parser.add_argument('-d', metavar='digits', type=int, nargs='?', help='number of random digits',default=4)
args = parser.parse_args()

words = []
for i in xrange(args.w):
	words.append(linecache.getline('common-words.txt', randint(1,1000)).rstrip().title())

line = "".join(words)+str(randint(10**(args.d-1), 10**args.d-1)).rstrip()

shuffled_line = ''.join(sample(line, len(line)))

print "Your random password is:", line

print "Your Shuffled random password is:", shuffled_line
