#lista de compras


compraslista = ["fruta", "gomas", "doritos"]
compras = input("O que queres adicinar?: ")
print("adicionas-te na tua lista: ", compras)

x = ', '.join(compraslista)

print(f"compras completas: {compras}, {x}")