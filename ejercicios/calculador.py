# -*- coding: UTF-8 -*-

__author__ = 'jeudy'

"""Función para calcular PI utilizando el producto de Wallis

(2n)(2n)
---------
(2n - 1)(2n + 1)

El parámetro nmax es el máximo valor que va a tomar n


"""
def calcular_pi(nmax):
    n = 1
    resultado = 1
    while n <= nmax:
        resultado *= wallis(n)
        n += 1
    return resultado * 2.0


# Función que calcula el producto de Wallis con un valor n
def wallis(n):
    return ((2.0 * n)**2) / ((2.0*n - 1.0) * (2.0*n + 1.0))

"""Calcula la raiz cuadrada de un número x por aproximaciones sucesivas (método de Newton).
err es a tolerancia al error para decidir cuando hay convergencia
Parametro verbose = True hace que se impriman resultados intermedios
"""

def raiz_newton(x, err, verbose=False):
    resultado = x/2.0
    while(True):
        cociente = x / resultado
        promedio = (resultado + cociente) / 2.0
        diferencia = abs(promedio - resultado)
        resultado = promedio
        if verbose:
            print "Estimado: %s - Cociente: %s - Promedio: %s - Diff: %s" % (str(resultado),
            str(cociente)[:5], str(promedio)[:5], str(diferencia))
        if diferencia < err:
            break

    return resultado