#creación heredada para un villano

from clases.personaje import personaje

class villano (personaje):
     def __init__ (self,nombre,fuerza,salud,poder,energia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud
        self.poder = poder
        self.energia = energia

