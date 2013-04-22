#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
ejemplos_funciones.py
Modulo con ejemplos de funciones vistas en clase.
"""

def sumatoria(n1, n2, *resto):
    resultado = n1 + n2
    for x in resto:
        resultado += x
    return resultado

def imprimirN(cadena, n=10):
    while n > 0:
        print cadena
        n -= 1

#Asume que x, y son valores numéricos
def multiplicar(x, y):
    x = x * y
    return x

#Recibe un diccionario al cual, a cada valor, le suma el valor dado.
#Asume que los valores del diccionario dado son numeros
#No devuelve nada, el diccionario se modifica por referencia
def sumar_valor(valor, diccionario):    
    for k in diccionario.keys():
        diccionario[k] += valor


