#!/usr/bin/python
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option("-a", action="store")
parser.add_option("-b", action="store")
parser.add_option("-d", action="store")
parser.add_option("-e", action="store")
parser.add_option("-f", action="store")
parser.add_option("-r", action="store")

options, args = parser.parse_args()

print options.b

"""for i in range(1,len(args),2):
		if args[i] in options:
			print sys.argv[i]+" => "+args[i+1]
"""	
