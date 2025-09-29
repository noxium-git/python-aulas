def soma_lista(numeros):
    "Função que recebe uma lista de inteiros e devolve a soma deles"
    total = 0
    for n in numeros:
        total += n
    return total

lista = [1, 2, 3, 4, 5]
resultado = soma_lista(lista)
print(f"A soma é: {resultado}")
