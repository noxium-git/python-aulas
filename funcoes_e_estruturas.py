class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print (f"The constructor has been inicialized.")

c1 = Carro("BMW", "i7")
print(c1.marca)
print(c1.modelo)

scope de uma variavel