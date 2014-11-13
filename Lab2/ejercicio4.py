#!/usr/bin/python

import sys
from optparse import OptionParser
import random

parser = OptionParser()

parser.add_option("-m",action="store",type="int",dest="numero1",default = 0)
parser.add_option("-M",action="store",type="int",dest="numero2",default = 100)
parser.add_option("-n",action="store",type="int",dest="iteraciones",default = 25)
(options,args)=parser.parse_args()

numero1 = options.numero1
numero2 = options.numero2
iteraciones = options.iteraciones

for n in range(iteraciones):
	num_aleatorio = random.randint(numero1,numero2)
	print num_aleatorio




