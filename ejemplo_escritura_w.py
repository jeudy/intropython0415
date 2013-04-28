#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Programa de ejemplo que escribe una linea de números a un archivo en modo w
Imprimer 10 lineas con los numeros del 0 al 100, 10 números por linea
"""

numeros = range(0,101)      # Genero una lista con los numeros del 0 al 100

linea = ""

ptr_archivo = open('datos/numeros.txt', 'w')    # Abrimos el archivo en modo write (sobreescribe!)

for n in numeros:
    linea += ",%s" % (n)
    if n % 10 == 0 and n != 0:
        ptr_archivo.write(linea[1:])            # Cada 10 numeros, escribo la linea. El [1:] es para eliminar la primera coma
        ptr_archivo.write('\n')                 # Tenemos que escribir el cambio de linea!
        linea = ""

ptr_archivo.close()
