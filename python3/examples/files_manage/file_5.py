manipulando = open("arquivo.dat")

linha = manipulando.readline()

# while linha:
#     linha = linha.strip('\n')
#     linha = linha.split('\t')
#     print(linha)
#
#     linha = manipulando.readline()
#
# manipulando.close()

for n, linha in enumerate(manipulando.readlines(), 1):
    print(n, linha)
manipulando.close()

#    id = int(linha[0])
#    nome = linha[1]
#    idade = int(linha[2])
#
#    total_idade = total_idade + idade

#   print(f"n: {n}; id: {id}; nome: {nome}; idade: {idade}")

#print(f"soma das idades: {total_idade}")
