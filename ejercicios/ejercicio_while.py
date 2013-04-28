#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

#Valido que el usuario de exactamente 2 parametros (recordar que el primero siempre es el nombre del programa)
if len(sys.argv) != 3:
    print "Error, debe dar 2 parámetros!"
#Valida que el segundo parámetro sea un número
elif not sys.argv[2].isdigit():
    print "Error: el segundo parámetro debe ser un número"
else:
    #Imprimo N veces la cadena dada
    cadena = sys.argv[1]
    numero = int(sys.argv[2])
    while numero > 0:        
        print "La cadena es %s - numero va por %d"%(cadena, numero)
        numero -= 1
