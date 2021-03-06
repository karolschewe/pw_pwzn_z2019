"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar. czyli zrobic na trzy wymiary dzialania, a jak nie to niech wywala error
"""


class Vector:

    dim = None  # Wymiar vectora
    def __init__(self, *args):
        self.coords = tuple(args)
        self.dim = len(self.coords)


    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point xd
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        start = Vector(*beg)
        ending = Vector(*end)
        outcome = ending-start
        return outcome.coords

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        start = Vector(*beg)
        ending = Vector(*end)
        outcome = ending - start
        return outcome


    def __add__(self, other):
        tmp = []
        if (self.dim == other.dim):
            for i in range(self.dim):
                tmp.append(self.coords[i]+other.coords[i])
        else:
            raise NotImplementedError
        return (Vector(*tmp))

    def __eq__(self, other):
        return (self.coords==other.coords)

    def __sub__(self, other):
        tmp = []
        if (self.dim == other.dim):
            for i in range(self.dim):
                tmp.append(self.coords[i] - other.coords[i])
        else:
            raise NotImplementedError
        return (Vector(*tmp))

    def __mul__(self, other):
        if type(other) is int:
            tmp = []
            for i in range(self.dim):
                tmp.append(self.coords[i] * other)
            return (Vector(*tmp))
        elif type(other) is Vector:
            tmp = []
            for i in range(self.dim):
                tmp.append(self.coords[i] * other.coords[i])
            return sum(tmp)

    def __len__(self):
        tmp = 0.
        for i in self.coords:
            tmp=(tmp+(i**2))
        return (int(tmp**0.5))







if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 5
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
