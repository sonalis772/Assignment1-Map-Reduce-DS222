#!/usr/bin/env python 

import sys
import os
import random
import re

def main():
    prevkey=" "
    prevlist=[]
    linelist=[]
    #lines=[lines[165]]
    for line in sys.stdin:
	if line[0]=='!':
		print line.split("\n")[0]
	else:
		list1=line.rsplit()
		if list1[0]==prevkey or prevkey==" ":
			if '~' not in list1[1]:
				prevkey=list1[0]
				prevlist=prevlist+list1[1:]
			else:
				linelist=linelist+[line]
		else:
			for store in linelist:
				list1=store.rsplit()
				currentkey=list1[0].split("~")[0]
				if (len(prevlist)==0):
					print " ".join(list1[2:]),"~"+currentkey
				else:
					print " ".join(list1[2:]),"~"+currentkey," ".join(prevlist)
			linelist=[]
			prevlist=[]
			list1=line.rsplit()
			if '~' not in list1[1]:
				prevkey=list1[0]
				prevlist=prevlist+list1[1:]
			else:
				linelist=linelist+[line]
				prevkey=list1[0]	
    for store in linelist:
		list1=store.rsplit()
		currentkey=list1[0].split("~")[0]
		if (len(prevlist)==0):
			print " ".join(list1[2:]),"~"+currentkey
		else:
			print " ".join(list1[2:]),"~"+currentkey," ".join(prevlist)
	
	


if __name__ == "__main__":
    main()

