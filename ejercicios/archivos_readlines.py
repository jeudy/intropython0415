#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Ejercicio simple de lectura de archivo con .readlines() y limpieza de líneas (eliminar \n)
Recibe un parámetro por línea de comandos, la ruta de un archivo de texto
"""

import sys

if len(sys.argv) != 2:
    print "Error: debe especificar un parametro con la ruta del archivo"
else:
    ruta = sys.argv[1]                          # Extrae la ruta del parámetro de la linea de comandos
    puntero = open(ruta, 'r')               # Abre el archivo
    lista_lineas = puntero.readlines()      # Lee las lineas a una lista
    nueva_lista = []                        # Crea una lista vacia para la limpieza
    for linea in lista_lineas:
        nueva_lista.append(linea.strip())

    # Una forma resumida y mas elegante de hacer lo anterior es:
    # nueva_lista = [s.strip() for s in lista_lineas]

    print nueva_lista    

    puntero.close()
