from LinkedList import LinkedList

listN = LinkedList()
x = 1
while x != 0:
    x = int(input("send a valor: " +
                  "\n[1]: send a v1alor" +
                  "\n[2]: see every\n"))

    if x == 1:
        listN.agregar_nodo(int(input("// Waiting value: ")))

    if x == 2:
        listN.recorrer_nodos()
