#!/usr/bin/env python

"""Script de FHI-AIMS para obtener coordenadas de atomos
@author: Tiare R
Ejecutar:
  ./coordenadas_1.py archivo.out 
Tambien se puede de la siguiente forma:
 python coordenadas_1.py archivo.out
"""


import re
import sys

def info(filename):
	n=re.compile(r"(Number of atoms\s*:?\s*([0-9]+))")
	coord=re.compile(r"atom\s*((-?[0-9]*\.[0-9]+\s*)(-?[0-9]+\.[0-9]+\s*)(-?[0-9]+\.[0-9]+\s*)([A-Za-z]+))")
	palabra=re.compile(r"Relaxation step number\s*[0-9]+:")
	#new1=open("Coordenadas_formato.out",'w')
	f = open(filename)
	f_name=f.name
	new=open("coord_"+f_name,'w')
	#print "\t\t x[A]\t\t y[A]\t\t z[A]"
	new.write("#\t\t x[A]\t\t y[A]\t\t z[A]\n")
	#new1.write("#\t x[A]\t\t y[A]\t\t z[A]\n")
	while True:
		line = f.readline()
		if not line: break
		
		nA=n.search(line)
		word=palabra.search(line)
		aux=coord.search(line)
		
		if nA != None:
			new.writelines(nA.group(0)+"\n")
			
		if word != None:
			#print word.group(0)
			new.writelines(word.group(0)+"\n")
			#new1.writelines(word.group(0)+"\n")
        
    
		if aux != None:
			#print aux.group(0)
			new.writelines(aux.group(0)+"\n")
			#new1.writelines(aux.group(5)+"\t"+aux.group(2)+"\t"+aux.group(3)+"\t"+aux.group(4)+"\n")
			#print aux.group(5)+"\t",aux.group(2)+"\t",aux.group(3)+"\t",aux.group(4)
	
	new.close()
	#new1.close()
  

if __name__ == '__main__':
	if len(sys.argv) > 1:
		filename = sys.argv[1]
    
	else:
		print "Usage: python {} somefile.out"
		sys.exit(1)
	info(filename)
