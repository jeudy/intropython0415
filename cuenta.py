# -*- coding: UTF-8 -*-

"""
Clase para modelar una cuenta bancaria.
Atributos:
        numero: numero de cuenta (integer)
        descripcion (string)
        monto (float)

Métodos:
    depositar: recibe un monto, aumenta el saldo con ese monto
    retirar: recibe un monto, revisa si hay saldo suficiente y resta
"""

class CuentaBancaria(object):

    def __init__(self, numero, descripcion):
        self.numero = numero
        self.description = descripcion
        self.saldo = 0.0

    def __str__(self):
        return "Cuenta #%s - %s con un saldo: %s" % (self.numero, self.description, self.saldo)

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if self.saldo - monto < 0:
            print "Fondos insuficientes."
        else:
            self.saldo -= monto