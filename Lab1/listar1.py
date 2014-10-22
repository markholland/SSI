#!/usr/bin/python

import sys

options=["-a","-b","-d","-e","-f","-r"]

for i in range(1,len(sys.argv),2):
		if sys.argv[i] in options:
			print sys.argv[i]+" => "+sys.argv[i+1]
		
