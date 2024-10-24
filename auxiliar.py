#creación heredada para un auxiliar

from clases.personaje import personaje

class auxiliar (personaje):
     def __init__ (self,nombre,fuerza,salud,poder,energia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud
        self.poder = poder
        self.energia = energia