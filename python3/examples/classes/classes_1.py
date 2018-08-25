# -*- coding: utf-8 -*-


class Carro(object):
    pass


def main():
    car_1 = Carro()
    car_2 = Carro()

    print(car_1)
    print(car_2)

    print(id(car_1))
    print(id(car_2))


if __name__ == "__main__":
    main()
