# -*- coding: UTF-8 -*-

"""
Clase Polinomio: representa un polinomio de 1 variable
como la lista de los coeficientes (en orden inverso).
Metodos:
    evaluar: recibe el valor de x en el cual evaluar el polinomio
    derivar: devuelve otro polinomio que representa la primera derivada del actual

"""

class Polinomio(object):

    def __init__(self, *lista_coeficientes):
        self.coeficientes = lista_coeficientes

    def __str__(self):
        cadena = ""
        for i, x in enumerate(self.coeficientes):
            cadena += "%sx^%d + " % (x, i)
        return cadena[:-2]      # remueve el + vacio al final

    def evaluar(self, x):
        resultado = 0
        for i, coef in enumerate(self.coeficientes):
            resultado += coef * x**i
        return resultado

    def derivar(self):
        tmp_coeficientes = self.coeficientes[1:]   # Desechamos el primer coeficiente (exponente 0)
        nuevos_coeficientes = []
        for i, x in enumerate(tmp_coeficientes):
            nuevos_coeficientes.append(x * (i+1))

        return Polinomio(*nuevos_coeficientes)  #El * es para llamar el constructor con N elementos, no con una lista como unico parametro