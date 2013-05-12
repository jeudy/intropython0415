#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'jeudy'

from funciones_intro import es_bisiesto
import sys

# Valido que el usuario pase 2 parámetros
if len(sys.argv) != 3:
    print "Debe indicar 2 parámetros"
    exit(1)

try:
    year1 = int(sys.argv[1])
    year2 = int(sys.argv[2])
except ValueError:
    print "Los años deben ser numéricos"
    exit(1)

while year1 <= year2:
    if es_bisiesto(year1):
        print "El año %d es bisiesto " % (year1)
    year1 += 1