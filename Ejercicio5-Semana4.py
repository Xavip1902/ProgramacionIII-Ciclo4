#De lo que trata este codigo es de una lista que me ayuda a gestionar mis tareas el codigo me permite agregar , marcarlos como completadas , eliminar tareas y las tareas deben tener al menos un título y un estado (pendiente o completada)
class Tarea:
    def __init__(self, titulo):
        self.titulo = titulo
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.titulo} - Estado: {estado}"


class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, titulo):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo]

    def marcar_tarea_completada(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.marcar_completada()
                break

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for tarea in self.tareas:
                print(tarea)
        print("-" * 40)


def iniciar_programa():
    lista_tareas = ListaDeTareas()

    while True:
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            tarea = Tarea(titulo)
            lista_tareas.agregar_tarea(tarea)
            print("Tarea agregada con éxito.\n")
        elif opcion == "2":
            titulo = input("Ingrese el título de la tarea a marcar como completada: ")
            lista_tareas.marcar_tarea_completada(titulo)
            print("Tarea marcada como completada.\n")
        elif opcion == "3":
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            lista_tareas.eliminar_tarea(titulo)
            print("Tarea eliminada con éxito.\n")
        elif opcion == "4":
            lista_tareas.mostrar_tareas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")


if __name__ == "__main__":
    iniciar_programa()
