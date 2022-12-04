class Adres:
    def __init__(self, nr_domu: int, ulica: str, miasto: str, kod_pocztowy: str, nr_mieszkania: int = 0) -> None:
        self.nr_domu = nr_domu
        self.nr_mieszkania = nr_mieszkania
        self.ulica = ulica
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy

    def show(self):
        if self.nr_mieszkania != 0:
            print(str(self.nr_domu) + '/' + str(self.nr_mieszkania) + " " + str(self.ulica) + "\n"
              + str(self.kod_pocztowy) + " " + str(self.miasto))
        else:
            print(str(self.nr_domu) +  " " + str(self.ulica) + "\n"
                  + str(self.kod_pocztowy) + " " + str(self.miasto))

a1: Adres = Adres(6, "3 Maja", "Olsztyn", "89-190")
a2: Adres = Adres(7, "Nowa Huta", "Olsztyn", "13-100", 9)
Adres.show(a1)
Adres.show(a2)
