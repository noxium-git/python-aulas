import requests

url = "https://official-joke-api.appspot.com/random_joke"

resposta = requests.get(url)

dados = resposta.json()

print("Piada do dia:")
print(dados['setup'])
print(dados['punchline'])
