nome_arq = "arquivo.dat"
arq_add = open(nome_arq, "a")

id, nome, idade = (
    int(input('id: ')),
    input('nome: '),
    int(input('idade: '))
)

arq_add.write(f"{id}\t{nome}\t{idade}\n")
arq_add.close()

ler = open(nome_arq)
leitura = ler.read()
print(leitura)
print(leitura)
ler.close()
