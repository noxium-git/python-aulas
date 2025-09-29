#jogo do bingo, só a parte do sorteio dos números, 0-100 sem repetir nenhum numero
import random
bingoCard = []
def randomNumbers():
    number = random.randint(1,100)
    return number

def cartao ():
    for row in bingoCard:
        print(row)

numbers = []
for i in range(8):
    number = random.randint(1,100)
    if number not in  numbers:
        numbers.append(randomNumbers)
