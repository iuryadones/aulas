from operator import add


class Soma:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def faz(self):
        return add(self.a, self.b)


if __name__ == "__main__":
    soma_valores = Soma(2, 3)
    print(soma_valores.faz())
