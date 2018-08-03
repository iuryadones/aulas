ler = open("arquivo.dat")

print(ler.read())
print("---")

ler.seek(0)

print(ler.read())

ler.close()
