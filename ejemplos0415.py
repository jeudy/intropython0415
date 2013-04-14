#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Script simple para demostrar conceptos básicos
del lenguaje Python. Temas incluidos:
    -Variables (enteros, cadenas, booleanos)
    -Operadores matemáticos y lógicos
    -Estructuras de datos (listas, diccionarios, conjuntos, tuplas)
"""

valor1 = 1000 #entero
valor2 = 2000
valor1 += valor2
potencia = 10**3

print valor1
print valor2
print potencia

cadena = "Los valores que tengo son %s, %s y la potencia: %s"%(valor1, valor2, potencia)

print cadena

cadena_upper = cadena.upper()

print cadena_upper

resultado = valor1 > valor2
booleano = not resultado

print resultado, booleano

str_lista_paises = "CR,MX,AR,US,IT"

lista_paises = str_lista_paises.split(",")

lista_paises.sort()

for pais in lista_paises:
    print pais

lista_paises.reverse()

for pais in lista_paises:
    print pais

print "El tamaño de la lista es: %d"%(len(lista_paises))


