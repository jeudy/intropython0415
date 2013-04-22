#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Demostración de uso de control de flujo con expresiones complejas
Usamos la función randint del módulo random para generar números aleatorios
"""

#Con import se pueden importar módulos conteniendo funciones
import random

numero1 = random.randint(1,1000)
numero2 = random.randint(1,1000)
numero3 = random.randint(1,1000)

print numero1, numero2, numero3

if numero1 > numero2 and numero2 > numero3:
    if numero1 > numero3:
        print "Se cumple condición 1 de ejemplo"
else:
    numero4 = random.randint(1,1000)
    print numero4
    if numero4 > (numero1 + numero2) or numero1 ** 3 > 50000:
        print "Ejemplo de condiciones complejas"
    
