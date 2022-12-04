import math

class Punkt:
    def __int__(self,x ,y) -> None:
        self.x = x
        self.y = y

    def distance(self, drugi):
        return sqrt(((self.x - drugi.x)**2) + (self.y - drugi.y)**2)

