from calcpack import Expmod
from calcpack import Prodmod


class Calcmod:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.em = Expmod(x, y)
        self.pm = Prodmod(x, y)

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.pm.mult()

    def div(self):
        return self.x / self.y

    def exp(self):
        return self.em.exp()
