from random import random
import pylab


class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.vida = 100
        self.vec = []

    @property
    def life(self):
        if self.vida <= 0:
            return "dead"
        elif self.vida <= 25:
            return "ferido"
        else:
            return "vivo"


class Dog(Animal):
    def attack(self):
        print("latido!!!")
        if self.life == "ferido":
            return 1 * random()
        elif self.life != "ferido" and self.life != "dead":
            return 5 * random()
        else:
            return 0


class Cat(Animal):
    def attack(self):
        print("garras!!!")
        if self.life == "ferido":
            return 1 * random()
        elif self.life != "ferido" and self.life != "dead":
            return 5 * random()
        else:
            return 0


def main():
    dog = Dog("Fire", 3)
    cat = Cat("Go", 2)

    for _ in range(500):
        cat.vec.append(cat.vida)
        dog.vec.append(dog.vida)

        cat.vida -= dog.attack()
        dog.vida -= cat.attack()
        print(cat.life)

        if "dead" in [cat.life, dog.life]:
            print(_)
            break

    print(dog.vida)
    print(cat.vida)

    pylab.plot(dog.vec)
    pylab.plot(cat.vec)
    pylab.show()


if __name__ == "__main__":
    main()
