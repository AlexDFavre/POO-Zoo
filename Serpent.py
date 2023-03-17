from Animal import Animal

# Creation class Serpent that inherits from the Animal class
class Serpent(Animal):
    
    def __init__(self, nom, poids, taille):
        super().__init__(nom, poids, taille)

    # Redefine method
    def se_deplacer(self):
        print('Un serpent dit "je rampe"')
