#!/usr/bin/python
# -*- coding: UTF-8 -*-

from calculador import raiz_newton
import math

print "Ingrese el X: "
try:
    x = int(raw_input())
except ValueError:
    print "Error: x debe ser numérico!"
    exit()

print "Ingrese el err:"

try:
    err = float(raw_input())
except ValueError:
    print "Error: err debe ser numérico!"
    exit()

r = raiz_newton(x, err, True)
print "La raiz cuadrada de %s es %s con una tolerancia de %s. Raiz de python: %s" % \
      (x, r, err, math.sqrt(x))
