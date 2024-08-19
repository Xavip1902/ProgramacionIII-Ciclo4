class DispositivoElectronico:
    def __init__(self, tipo, modelo, almacenamiento, ram, procesador, precio_compra):
        self.marca = "PHR"
        self.tipo = tipo  
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.procesador = procesador
        self.precio_compra = precio_compra
        self.precio_venta = round(precio_compra * 1.7, 2)
        self.origen = "Importado"

    def __str__(self):
        return (f"Tipo: {self.tipo}\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Almacenamiento: {self.almacenamiento}\n"
                f"RAM: {self.ram}\n"
                f"Procesador: {self.procesador}\n"
                f"Precio de compra: ${self.precio_compra}\n"
                f"Precio de venta: ${self.precio_venta}\n"
                f"Origen: {self.origen}\n")


def registrar_dispositivos():
    dispositivos = []

    for _ in range(3):
        print("Ingrese los datos del dispositivo:")
        tipo = input("Tipo (Celular/Tablet/Portátil): ").strip().capitalize()
        modelo = input("Modelo: ")
        almacenamiento = input("Almacenamiento: ")
        ram = input("RAM: ")
        procesador = input("Procesador: ")
        precio_compra = float(input("Precio de compra: "))

        dispositivo = DispositivoElectronico(tipo, modelo, almacenamiento, ram, procesador, precio_compra)
        dispositivos.append(dispositivo)
        print("\nDispositivo registrado exitosamente!\n")

    return dispositivos


def mostrar_dispositivos(dispositivos):
    for dispositivo in dispositivos:
        print(dispositivo)
        print("-" * 40)


dispositivos = registrar_dispositivos()
mostrar_dispositivos(dispositivos)
