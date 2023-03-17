from Animal import Animal
from Serpent import Serpent
from Oiseau import Oiseau
from Zoo import Zoo

# Instanciate an object of class Animal
tanuki = Animal("tanuki", 8, 30)

# Print its attributes
print(f"Un taunki pèse {tanuki.poids} kg and mesure {tanuki.taille} cm de haut")



# Instanciate an object of class Serpent
hebi = Serpent("hebi", 10, 100)
hebi.se_deplacer() # call its method

# Instanciate an object of class Oiseau
taka = Oiseau("taka", 1, 40, 3600)
taka.se_deplacer() # call its method



# Instanciation of animals
kuma = Animal("kuma", 200, 250)
doflamingo = Animal("mingo", 4, 125)
zo = Animal("zo", 5000, 350)

jinbe = Animal("jinbe", 8000, 4500)
same = Animal("same", 80, 230)

ani = Animal("ani", 33, 77)
print(str(ani))


residents_terrestres = [kuma, doflamingo, zo]
residents_marins = [jinbe, same]


# Instanciation of a Zoo type object
zoo_terrestre = Zoo(residents_terrestres)
print([animal.__str__() for animal in zoo_terrestre.animaux])

zoo_marin = Zoo(residents_marins)
print([animal.__str__() for animal in zoo_marin.animaux])


# Operator overload
residents = zoo_terrestre + zoo_marin 
print([resident.__str__() for resident in residents.animaux])

