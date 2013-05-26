"""
Ejercicio de Orientación a Objetos

"""
class Figura(object):

    # Constructor
    def __init__(self, lados):
        self.lados = lados

    # Metodo especial para imprimir objeto amigablemente
    def __str__(self):
        return "Figura, lados: %s" % (self.lados)

    def perimetro(self):
        suma = 0
        for lado in self.lados:
            suma += lado

        return suma

class Cuadrado(Figura):

    # Constructor
    def __init__(self, lado):
        Figura.__init__(self, [lado, lado, lado, lado]) # Llamo al constructor de la clase padre
        self.lado = lado    # Defino un atributo de la clase cuadrado

    def __str__(self):
        return "Cuadrado de lado: %s " % (self.lado)

    def area(self):
        return self.lado**2
