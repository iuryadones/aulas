nome_arq = "arquivo.dat"

arq = open(nome_arq, "a")
arq.write("6\tjunior\t22\n")
arq.close()

ler = open(nome_arq)
leitura = ler.read()
print(leitura)
ler.close()
