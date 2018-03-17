# -*- coding: utf-8 -*-


class Pessoa(object):

    def __init__(self, name, gender, mass):
        self.gender = gender
        self.mass = mass
        self.name = name

def main():
    pessoa = Pessoa("John", "Male", 84)

    print(f"Nome: {pessoa.name}")
    print(f"Sexo: {pessoa.gender}")
    print(f"Massa Corporal: {pessoa.mass} Kg")


if __name__ == "__main__":
    main()

