# -*- coding: utf-8 -*-


class Carro(object):

    def __init__(self):
        self.massa = 500


def add_massa(obj, valor):
    obj.massa += valor


def main():
    car = Carro()
    print(car.massa)

    add_massa(car, 250)
    print(car.massa)


if __name__ == "__main__":
    main()

