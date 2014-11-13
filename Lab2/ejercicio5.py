#!/usr/bin/python
import commands
import sys

listnum = []
fin = sys.stdin; 						#captura salida estandar
datos = fin.read();	
listnum = datos.split();				#transforma en una lista
listnum.sort(key=int);							#ordena la lista
rangomin = int(listnum[0])				#casting a int
rangomax = int(listnum[len(listnum)-1]) #casting a int

"""print "rango: ",
print rangomin
print rangomax
print "cadena: ",
print(listnum)""" #varios prints para comprobaciones

for x in range(rangomin, rangomax+1):
	print(x),
	apariciones = listnum.count(str(x)) #numero de veces que aparece un numero
	for pinta in range(apariciones):
		print("*"),
	print("\n")
