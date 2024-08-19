#--------------------EJERCICIO 1----------------------------------
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


#----------------- EJERCICIO 2 -------------------------------
class Articulo:
    def __int__(self, tipo, sub_tipo, precio_compra):
        self.tipo = tipo
        self.sub_tipo = sub_tipo
        self.precio_compra = precio_compra
        self.marca = "HOJITAS" if tipo =="cuaderno" else "RAYAS"
        self.precio_compra = round(precio_compra * 1.30, 2)

    def __str__(self):
        return (f"Articulo: {self.tipo} ({self.sub_tipo})\n"
                f"Marca: {self.marca}\n"
                f"Precio de compra: ${self.precio_compra}\n"
                f"Precio de venta: ${self.precio_compra}\n")   
    
def registrar_articulos():
    articulos = []

    for _ in range(2):
        tipo =input("Ingrese que prefiere (cuaderno/lapiz): ").strip().lower()
        if tipo not in ["cuaderno", "lapiz"]:
            print("INTENTAR DE NUEVO. ARTICULO NO VALIDO")
            continue

        if tipo== "cuaderno":
            sub_tipo = input("Ingrese que tipo de cuaderno quiere (50/100) hojas: ").strip().lower()
            if sub_tipo not in ["50","100"]:
                print("Tipo de cuaderno no valido. Intente de nuevo")
                continue
        elif tipo== "lapiz":
            sub_tipo = input("Ingrese que tipo de lapiz quiere (grafito/colores): ")
            if sub_tipo not in ["grafito", "colores"]:
                print("Tipo de lapiz no valido. intente de nuevo")
                continue

        precio_compra= float(input("Ingrese el precio de compre: "))
        articulo = Articulo(tipo, sub_tipo, precio_compra)
        articulos.append(articulo)

    return articulos

def mostrar_articulos(articulos):
    for articulo in articulos:
        print(articulo)
        print("-" *40)  

articulos = registrar_articulos()
mostrar_articulos(articulos)