#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

class Estrella(object):
    """Definición de la clase Estrella para modelar
    objetos astrofísicos

    """
    
    def __init__(self, name, temp, vmag, espectral_type, d):
        """Constructor de la clase estrella
        Inicializa los diferentes atributos

        """
        self.nombre = name
        self.temperatura = temp
        self.magnitud_visual = vmag
        self.tipo_espectral = espectral_type
        self.diametro = d

    def calcular_area(self):
        """Calcula el área de la estrella basado en su diametro"""
        
        radio = self.diametro / 2
        return 4.0 * math.pi * radio * radio
    
    def calcular_brillo(self):
        """Calcula un valor de brillo ficticio a partir de la temperatura de la estrella
        y el area de su superficie

        """

        return self.temperatura * self.calcular_area()
