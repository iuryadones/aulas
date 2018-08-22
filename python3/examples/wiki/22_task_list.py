

labels = ["Situação", "Quantidade", "Percentual"]

problems = [
    "1 - necessita da esfera",
    "2 - necessita de limpeza",
    "3 - necessita troca do cabo ou conector",
    "4 - quebrado ou inutilizado",
]


type_mouse = {"100": "razen", "101": "multilaser", "102": "logitech"}



qtd_mouses = int(input("Digite a quantidade dos mouses: "))

base = [labels]

print("\nCodigos e tipos de problemas")
for p in problems:
    print(p)

qtd_problems = int(input("Digite a quantidade dos problemas: "))


for _ in range(qtd_problems):
    cod_m = input("\nModelo do mouse: ")
    tipo_p = int(input("Tipo do problema: "))

    import pdb; pdb.set_trace()
    qtd_p = int(input("Quantidade do problema: ")) or 0

    result = [problems[tipo_p], qtd_p, qtd_p / qtd_mouses]
    base.append(result)

print("\n")
tam_p = [len(p) for p in problems]

for n, b in enumerate(base):
    if n is 0:
        x, y, z = len(b[0]), len(b[1]), len(b[2])
        print(
            f"{str(b[0]).ljust(tam_p)}\t{str(b[1]).rjust(y)}\t{b[2].rjust(z)}"
        )
    else:
        b[2] = f"{b[2]:0.2f}"
        print(
            f"{str(b[0]).ljust(tam_p)}\t{str(b[1]).rjust(y)}\t{b[2].rjust(z-1)}%"
        )
