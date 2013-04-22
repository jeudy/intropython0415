#!/usr/bin/python
# -*- coding: UTF-8 -*-

lista_numeros = range(0,101)

#Inicializa lista donde guardaremos números pares
lista_pares = []
#Inicializa lista donde guardaremos números impares
lista_impares = []

#Se pudo haber asignado más abreviado:
#lista_pares, lista_impares = [], []

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

