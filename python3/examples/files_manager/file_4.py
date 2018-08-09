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

arquivo = open("arquivo.dat")
leitura = arquivo.read()
arquivo.close()


print(leitura, end="\n\n")

vogais = ["a", "e", "i", "o", "u"]

conte_vogais = open("conte_vogais.dat", "w")
conte_vogais.close()

for letra in vogais:
    print(f"vogal: {letra}\tquantidade: {leitura.count(letra)}")

    conte_vogais = open("conte_vogais.dat", "a")
    conte_vogais.write(f"{letra}\t{leitura.count(letra)}\n")
    conte_vogais.close()

ler = open("conte_vogais.dat")
l = ler.read()
ler.close()

print(f"\n{l}\n")

