# -*- coding: utf-8 -*-


class Pessoa(object):

    def __init__(self, name, gender, mass):
        self.gender = gender
        self.mass = mass
        self.name = name

    def falar_nome(self):
        print(f"Meu nome é {self.name}")


def main():
    pessoa = Pessoa("John", "Male", 84)

    print(f"Nome: {pessoa.name}")
    print(f"Sexo: {pessoa.gender}")
    print(f"Massa Corporal: {pessoa.mass} Kg")

    pessoa.falar_nome()


if __name__ == "__main__":
    main()

