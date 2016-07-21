class Animal(object): #представялет любое животное
    def __init__(self, size, type):
        self.Size = size # Размер животного
        self.Type = type # Хищник, водоплавающее и т.д.

    def __str__(self):
        return '({}, {})'.format(self.Size, self.Type)

class Wolf(Animal):
    def __init__(self, size, type, color):
        self.Color = color
        Animal.__init__(self, size, type)

    """def __init__(self):
        self.Color = "gray"
        Animal.__init__(self, "average", "predator")"""

    def __str__(self):
        if hasattr(self, "Color"):
            print("Волк цвета {0}".format(self.Color))
        print(Animal.__str__(self))

class Polar_wolf(Wolf):
    def __init__(self, size, type):
        Wolf.__init__(self, size, type, "white")
    def __str__(self):
        print('({}, {}, {})'.format(self.Size, self.Type, self.Color))


w = Polar_wolf("big", "predator")
w.__str__()
