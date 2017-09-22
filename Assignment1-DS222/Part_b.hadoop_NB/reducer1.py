#!/usr/bin/env python 

import sys
import os
import random
import re
#import numpy as np



def main():
    prevkey=" "
    prevlist=""
    for line in sys.stdin:
	if line[0]=='!':
		print '0'+line.split("\n")[0]
	else:
		list1=line.split("~")
		if list1[0]==prevkey or prevkey==" ":
			prevlist=prevlist+"~"+list1[1].split("\n")[0]
			prevkey=list1[0]
		else:  
                        print prevkey,prevlist
			prevkey=list1[0]
			prevlist="~"+list1[1].split("\n")[0]
			
    print prevkey,prevlist	       	


if __name__ == "__main__":
    main()

