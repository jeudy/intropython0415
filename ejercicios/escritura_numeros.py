#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Ejercicio: programa escribe lineas con numeros (de 10 en 10). Recibe como parametros:
    -Ruta del archivo
    -Modo (a o w)
    -Limite superior del rango
"""

import sys

"""
Funcion para validar los parametros. Devuelve true o false segun validez de los mismos
"""
def validar_parametros(lista_parametros):
    if len(lista_parametros) != 4:
        print "Error: debe especificar 3 parametros: ruta del archivo, modo (w/a) y un numero con el limite superior del rango"
        return False
    elif not lista_parametros[2] in ['a', 'w']:
        print "Error: el modo debe ser a para append, o w para write"
        return False
    elif not lista_parametros[3].isdigit():
        print "Error: el limite del rango debe ser un numero"
        return False
    else:
        return True        

# Cuerpo principal del programa empieza aqui

if not validar_parametros(sys.argv):
    exit()

# En este punto, sabemos que los parametros estan correctos

ruta = sys.argv[1]
modo = sys.argv[2]
limite = int(sys.argv[3])

numeros = range(0,limite)      # Genero una lista con los numeros del 0 al 100

linea = ""

ptr_archivo = open(ruta, modo)    # Abrimos el archivo en modo append

for n in numeros:
    linea += ",%s" % (n)
    if n % 10 == 0 and n != 0:
        ptr_archivo.write(linea[1:])            # Cada 10 numeros, escribo la linea. El [1:] es para eliminar la primera coma
        ptr_archivo.write('\n')                 # Tenemos que escribir el cambio de linea!
        linea = ""

        

ptr_archivo.close()
