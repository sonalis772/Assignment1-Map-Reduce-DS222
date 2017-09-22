#!/usr/bin/env python 

import sys
import os
import random
import re
#import numpy as np



def main():
    for line in sys.stdin:
	if ((line[0]=='"')and(line[1]=='!')and(line[2]=='!')):
		list1=line.split("\t")
		#print(re.findall(r'"(.*?)"', list1[0]),list1[1].split("\n")[0])
		print re.findall(r'"(.*?)"', list1[0])[0] ,list1[1].split("\n")[0]
	elif ((line[0]=='"')and(line[1]=='!')):
		list1=line.split("\t")
		#print(re.findall(r'"(.*?)"', list1[0]),list1[1].split("\n")[0])
		print re.findall(r'"(.*?)"', list1[0])[0] ,list1[1].split("\n")[0]
	elif ((line[0]=='[')):
	        number =line.split("]")[1].split("\n")[0]
		list1=re.findall(r'"(.*?)"', line.split("] ")[0])
		print list1[1],list1[0],number
	 	#print(list1)
	else:
			values = line.split("\t")
			labels=values[1]#.rstrip().split(",")
			words = re.sub("\d+", "", values[2].rsplit('"',1)[0].split('"',1)[1])
			regex = r'(\w*)'
			list1=re.findall(regex,words)
			#listx=["and", "the", "are","was","were","will","with","from","that","its","has"]
			while '' in list1:
			   list1.remove('')
			list1=map(str.lower,list1)
			list1 = [word for word in list1 if len(word)>2]
			s=[]
			for i in list1:
       				if i not in s:
          				s.append(i)
			#list1=list(np.unique(list1))
			for word in s:
			    	print word+' ~' ,values[0],labels


if __name__ == "__main__":
    main()

