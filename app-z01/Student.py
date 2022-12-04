class Student:
    def get_name(self, imie: str, nazwisko: str):
        self.imie = imie
        self.nazwisko = nazwisko

    def add_quiz(self, score: float):
        self.score = score

    def get_total_score(self,total_score: float) -> float:
        self.total_score = total_score


s1 = Student
s1.get_name("Jakub", "Oleksiak")