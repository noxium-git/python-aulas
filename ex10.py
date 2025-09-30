#uma funcao que receb um set e dentro da funcao, um a um, os elementos do set sao transferidos para outro set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def transferirSet(xpto):
    setB = set()
    for n in range(len(setA)):
        numero = setA.pop()
        setB.add(numero)
        print(setA)
        print(setB)
        set()