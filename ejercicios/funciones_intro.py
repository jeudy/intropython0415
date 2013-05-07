#!/usr/bin/python
# -*- coding: UTF-8 -*-


def es_primo(n):
    contador = 2
    while contador < n:
        if n % contador == 0:
            return False
        contador+= 1
    #Si llegue a este punto, se que el numero es primo
    return True

def es_bisiesto_oneliner(n):
    return n % 4 == 0 and n % 100 != 0 or n % 400 == 0

def es_bisiesto(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


