#!/usr/bin/python
# -*- coding: UTF-8 -*-

from calculador import calcular_pi
import sys
import math

# Valido que el usuario pase 1 parámetro
if len(sys.argv) != 2:
    print "Debe indicar 1 parámetro numérico"
    exit(1)

try:
    nmax = int(sys.argv[1])
except ValueError:
    print "El nmax debe ser numérico!"
    exit(1)
else:
    my_pi = calcular_pi(nmax)
    print "Mi valor de pi es %s . El de python es: %s. \nDiferencia: %s" % \
          (str(my_pi), str(math.pi), str(abs(math.pi - my_pi)))

