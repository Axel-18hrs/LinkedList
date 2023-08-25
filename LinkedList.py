from Node import Node

class LinkedList:

    def __init__(self):
        self.NODO_CABEZA = None

    def agregar_nodo(self, valor):
        nuevoNodo = Node(valor)

        if (self.NODO_CABEZA is None):
            self.NODO_CABEZA = nuevoNodo
            return

        nodo_actual = self.NODO_CABEZA
        while nodo_actual.siguiente != None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevoNodo

    def recorrer_nodos(self):
        nodo_actual = self.NODO_CABEZA

        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
