print("teste")

idade = "18"
altura = "175"
estudante = True
nome = "joao"
print(nome)

#Inputs
nome = input ("qual o teu nome? ")

#instrucao condicional
idade = int(input("qual a tua idade? "))
if idade < 18:
    print ("és menor")
    elif idade == 18:
        print("acabaste de fazer 18")
        else:
            print ("maior de idade")

#operadores aritmeticos

print(idade + 5)
print(altura + 2)
print(idade + 2)
print(altura + 1)

#operadores de comparacao

print(idade > 18)
print(idade == 18)
print(idade != 18)
print(idade <= 18)
print(idade >= 18)
print(idade >= 18 and estudante=="joao")
print(idade >= 18 or estudante)
print(not estudante)

#lacos de repeticao
for i in range(5):
    print("repeticao", i)

#Ciclos exemplos
for i in range(5): print(i)

#Classes exemplos
class Pessoa: def __init__(self, nome): self.nome = nome

#while exemplos

i = 0
while i < 10:
    print("repeticao", i)
    i += 1

#do while nao existe em python

#funcoes
def repetir():
    i = 0
    while i < 10:
        print("repeticao", i)
        i += 1
    return

repetir()

#funcao com parametros
def repetirVezes(vezes):
    i = 0
    while 1 < vezes:
        print("repeticao", i)
        i += 1
    return

repetirVezes(5)

#funcoes com retorno
def somar(a, b):
    return a + b
    resultado = somar(5, 3)
    print("resultado: ", resultado)

#bibliotecas
import math

raiz = math.sqrt(16)
print("Raiz quandrada de 16 é: ", raiz)
potencia = math.pow(2, 3)
print("2 elevado a 3 é: ". potencia)

#comentarios em multipla
"""
comentarios
"""
#EXERCICIOS:

fazer um jogo, 
declarar uma funcao x com valor 5

x = 5



#casting:
y=int(5)

y:int=5 #declarando uma variavel e atribuindo o valor 5 a ela

#arrays

marcas =["Nike", "Adidas", "Puma"]
print(marcas[0])

#exercicio 2

elementos = ["agua", "fogo", "terra", "ar", "ferro"]

for i in range(5):
    print("repeticao: ", i)

    for i in range(5): print(i)

