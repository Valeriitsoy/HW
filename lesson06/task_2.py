
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height
        print(f'для дороги нужно {round(asphalt_mass / 1000)} тонн асфальта')


a = Road(20, 5000)
a.asphalt_mass()
