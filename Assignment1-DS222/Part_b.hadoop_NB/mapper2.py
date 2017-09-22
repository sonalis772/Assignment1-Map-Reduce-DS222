#!/usr/bin/env python 

import sys
import os
import random
import re
from collections import defaultdict
import math

def main():
        prevkey=" "
	prevlist=""
	dy_classes = defaultdict(int)
	dy_words = defaultdict(int)
	f = open("ref", 'r')
	lines = f.readlines()
	for line in lines:
		#print(line)
		if line[0]=='!' and line[1] =='!':
			list2=line.rsplit()
			key=list2[0].split('!!')[1]
			dy_words[key]=int(list2[1])
		elif    line[0]=='!':
			list2=line.rsplit()
			key=list2[0].split('!')[1]
			dy_classes[key]=int(list2[1])
	#print(dy_classes)	
	for line in sys.stdin:
		if line[0]!='0' and line[1]!='!':
		
			#print dy_words
			#print dy_classes
			list1=line.split("~")
			line_no=list1[0].rsplit()[0]
			labels=list1[0].rsplit()[1].split(",")
			#print line_no
		       	#print labels
			prob_classes=defaultdict(int)
			for label in dy_classes.keys():
				prob_classes[label]=0
			list_words=list1[1:]
			for i in range(len(list_words)):
				temp_dic=defaultdict(int)
				data=list_words[i].rsplit()
				for i in range(1,len(data),2):
					temp_dic[data[i]]=int(data[i+1])
				for label in dy_classes.keys():
					if label not in temp_dic.keys():
						prob_classes[label]=prob_classes[label]+math.log((0.0+1.0/len(list_words))/(dy_words[label]+1.0))
					else:
						prob_classes[label]=prob_classes[label]+math.log((temp_dic[label]+1.0/len(list_words))/(dy_words[label]+1.0))
			for label in dy_classes.keys():
				prob_classes[label]=prob_classes[label]+math.log((dy_classes[label]+1.0/len(dy_classes))/(sum(dy_classes.values())+1.0))
			#output_label=max(prob_classes.iteritems(), key=operator.itemgetter(1))[0]
			maxprob=max(prob_classes.values())
			out_label=prob_classes.keys()[prob_classes.values().index(maxprob)]
			if out_label in labels:
				print "correct",1
			else:
				print "error",1



if __name__ == "__main__":
    main()

