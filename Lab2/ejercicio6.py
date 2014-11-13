#!/usr/bin/python

import sys

if(len(sys.argv) < 1):
    print "ejercicio6 filein caesar_shift"

if(len(sys.argv) > 2):
    shift = sys.argv[2]
else:
    shift = 3

f = open(sys.argv[1],'r')
cif = ''
for letra in f.read():
    letra.upper()
    if letra != ' ' and letra != '\n':
        num = ord(letra)-65-int(shift)
        num %=26
        num +=65
        cif += chr(num)
    elif letra == ' ' or letra == '\n':
		cif+=letra
print cif,

f.close()
