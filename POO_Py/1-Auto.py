class Coche():

    def __init__(self):
        self.ids = []
        self.marcas = []

    def id(self, identification):
        self.ids.append(identification)

    def marca(self):

        marca = input("Ingresa la marca del coche: ")

        while marca == "":
            marca = input("Marca no puede ser nulo: ")
        
        else: self.marcas.append(marca)

    def imprimir(self):
        print("{:<8} {:<15}".format("ID", "MARCA"))

        for i in range(len(self.ids)):
            print("{:<8} {:<15}".format(self.ids[i], self.marcas[i]))

a = 1

carro = Coche()

while a <= 5:

    carro.id(identification = a)
    carro.marca()
    a += 1

carro.imprimir()
        