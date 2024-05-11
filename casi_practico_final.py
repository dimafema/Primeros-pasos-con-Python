
"""
Clase que representa una tarea.
Atributos:
- descripcion: str, la descripción de la tarea.
- completada: bool, indica si la tarea está completada o no.
"""
class Tarea:
    def __init__(self, descripcion):
        """
        Inicializa una nueva instancia de la clase Tarea.
        Args:
            descripcion (str): La descripción de la tarea.
        Returns:
            None
        """
        self.descripcion = descripcion
        self.completada = False

import unittest

class TareaTest(unittest.TestCase):
    """
    Caso de prueba para la clase Tarea.
    """
    def test_init(self):
        """
        Prueba el método init de la clase Tarea.
        Verifica que la descripción se inicialice correctamente y que la tarea no esté completada.
        """
        tarea = Tarea("Comprar leche")
        self.assertEqual(tarea.descripcion, "Comprar leche")
        self.assertFalse(tarea.completada)

    def test_marcar_completada(self):
        """
        Prueba el método marcar_completada de la clase Tarea.
        Verifica que la tarea se marque como completada correctamente.
        """
        tarea = Tarea("Comprar leche")
        tarea.marcar_completada()
        self.assertTrue(tarea.completada)

    def test_eliminar(self):
        """
        Prueba el método eliminar de la clase Tarea.
        Verifica que la descripción de la tarea se elimine correctamente.
        """
        tarea = Tarea("Comprar leche")
        tarea.eliminar()
        self.assertIsNone(tarea.descripcion)

class ListaTareas:
    """
    Clase que representa una lista de tareas pendientes.
    Attributes:
        tareas (list): Lista de tareas pendientes.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase ListaTareas.
        Returns:
            None
        """
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Agrega una nueva tarea a la lista de tareas pendientes.
        Args:
            descripcion (str): Descripción de la tarea.
        Returns:
            None
        """
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, posicion):
        """
        Marca una tarea como completada, dada su posición en la lista.
        Args:
            posicion (int): Posición de la tarea en la lista.
        Raises:
            IndexError: Si la posición no existe en la lista de tareas.
        Returns:
            None
        """
        if posicion >= 0 and posicion < len(self.tareas):
            self.tareas[posicion].completada = True
        else:
            raise IndexError("La posición no existe en la lista de tareas")

    def mostrar_tareas(self):
        """
        Muestra todas las tareas pendientes, numeradas y mostrando su estado.
        Returns:
            None
        """
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i+1}. {tarea.descripcion} - {estado}")

    def eliminar_tarea(self, posicion):
        """
        Elimina una tarea de la lista, dada su posición.
        Args:
            posicion (int): Posición de la tarea en la lista.
        Raises:
            IndexError: Si la posición no existe en la lista de tareas.
        Returns:
            None
        """
        if posicion >= 0 and posicion < len(self.tareas):
            del self.tareas[posicion]
        else:
            raise IndexError("La posición no existe en la lista de tareas")

# Ejemplo de uso
lista = ListaTareas()

while True:
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        descripcion = input("Ingrese la descripción de la tarea: ")
        lista.agregar_tarea(descripcion)
    elif opcion == "2":
        posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
        try:
            lista.marcar_completada(posicion)
        except IndexError as e:
            print(e)
    elif opcion == "3":
        lista.mostrar_tareas()
    elif opcion == "4":
        posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
        try:
            lista.eliminar_tarea(posicion)
        except IndexError as e:
            print(e)
    elif opcion == "5":
        break
    else:
        print("Opción no válida")