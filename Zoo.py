from Animal import Animal

# Creation class Zoo
class Zoo:

    def __init__(self, animaux):
        self.animaux = animaux

    def ajouter_animal(self, new_animal):
        self.animaux.append(new_animal)

    def __add__(self, other):
        if isinstance(other, Zoo):
            return Zoo(self.animaux + other.animaux)
        else:
            return NotImplemented