#!/usr/bin/env python

import psycopg2
import re
import sys
import glob 
import os
from os import listdir

#ip= 10.10.120.17
		
		
def info(filename):
	try:
		conn = psycopg2.connect("dbname=ier user=ier password=ier host=localhost")
		cur = conn.cursor()
		n=re.compile(r"(Number of atoms\s*:?\s*([0-9]+))")
		coord=re.compile(r"atom\s*((-?[0-9]*\.[0-9]+\s*)(-?[0-9]+\.[0-9]+\s*)(-?[0-9]+\.[0-9]+\s*)([A-Za-z]+))")
		palabra=re.compile(r"Relaxation step number\s*[0-9]+:")
		f = open(filename)
		f_name=f.name
		new=open("coord_"+f_name,'w')
		new.write("#\t\t x[A]\t\t y[A]\t\t z[A]\n")
		new = open("coord_"+f_name, 'w')
		new.write("#\t\t x[A]\t\t y[A]\t\t z[A]\n")
		while True:
			line = f.readline()
			if not line: break
			
			nA=n.search(line)
			word=palabra.search(line)
			aux=coord.search(line)
			
			if nA != None:
				new.writelines(nA.group(0)+"\n")
				
			if word != None:
				new.writelines(word.group(0)+"\n")
				
			if aux != None:
				new.writelines(aux.group(0)+"\n")
				
		new.close()
		new=open("coord_"+f_name, 'r').read()
		binaryF = f.read()
		cur.execute("INSERT INTO fhi(archivo,coordenadas) VALUES (%s,%s)", (psycopg2.Binary(binaryF),psycopg2.Binary(new),))
		conn.commit()
		f.close()
		cur.close()
		conn.close()
		
	except psycopg2.DatabaseError, dbe:
		print str(dbe)
		return(None)
	except Exception, e:
		print str(e)
		return(None)


def directorio():
	for i in os.listdir(os.getcwd()):
		if i.endswith(".out"):
			info(i)



if __name__ == '__main__':
	directorio()
