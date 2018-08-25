# -*- coding: utf-8 -*-


def imprimir_olar_mundo():
    print("Olar mundo")
    return locals()


def somar(x=2, y=3):
    """
        somar -> x + y
        return somar
    """
    return x + y


if __name__ == "__main__":
    # imprimir_olar_mundo()
    # print(imprimir_olar_mundo())
    print(help(somar))
