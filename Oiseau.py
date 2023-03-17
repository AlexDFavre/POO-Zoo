from Animal import Animal

# Creation class Oiseau that inherits from the same class
class Oiseau(Animal):

    def __init__(self, nom, poids, taille, altitude_max):
        super().__init__(nom, poids, taille)
        self.altitude_max = altitude_max

    # Redefine method
    def se_deplacer(self):
        print('Un oiseau dit "je vole"')
