import requests

pokemon = input("Escreve o nome de um Pokémon: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

resposta = requests.get(url)

if resposta.status_code == 200:

    dados = resposta.json()

    nome = dados['name'].capitalize()

    altura = dados['height'] / 10

    peso = dados['weight'] / 10

    tipos = [t['type']['name'] for t in dados['types']]

    

    print(f"\n Informações sobre {nome}:")

    print(f"Altura: {altura} m")

    print(f"Peso: {peso} kg")

    print(f"Tipo(s): {', '.join(tipos)}")

else:

    print("Esse Pokémon não existe! Tenta outro.")