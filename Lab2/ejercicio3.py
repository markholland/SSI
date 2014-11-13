#!/usr/bin/python

import sys

argumento = sys.argv
if len(argumento) < 2 :
	print"listar 4 file in"
else:
    f = open(argumento[1],'r')
    text=f.read().split(':')
    print text[0]+":"
    for i in range(1, len(text)):
        print "\t"+text[i]
	f.close()
