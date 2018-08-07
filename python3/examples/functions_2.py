# -*- coding: utf-8 -*-


def imprimir_olar_mundo_1(flag):
    if flag == True:
        print("1 - Olar mundo!")
    elif flag == False:
        print("\n1 - ...\n")
    else:
        pass


def imprimir_olar_mundo_2(flag=False):
    if flag:
        print("2 - Olar mundo!")
    elif not (flag):
        print("\n2 - ...\n")
    else:
        pass


imprimir_olar_mundo_1(False)
imprimir_olar_mundo_1(True)

imprimir_olar_mundo_2()
imprimir_olar_mundo_2(True)
imprimir_olar_mundo_2(flag=True)
