#programa com um funcao que aceita como parametro 2 sets e  devolve a sua uniao

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5}

def soma_sets(set1, set2):
    set1 + set2
    resultado = set1 + set2
    return resultado
ERRADO
CORRIGIDO:

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5}

def soma_sets(set1, set2):
    resultado = set1.union(set2)
    return resultado

resultado_final = soma_sets(set1, set2)
print(f"RESULTADO: {resultado_final}")