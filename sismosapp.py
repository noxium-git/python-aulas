import requests

def buscar_dados(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print(f"Erro na ligacao. Código: {resposta.status_code}")
        return None


def mostrar_sismos(lista_sismos, limite=5):

def filtrar_por_cidade(lista_sismos, cidade):
    

url = "https://api.ipma.pt/open-data/observation/seismic/3.json"

dados = buscar_dados(url)

if dados:

    cidade = input("Filtrar por cidade? (deixa em branco para todos): ").strip()
    sismos_filtrados = filtrar_por_cidade(dados, cidade)

    if sismos_filtrados:
        mostrar_sismos(sismos_filtrados, limite=5)

