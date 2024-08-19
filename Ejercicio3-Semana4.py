class Auto:
    def __init__(self, marca, modelo, año, color, tipo_motor, combustible, transmisión, precio_compra, tipo, país_origen):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_motor = tipo_motor
        self.combustible = combustible
        self.transmisión = transmisión
        self.precio_compra = precio_compra
        self.tipo = tipo  
        self.país_origen = país_origen
        self.ruedas = 4
        self.capacidad_pasajeros = 5
        self.precio_venta = round(precio_compra * 1.4, 2)

    def __str__(self):
        return (f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Año: {self.año}\n"
                f"Color: {self.color}\n"
                f"Tipo de motor: {self.tipo_motor}\n"
                f"Combustible: {self.combustible}\n"
                f"Transmisión: {self.transmisión}\n"
                f"Precio de compra: ${self.precio_compra}\n"
                f"Precio de venta: ${self.precio_venta}\n"
                f"Tipo: {self.tipo}\n"
                f"País de origen: {self.país_origen}\n"
                f"Ruedas: {self.ruedas}\n"
                f"Capacidad de pasajeros: {self.capacidad_pasajeros}\n")


def registrar_autos():
    autos = []

    for _ in range(10):
        print("Ingrese los datos del auto:")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = input("Año: ")
        color = input("Color: ")
        tipo_motor = input("Tipo de motor: ")
        combustible = input("Combustible: ")
        transmisión = input("Transmisión: ")
        precio_compra = float(input("Precio de compra: "))
        tipo = input("Tipo (Nacional/Importado): ")
        país_origen = input("País de origen: ")

        auto = Auto(marca, modelo, año, color, tipo_motor, combustible, transmisión, precio_compra, tipo, país_origen)
        autos.append(auto)
        print("\nAuto registrado exitosamente!\n")

    return autos


def mostrar_autos(autos):
    for auto in autos:
        print(auto)
        print("-" * 40)


autos = registrar_autos()
mostrar_autos(autos)
