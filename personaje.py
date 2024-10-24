#Aqui se crea el personaje, sin importar si es heroe o villano o auxiliar

class personaje:
    def __init__(self,nombre,fuerza,salud,poder,energia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud
        self.poder = poder
        self.energia = energia

    def identificarpersonaje (self):
        print(f"Hola soy {self.nombre}")

    def mostrarsalud (self):
        print (f"{self.nombre} tiene {self.salud} puntos de salud" )

    def mostrarpersonaje (self):
        print (f"Soy {self.nombre} tengo {self.salud} puntos de salud, mi poder es {self.poder}, mi fuerza es de {self.fuerza} y mi energia es {self.energia}" )


