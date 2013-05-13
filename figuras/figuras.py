import math

"""Clase que define a la figura geométricula Círculo
El constructor recibe el valor del radio como parámetro.
Los métodos que tiene son: area y circunferencia

"""

class Circulo(object):

    # Constructor
    def __init__(self, r):
        self.radio = r

    # Metodo especial para imprimir objeto amigablemente
    def __str__(self):
        return "Circulo de radio: %s " % (self.radio)

    # Area del circulo
    def area(self):
        return math.pi * self.radio**2

    def circunferencia(self):
        return 2.0 * math.pi * self.radio