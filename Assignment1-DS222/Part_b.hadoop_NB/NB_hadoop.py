#! /usr/bin/env python
import os
import re
import sys

from mrjob.job import MRJob
from mrjob.protocol import RawProtocol, ReprProtocol


#input_file = os.environ['map_input_file']
#WORD_RE  = (re.compile(r"[\w']+", os.path.basename(input_file))[0])
#WORD_RE = re.compile(r"[\w']+")
#OUTPUT_PROTOCOL = RawProtocol

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
	values = line.split("\t")
	labels=values[0].rstrip().split(",")
	#listx=["and", "the", "are","was","were","will","with","from","that","its","has"]
	words = re.sub("\d+", "", values[1].rsplit('"',1)[0].split('"',1)[1])
	regex = r'(\w*)'
	list1=re.findall(regex,words)
	while '' in list1:
	   list1.remove('')
	list1=map(str.lower,list1)
	list1 = [word for word in list1 if len(word)>2]
	for label in labels:
		yield '!'+label, 1
		for word in list1:
			yield '!!'+label, 1
	    		yield (label,word), 1

    #def combiner(self, key, counts):
        #yield key, sum(counts)
	
    def reducer(self, key, counts):
        yield key, sum(counts)
	

if __name__ == '__main__':
    MRWordFreqCount.run()
