class Articulo:
    def __init__(self, tipo, sub_tipo, precio_compra):
        self.tipo = tipo
        self.sub_tipo = sub_tipo
        self.precio_compra = precio_compra
        self.marca = "HOJITAS" if tipo == "cuaderno" else "RAYAS"
        self.precio_venta = round(precio_compra * 1.30, 2)
    
    def __str__(self):
        return (f"Artículo: {self.tipo} ({self.sub_tipo})\n"
                f"Marca: {self.marca}\n"
                f"Precio de compra: ${self.precio_compra}\n"
                f"Precio de venta: ${self.precio_venta}\n")


def registrar_articulos():
    articulos = []

    for _ in range(2):
        tipo = input("Ingrese el tipo de artículo (cuaderno/lápiz): ").strip().lower()
        if tipo not in ["cuaderno", "lápiz"]:
            print("Tipo de artículo no válido. Intente de nuevo.")
            continue
        
        if tipo == "cuaderno":
            sub_tipo = input("Ingrese el sub-tipo de cuaderno (50 hojas/100 hojas): ").strip().lower()
            if sub_tipo not in ["50 hojas", "100 hojas"]:
                print("Sub-tipo de cuaderno no válido. Intente de nuevo.")
                continue
        elif tipo == "lápiz":
            sub_tipo = input("Ingrese el sub-tipo de lápiz (grafito/colores): ").strip().lower()
            if sub_tipo not in ["grafito", "colores"]:
                print("Sub-tipo de lápiz no válido. Intente de nuevo.")
                continue
        
        precio_compra = float(input("Ingrese el precio de compra: "))
        articulo = Articulo(tipo, sub_tipo, precio_compra)
        articulos.append(articulo)
    
    return articulos


def mostrar_articulos(articulos):
    for articulo in articulos:
        print(articulo)
        print("-" * 40)



articulos = registrar_articulos()
mostrar_articulos(articulos)
