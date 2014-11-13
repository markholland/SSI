# -*- coding: utf-8 -*-
import sys;
from urllib2 import URLError, HTTPError, urlopen;

if len(sys.argv) < 2:
	address="http://www.upv.es";
elif sys.argv[1].startswith('http://'):
    address=sys.argv[1];
else:
    address='http://'+sys.argv[1];
url=urlopen(address);
data=url.read();
tipo=url.info().getheader("Content-Type") 
if (tipo.find("html") != -1):
	myList=''
	for simbolo in data:
		if simbolo.isalpha() or simbolo.isspace():
			myList+=simbolo;
		else:
			myList+=' ';
	myList=myList.split()
	myList.sort()
	#list(set(myList))
	s = []
	for i in myList:
		if i not in s:
			s.append(i)
	print s
