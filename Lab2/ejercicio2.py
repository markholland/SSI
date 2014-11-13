#!/usr/bin/python

import sys
from optparse import OptionParser

print "salida de listar"

def my_callback(option,opt,value,parser):
	print opt," => ",value
		
parser = OptionParser()
#options=["-a","-b","-d","-e","-f","-r"]
parser.add_option("-a",action="callback",callback = my_callback,type="string")
parser.add_option("-b",action="callback",callback = my_callback,type="string")
parser.add_option("-d",action="callback",callback = my_callback,type="string")
parser.add_option("-e",action="callback",callback = my_callback,type="string")
parser.add_option("-f",action="callback",callback = my_callback,type="string")
parser.add_option("-r",action="callback",callback = my_callback,type="string")
parser.parse_args()

