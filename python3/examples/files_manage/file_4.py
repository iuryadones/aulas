"""
1 - leia o arquivo.dat e atribua a leitura em uma variavel
2 - contar quantas vogais tem e guardar em outro arquivo
chamadado conte_vogais.dat:
    a   #
    e   #
    i   #
    o   #
    u   #
3 - somar todas as idades
4 - calcular a média das idades da turma
5 - mostrar a pessoa mais nova e a mais sabia da turma
"""

# arquivo = open("arquivo.dat")
# leitura = arquivo.read()
# arquivo.close()


# print(leitura, end="\n\n")

# vogais = ["a", "e", "i", "o", "u"]

# conte_vogais = open("conte_vogais.dat", "w")
# conte_vogais.close()

# for letra in vogais:
#     print(f"vogal: {letra}\tquantidade: {leitura.count(letra)}")

#     conte_vogais = open("conte_vogais.dat", "a")
#     conte_vogais.write(f"{letra}\t{leitura.count(letra)}\n")
#     conte_vogais.close()

# ler = open("conte_vogais.dat")
# l = ler.read()
# ler.close()

# print(f"\n{l}\n")

base_nomes = {}
conv = {0: "id", 1: "nome", 2: "idade"}

arq = open("arquivo.dat")
for line in arq.readlines():
    for n, col in enumerate(line.split("\t")):
        if conv.get(n) == "id":
            _id = int(col)
            base_nomes.update({_id: {}})
        else:
            base_nomes.get(_id).update({conv.get(n): col})

# print(base_nomes)
idades = []

for key, value in base_nomes.items():
    idades.append(int(value.get("idade").strip()))

print(sum(idades))
print(sum(idades) / len(idades))
print(min(idades))
print(max(idades))

for key, value in base_nomes.items():

    if int(value.get("idade").strip()) in (min(idades), max(idades)):
        print(value.get("nome"))

from pprint import pprint

print(base_nomes, end="\n\n")

pprint(base_nomes)
