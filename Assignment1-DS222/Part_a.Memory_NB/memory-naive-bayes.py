from __future__ import division



import os
import random
import time
import re
import numpy as np
import codecs
from collections import defaultdict





dx = defaultdict(lambda : defaultdict(int))
dy = defaultdict(int)
train_dir="/home/sonalis/nlp/mlld/full_train.txt"
filename_train = open(train_dir,"r") 
lines = filename_train.readlines()
start = time.time()
for line in lines:
	values = line.split("\t")
	labels=values[0].rstrip().split(",")
	words = re.sub("\d+", "", values[1].rsplit('"',1)[0].split('"',1)[1])
	regex = r'(\w*)'
	list1=re.findall(regex,words)
	while '' in list1:
	   list1.remove('')
	list1=map(str.lower, list1)
	list1 = [word for word in list1 if len(word)>2]
	for label in labels:
	   dy[label] += 1
	   for word in list1:
	       dx[label][word] += 1

print("--- %s seconds ---" % (time.time() - start))
test_dir="/home/sonalis/nlp/mlld/full_test.txt"         ########################change train path
filename_test = open(test_dir,"r") 
lines = filename_test.readlines()
total =len(lines)
print(total)
error=0	
out_label="a"
start = time.time()
with open("/home/sonalis/nlp/mlld/full_test.txt", "r") as script: ######################change test path
		filelines = script.readlines()
		i=0
		for line in filelines:
		   i=i+1
		   print(i)
		   max_prob = float("-inf")
		   values = line.split("\t")
		   labels=values[0].rstrip().split(",")
		   words = re.sub("\d+", "", values[1].rsplit('"',1)[0].split('"',1)[1])
		   regex = r'(\w*)'
		   list1=re.findall(regex,words)
		   while '' in list1:
		   	list1.remove('')
		   list1=map(str.lower,list1)
		   list1 = [word for word in list1 if len(word)>2]
		   list1=list(np.unique(list1))
		   size_list = len(list1)
		   if size_list != 0:
			   counta = 1.0/size_list
			   countc = 1.0/len(dy)
			   countd = sum(dy.values())+1.0
			   for clas in dy.keys():
				prob = 0
				countb = sum(dx[clas].values())+1.0
				for word in list1:
				
						prob = prob + np.log((dx[clas][word]+counta)/(countb))
				
				prob = prob + np.log((dy[clas]+countc)/(countd))
		                if(max_prob<prob):
					max_prob = prob
					max_prob_clas = clas
			
	     
		   if max_prob_clas in labels:
			#print "right"
			f=0
		   else:
			#print "wrong"
			error=error+1

print("test accuracy" , ((total-error)/total)*100)
print("--- %s seconds ---" % (time.time() - start))	
	    
		
        
	
