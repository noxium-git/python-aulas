import requests

url = "https://api.ipma.pt/open-data/observation/seismic/3.json"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    if 'data' in dados:
        sismos = dados['data']

        print(f"Foram encontrados {len(sismos)} sismos nos últimos 3 dias.\n")
        
        for sismo in sismos[:5]:
            print("------------------------------")
            print("Data/Hora:", sismo.get('time', 'N/A'))
            print("Local:", sismo.get('local', 'N/A'))
            print("Latitude:", sismo.get('lat', 'N/A'))
            print("Longitude:", sismo.get('lon', 'N/A'))
            print("Magnitude:", sismo.get('mag', 'N/A'))
            print("Profundidade:", sismo.get('depth', 'N/A'), "km")
    else:
        print("A chave 'data' não foi encontrada nos dados retornados.")
else:
    print("Erro na ligação. Código:", resposta.status_code)
