import random
#zad1
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.naziwsko = nazwisko


osoba_pierwsza = Osoba('Karol', 'Krawczyk')
osoba_druga = Osoba('Błażej', 'Syska')
#print(f'Pierwsza osoba nazywa sie {osoba_pierwsza.imie} {osoba_pierwsza.naziwsko}')

#zad2
class Coin:
    def __init__(self):
      self.side = random.choice(["Orzeł", "Reszka"])

    def show_side(self):
        return self.side

    def throw(self):
        self.side = random.choice(["Orzeł", "Reszka"])


moneta_1 = Coin()
print(moneta_1.show_side())
moneta_1.throw()
print(moneta_1.show_side())

moneta_2 = Coin()
print(moneta_2.show_side())
moneta_2.throw()
print(moneta_2.show_side())

#zad3
class Prostokat:
    def __init__(self, bok_a: int, bok_b: int):
        self.bok_a = bok_a
        self.bok_b = bok_b

    def pole(self) -> int:
        return self.bok_a * self.bok_b


prostokat_1 = Prostokat(12, 22)
prostokat_2 = Prostokat(8, 15)

Lista = [prostokat_1, prostokat_2]
for i in Lista:
    print(i.pole())


def foo(Prostokat):
    print("Długości boków wynoszą: " + str(Prostokat.bok_a) + "," + str(Prostokat.bok_b)+
          ",a pole wynosi: "+ str(Prostokat.pole()))

for i in Lista:
    foo(i)


class Stat:
    def __init__(self,lista_2):
        self.lista_2 = lista_2

    def suma_listy(self):
        suma = 0
        for i in self.lista_2:
            suma += i
        return suma

    def maximum(self):
        max = lista_2[0]
        j = 0
        for i in self.lista_2:
            if max < self.lista_2[j]:
                max = self.lista_2[i]
            j += 1
        return max

    def minimum(self):
        j = 0
        min = self.lista_2[0]
        for i in self.lista_2:
            if min > self.lista_2[j]:
                min = self.lista_2[i]
            j += 0
        return min


lista_2 = [1, 2, 3, 4, 5, 6, 7]
print(Stat(lista_2).suma_listy())
print(Stat(lista_2).maximum())
print(Stat(lista_2).minimum())


