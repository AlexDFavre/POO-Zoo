# Creation class Animal
class Animal:
    # creation of attributes with the __init__ constructor
    def __init__(self, nom, poids, taille): 
        self.nom = nom
        self.set_poids(poids)
        self.taille = taille

    # Instanciation method
    def se_deplacer(self):
        pass

    def __str__(self):
        return self.nom
    

    # Validation de données dans le setter
    def set_poids(self, poids):
        if poids < 0: 
            raise TypeError("ValueError")
        else:
            self.__poids = poids

    # Getter
    def get_poids(self):
        return self.__poids

    poids = property(get_poids, set_poids)

    