#programa que tenha uma funcao que aceita uma lista e devolve a soma dos seus elementos (de inteiros com 5 elementos)

lista = [1, 2, 3, 4, 5]

def imprime_lista(numeros):
    for inteiros in numeros:
        lista += inteiros
    print("A lista é: ", {lista})

    imprime_lista()