from abc import ABC, abstractmethod


class Wear(ABC):
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def sum_mat(self, other):
        return f'Общий расход ткани {round(2 * self.data + 0.3 + other.data / 6.5 + 0.5, 2)} погонного метра'

    @abstractmethod
    def abstract(self):
        pass


class Topcoat(Wear):

    def material(self):
        return f'Расход ткани на пальто {round(self._data / 6.5 + 0.5, 2)} погонного метра'

    def abstract(self):
        return f'Этот метод должен быть во всех дочерних классах'


class Suit(Wear):

    def material(self):
        return f'Расход ткани на костюм {2 * self._data + 0.3} погонного метра'

    def abstract(self):
        pass


my_suit = Suit(2.5)
my_topcoat = Topcoat(55)
print(my_suit.data)
print(my_topcoat.data)
print(my_topcoat.abstract())
print(my_suit.sum_mat(my_topcoat))
print(my_suit.material())
print(my_topcoat.material())
