class personaje:
    def __init__(self,nombre,fuerza,salud,poder,energia):
        self = nombre
        self = fuerza
        self = salud
        self = poder
        self = energia

    def identificarpersonaje (self):
        print("Hola soy {self.nombre}")

    def mostrarsalud (self):
        print ("{self.nombre} tiene {self.salud} puntos de salud" )

    def mostrarpersonaje (self):
        print ("Soy {self.nombre} tengo {self.salud} puntos de salud, mi poder es {self.poder}, mi fuerza es de {self.fuerza} y mi energia es {self.energia}" )