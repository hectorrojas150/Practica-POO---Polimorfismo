#creación heredada para un heroe

from clases.personaje import personaje

class heroe (personaje):
     def __init__ (self,nombre,fuerza,salud,poder,energia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud
        self.poder = poder
        self.energia = energia

