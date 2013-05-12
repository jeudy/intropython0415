#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Ejemplo de manejo de excepciones en python
"""

# Dummy comment para probar integración con git.

import random

print "Digite un numero que sera denominador de division: "

try:
    numero = int(raw_input())

    # El manejo de excepciones puede ser anidado
    try:
        resultado = 1000 / numero
    except ZeroDivisionError:
        print "Division entre cero detectada"
        resultado = -1
except ValueError:
    print "Valor incorrecto! No es un numero!"
    exit()


print "Vamos a generar una lista de numeros aleatorios. Cuantos elementos desea? "

try:
    cantidad = int(raw_input())
except ValueError:
    print "Cantidad invalida!"
    exit()

lista = []

while cantidad > 0:
    lista.append(random.randint(0,100))
    cantidad -= 1

print "Lista creada. Cual elemento desea accesar: "

# Se pueden manejar multiples excepciones a la vez
try:
    indice = int(raw_input())
    print "El elemento en la posicion %d es %d" % (indice, lista[indice])
except ValueError:
    print "Debe indicar un numero"
    exit()
except IndexError:
    print "Elemento fuera del rango. La lista contiene %d elementos " % (len(lista))
    exit()

print "Desea imprimir la lista de valores? y/n"

opcion = raw_input().lower()

if opcion == "y":
    print lista

print "¡Hasta pronto!"
