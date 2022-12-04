class Car:
    def __init__(self, wydajnosc_paliwowa: float, max_paliwo: float, poziom_paliwa: float = 0):
        self.wydajnosc_paliwowa = wydajnosc_paliwowa #ile przejedzie km na 1l paliwa
        self.max_paliwo = max_paliwo #pojemnosc baku
        self.poziom_paliwa = poziom_paliwa #poczatkowo 0

    def get_fuel_level(self):
        if self.poziom_paliwa > self.max_paliwo:
            self.poziom_paliwa = self.max_paliwo
            return self.poziom_paliwa
        elif self.poziom_paliwa < 0:
            self.poziom_paliwa = 0
            return "Brak Paliwa!"
        else:
            return self.poziom_paliwa

    def add_fuel(self, paliwo: float):
        self.poziom_paliwa += paliwo


    def drive(self, dystans: float):
        self.poziom_paliwa -= dystans * self.wydajnosc_paliwowa


car1: Car = Car(10.0, 50.0)
car1.add_fuel(30.0)
print(car1.get_fuel_level())
car1.drive(1.0)
print(car1.get_fuel_level())
car1.drive(2.0)
print(car1.get_fuel_level())
car1.drive(2.0)
print(car1.get_fuel_level())
car1.add_fuel(50.0)
print(car1.get_fuel_level())
