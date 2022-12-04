class Prostokat:
    def __init__(self, bok_a: int, bok_b: int) -> None:
        self.bok_a = bok_a
        self.bok_b = bok_b

    def pole(self, a, b) -> int:
        return self.bok_a * self.bok_b


prostokat_1 = Prostokat(1, 2)
prostokat_2 = Prostokat(8, 15)

Lista = [prostokat_1, prostokat_2]
print(list[0])


def minimum(self):
    min = self.lista_2[0]
    for i in self.lista_2:
        if min > self.lista_2[i]:
            min = self.lista_2[i]
    return min

class Coin:
    side: str
    side_list: list = ["Orzeł", "Reszka"]
    def __init__(self):
        self.side_list = ["Orzeł", "Reszka"]
        self.losowa: int = random.random(0, 1)
        self.losowa_strona = self.side_list[self.losowa]

    def throw(self):
        x: int = random.random()
        return self.side_list[x]

    def show_side(self):
        return self.losowa_strona


moneta_1 = Coin()
print(moneta_1.show_side())