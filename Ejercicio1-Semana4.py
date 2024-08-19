class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.estado = "NO ATENDIDO"
        self.tipo_perro = self.clasificar_perro()
        self.registrar_perro()

    def clasificar_perro(self):
        if self.peso < 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def registrar_perro(self):
        self.estado = "ATENDIDO"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Dueño: {self.dueño}")
        print(f"Estado: {self.estado}")
        print(f"Tipo: {self.tipo_perro}")


def registrar_perro():
    nombre = input("Ingrese el nombre del perro: ")
    raza = input("Ingrese la raza del perro: ")
    edad = int(input("Ingrese la edad del perro: "))
    peso = float(input("Ingrese el peso del perro (kg): "))
    color = input("Ingrese el color del perro: ")
    dueño = input("Ingrese el nombre del dueño: ")

    perro = Perro(nombre, raza, edad, peso, color, dueño)
    print("\n--- Información del perro registrada ---")
    perro.mostrar_info()


if __name__ == "__main__":
    registrar_perro()
