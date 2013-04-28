#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Programa de ejemplo que escribe una linea de números a la salida estandar
Imprimer 10 lineas con los numeros del 0 al 100, 10 números por linea
"""

numeros = range(0,101)      #Genero una lista con los numeros del 0 al 100

linea = ""

for n in numeros:
    if n % 10 == 0:
        print linea[1:]     #Cada 10 numeros, imprimo la linea. El [1:] es para eliminar la primera coma
        linea = ""
    else:
        linea += ",%s" % (n)
