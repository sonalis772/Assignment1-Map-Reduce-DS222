#!/usr/bin/env python

import sys
import os
import random
import re



def main():
	current_word = None
	current_count = 0
	word = None
	for line in sys.stdin:
	    word = line.split('\t')[0]
	    count=line.split('\t')[1].split('\n')[0]
	    if(word==current_word or current_word==None):
		current_count=current_count+int(count)
		current_word=word
	    else:
		print current_word,current_count
		current_word=word
		current_count=1
	print current_word,current_count
if __name__ == "__main__":
    main()

