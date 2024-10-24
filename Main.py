from clases.heroe import heroe
from clases.villano import villano


#Estos son los personas principales divididos en villanos, heroes, auxiliar

#Heroes
Malena = heroe ("Malena", 90, 90, "Sigilo Mágico",70)
Maite = heroe ("Maite",80,90,"Grito de Poder",70)
Dante = heroe ("Dante", 70,90,"Patada Rápida",90)



###
#Villanos
Babosadepasillo = villano ("Babillo", 20, 30, "Golpe Normal",10 )
Babosadebaño = villano ("bañoba", 25,30,"Salto Sorpresa",15)
Babosadeaula = villano ("Baula", 30,50,"Ataque de baba",40)

#Auxiliar

#------------------------------------------------- Metodo para presentar personaje
Malena.mostrarpersonaje()
Dante.mostrarpersonaje ()
