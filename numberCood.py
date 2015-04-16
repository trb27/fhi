#!/usr/bin/env python

"""Script de FHI-AIMS para obtener coordenadas especificas de atomos
@author: Tiare R
Ejecutar:
  ./numberCoord1.py archivo.out numero
el archivo tiene que ser coord_archivo.out  
numero es un entero positivo 
Tambien se puede de la siguiente forma:
 python numberCoord1.py archivo.out numero
"""


import re
import sys

def coordN(filename,num):
	n=re.compile(r"(Number of atoms\s*:?\s*([0-9]+))")
	palabra=re.compile("Relaxation step number\s*%s:"%num)
	atom=re.compile("^atom")
	coord=re.compile(r"atom\s*((-?[0-9]*\.[0-9]+\s*)(-?[0-9]+\.[0-9]+\s*)(-?[0-9]+\.[0-9]+\s*)([A-Za-z]+))")
	f = open(filename)
	f_name=f.name
	new=open(num+"_C_FHI_"+f_name,'w')
	new1=open(num+"_C_visual_"+f_name+".xyz",'w')
	new.write("#\t\t x[A]\t\t y[A]\t\t z[A]\n")
	while True:
		line = f.readline()
		if not line: break
		
		nA=n.search(line)
		word=palabra.match(line)
		
		if nA != None:
			new1.writelines(nA.group(2)+"\n")
			
			
		if word != None:
			#new.writelines(word.group(0)+"\n")
			line=f.readline()
			aux=coord.search(line)
			while aux != None:
				new.write(aux.group(0)+"\n")
				new1.writelines(aux.group(5)+"\t"+aux.group(2)+"\t"+aux.group(3)+"\t"+aux.group(4)+"\n")
				line=f.readline()
				aux=coord.search(line)
	
	    
	new.close()
	new1.close()
    

if __name__ == '__main__':
	if len(sys.argv) > 2:
		filename = sys.argv[1]
		num= sys.argv[2]
    
	else:
		print "Usage: python {} somefile.out"
		print "miss number of iteration "
		sys.exit(1)
	coordN(filename,num)
