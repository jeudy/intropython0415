#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Demostración de uso de control de flujo con expresiones complejas
Usamos la función randint del módulo random para generar números aleatorios
Programa recibe 2 parámetros por línea de comandos, dos números que multiplica e imprime el resultado
"""

import sys  #Libreria sys contiene muchas funciones relacionadas con el sistema

"""
Los párametros de linea de comandos se pasan al llamar al programa, separados por espacio en blanco.
Se accesan a través del módulo sys y la variable argv: sys.argv en forma de una lista. 
OJO, el primer elemento de la lista SIEMPRE es el mismo nombre del programa, por lo que siempre será una lista con
al menos 1 elemento. El primer parámetro verdadero será sys.argv[1]
"""

print "Cantidad de parámetros en la llamada: %s"%(len(sys.argv))

#Validación de cantidad de parámetros
if len(sys.argv) != 3:
    print "ERROR: número de parámetros incorrecto, deben ser 2 números"
elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():    #valido que ambos parámetros sean números con la función isdigit()
    print "ERROR: parámetros deben ser números"
else:
    parametro1 = int(sys.argv[1])
    parametro2 = int(sys.argv[2])
    print "Multiplicación de parámetros es: %d"%(parametro1 * parametro2)
