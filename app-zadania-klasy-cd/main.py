class Wymierna:
    def __init__(self, licznik: int = 0, mianownik: int = 1):
        self.licznik = licznik
        self.mianownik = mianownik

    def get_licznik(self):
        return self.licznik

    def get_mianownik(self):
        return self.mianownik

    def __repr__(self,):
        rep = 'Licznik = ' + str(self.licznik) + ' Mianownik = ' + str(self.mianownik)
        return rep

    def __float__(self) -> float:
        wynik = self.licznik / self.mianownik
        return wynik

    def __add__(self, other):
        wynik = (self.licznik / self.mianownik) + (other.licznik / other.mianownik)
        return wynik

    def __sub__(self, other):
        wynik = (self.licznik / self.mianownik) - (other.licznik / other.mianownik)
        return wynik

    def __eq__(self, other):
        a = self.__float__()
        b = other.__float__()

        if a > b:
            return False
        elif a < b:
            return False
        return True

    def __ne__(self, other):
        return self.__float__() != other.__float__()

    def __lt__(self, other):
        return self.__float__() < other.__float__()

    def __le__(self, other):
        return self.__float__() <= other.__float__()

    def __gt__(self, other):
        return self.__float__() > other.__float__()

    def __ge__(self, other):
        return self.__float__() >= other.__float__()


l1: Wymierna = Wymierna(2, 7)
l2: Wymierna = Wymierna(3, 8)
print(l1.get_mianownik())
print(l1.get_licznik())

print(l1.__repr__())
print(l1.__float__())
print(l2.__float__())

print(l1.__add__(l2))

print(l1.__sub__(l2))

print(l1.__eq__(l2))

print(l1.__ne__(l2))

print(l1.__lt__(l2))

print(l1.__le__(l2))

print(l1.__gt__(l2))

print(l1.__ge__(l2))
