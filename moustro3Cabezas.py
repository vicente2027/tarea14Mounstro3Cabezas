
class Node:
    def __init__(self, nombre=None,apellido_paterno=None,apellido_materno=None,data=None, pointer = None, pointer2 = None, pointer3 = None):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.data = data
        self.next = None
        self.pointer = pointer
        self.pointe2 = pointer2
        self.pointer3 = pointer3

    def get_node(self):
        return self.data

    def cont_nodes(self): # Metodo recursivo para contar todos los nodos
        if self.next is None:
            return 1
        else:
            return self.next.cont_nodes()+1

    def display_recursive(self): # Metodo recursivo para desplegar los nodos
        if self.next is None:
            return
        else:
            print(self.next.data)
            return self.next.display_recursive()

    def display_recursive_inverse(self): # Metodo recursivo para desplegar los nodos de manera inversa
        if self.next is None:
            return
        else:
            self.next.display_recursive_inverse()
            return print(self.next.data)

    def order_by_name(self, nombre):
        char = nombre[0]
        if char == 'A':
            self.pointer = 1
        elif char == 'B':
            self.pointer = 2
        elif char == 'C':
            self.pointer = 3
        elif char == 'D':
            self.pointer = 4
        elif char == 'E':
            self.pointer = 5
        elif char == 'F':
            self.pointer = 6
        elif char == 'G':
            self.pointer = 7
        elif char == 'H':
            self.pointer = 8
        elif char == 'I':
            self.pointer = 9
        elif char == 'J':
            self.pointer = 10
        elif char == 'K':
            self.pointer = 11
        elif char == 'L':
            self.pointer = 12
        elif char == 'M':
            self.pointer = 13
        elif char == 'N':
            self.pointer = 14
        elif char == 'Ñ':
            self.pointer = 15
        elif char == 'O':
            self.pointer = 16
        elif char == 'P':
            self.pointer = 17
        elif char == 'Q':
            self.pointer = 18
        elif char == 'R':
            self.pointer = 19
        elif char == 'S':
            self.pointer = 20
        elif char == 'T':
            self.pointer = 21
        elif char == 'U':
            self.pointer = 22
        elif char == 'V':
            self.pointer = 23
        elif char == 'W':
            self.pointer = 24
        elif char == 'X':
            self.pointer = 25
        elif char == 'Y':
            self.pointer = 26
        elif char == 'Z':
            self.pointer = 27

    def order_by_apellido_paterno(self, nombre):
        char = nombre[0]
        if char == 'A':
            self.pointer2 = 1
        elif char == 'B':
            self.pointer2 = 2
        elif char == 'C':
            self.pointer2 = 3
        elif char == 'D':
            self.pointer2 = 4
        elif char == 'E':
            self.pointer2 = 5
        elif char == 'F':
            self.pointer2 = 6
        elif char == 'G':
            self.pointer2 = 7
        elif char == 'H':
            self.pointer2 = 8
        elif char == 'I':
            self.pointer2 = 9
        elif char == 'J':
            self.pointer2 = 10
        elif char == 'K':
            self.pointer2 = 11
        elif char == 'L':
            self.pointer2 = 12
        elif char == 'M':
            self.pointer2 = 13
        elif char == 'N':
            self.pointer2 = 14
        elif char == 'Ñ':
            self.pointer2 = 15
        elif char == 'O':
            self.pointer2 = 16
        elif char == 'P':
            self.pointer2 = 17
        elif char == 'Q':
            self.pointer2 = 18
        elif char == 'R':
            self.pointer2 = 19
        elif char == 'S':
            self.pointer2 = 20
        elif char == 'T':
            self.pointer2 = 21
        elif char == 'U':
            self.pointer2 = 22
        elif char == 'V':
            self.pointer2 = 23
        elif char == 'W':
            self.pointer2 = 24
        elif char == 'X':
            self.pointer2 = 25
        elif char == 'Y':
            self.pointer2 = 26
        elif char == 'Z':
            self.pointer2 = 27

class List:
    def __init__(self):
        self.head = Node()
        self.cont = 0
        self.cont_imp = 0
        self.sum = 0
        self.elem = None
        self.anterior = Node()

    def get_head(self):
        return self.head

    def append(self, data): # Metodo para insertar dato

        new_node = Node(None, None, None, data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append_node(self, node): # Metodo para insertar nodo
        new_node = node
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append_sorted3(self, data): # este metodo

        node_nuevo = Node(None, None, None, data)
        node_cabeza = self.head
        node_anterior = self.anterior

        if self.is_empty(): # Si la lista esta vacia
            print("Vacia")
            node_cabeza.next = node_nuevo # Priximo nodo igual a nuevo nodo
            node_anterior.next = node_cabeza.next # Nodo anterior igual primer nodo
        else:
            print("Nodo anterior "+str(node_anterior.next.data))
            self.display()
            if node_nuevo.data < node_anterior.next.data:
                print("Node nuevo "+str(node_nuevo.data) + " es menor a node anterior " + str(node_anterior.next.data))

                boolean = False
                print("fuera del if")
                print(node_cabeza.next.data)
                if node_nuevo.data < node_cabeza.next.data:
                    print("2,3,5")
                    node_anterior = node_cabeza.next
                    node_cabeza.next = node_nuevo
                    self.append_node(node_anterior)
                else:
                    print("3,4,5")
                    while  node_cabeza.next.data < node_nuevo.data:
                        node_cabeza = node_cabeza.next
                        print("dentro while")
                    print(node_cabeza.next.data)
                    while boolean is False and node_nuevo.data < node_cabeza.next.data: #(node_cabeza.next.data and node_nuevo.data) < node_anterior.next.data: # Mientras nuevo nodo sea menor a nodo anterior
                        print("antes del if ")
                        if node_nuevo.data < node_anterior.next.data:
                            print("dentro del if")
                            node_cabeza.next = node_nuevo
                            print(node_anterior.data)
                            self.append_node(node_anterior.next)
                            return
                            boolean = True
                        else:
                            print("dentro del else")
                            return
                            boolean = True

                    #node_cabeza = node_cabeza.next
                    #print("Nodo nuevo " + str() + " menor a ")
                    #print(node_cabeza.data)
                #node_cabeza.next = node_nuevo
                self.display()
                return
            else:
                print("Node nuevo " + str(node_nuevo.data) + " es mayor a node anterior " + str(node_anterior.next.data))
                while node_cabeza.next != None:
                    node_cabeza = node_cabeza.next
                node_cabeza.next = node_nuevo



            node_anterior.next = node_cabeza.next # set el ultimo nodo



            '''while node_cabeza.next != None:
                node_cabeza = node_cabeza.next
            node_cabeza.next = node_nuevo
            node_anterior.next = node_cabeza.next'''

    def append_sorted_name(self, nombre): # este metodo

        node_nuevo = Node(nombre, None, None, None)
        node_nuevo.order_by_name(nombre)
        #print(node_nuevo.pointer)
        node_cabeza = self.head
        node_anterior = self.anterior

        if self.is_empty(): # Si la lista esta vacia
            #print("Vacia")
            node_cabeza.next = node_nuevo # Priximo nodo igual a nuevo nodo
            node_anterior.next = node_cabeza.next # Nodo anterior igual primer nodo
        else:
            #print("Nodo anterior "+str(node_anterior.next.pointer))
            #self.display_name()
            if node_nuevo.pointer < node_anterior.next.pointer:
                #print("Node nuevo "+str(node_nuevo.pointer) + " es menor a node anterior " + str(node_anterior.next.pointer))
                boolean = False
                #print("fuera del if")
                #print(node_cabeza.next.pointer)
                if node_nuevo.pointer < node_cabeza.next.pointer:
                    #print("2,3,5")
                    node_anterior = node_cabeza.next
                    node_cabeza.next = node_nuevo
                    self.append_node(node_anterior)
                else:
                    #print("3,4,5")
                    while  node_cabeza.next.pointer < node_nuevo.pointer:
                        node_cabeza = node_cabeza.next
                        #print("dentro while")
                    #print(node_cabeza.next.pointer)
                    while boolean is False and node_nuevo.pointer < node_cabeza.next.pointer: #(node_cabeza.next.data and node_nuevo.data) < node_anterior.next.data: # Mientras nuevo nodo sea menor a nodo anterior
                        #print("antes del if ")
                        if node_nuevo.pointer < node_anterior.next.pointer:
                            #print("dentro del if")
                            node_cabeza.next = node_nuevo
                            #print(node_anterior.next.pointer)
                            self.append_node(node_anterior.next)
                            #self.display_name()
                            return
                            boolean = True
                        else:
                            #print("dentro del else")
                            return
                            boolean = True
                #self.display_name()
                return
            else:
                #print("Node nuevo " + str(node_nuevo.pointer) + " es mayor a node anterior " + str(node_anterior.next.pointer))
                while node_cabeza.next != None:
                    node_cabeza = node_cabeza.next
                node_cabeza.next = node_nuevo

            node_anterior.next = node_cabeza.next # set el ultimo nodo
            #self.display_name()

    def append_sorted_apellido_paterno(self, apellido_paterno): # este metodo
        node_nuevo = Node(None, apellido_paterno)
        node_nuevo.order_by_apellido_paterno(apellido_paterno)
        #print(node_nuevo.pointer2)
        node_cabeza = self.head
        node_anterior = self.anterior

        if self.is_empty(): # Si la lista esta vacia
            #print("Vacia")
            node_cabeza.next = node_nuevo # Priximo nodo igual a nuevo nodo
            node_anterior.next = node_cabeza.next # Nodo anterior igual primer nodo
        else:
            #print("Nodo anterior "+str(node_anterior.next.pointer2))
            #self.display_name()
            if node_nuevo.pointer2 < node_anterior.next.pointer2:
                #print("Node nuevo "+str(node_nuevo.pointer2) + " es menor a node anterior " + str(node_anterior.next.pointer2))
                boolean = False
                #print("fuera del if")
                #print(node_cabeza.next.pointer2)
                if node_nuevo.pointer2 < node_cabeza.next.pointer2:
                    #print("2,3,5")
                    node_anterior = node_cabeza.next
                    node_cabeza.next = node_nuevo
                    self.append_node(node_anterior)
                else:
                    #print("3,4,5")
                    while  node_cabeza.next.pointer2 < node_nuevo.pointer2:
                        node_cabeza = node_cabeza.next
                        #print("dentro while")
                    #print(node_cabeza.next.pointer2)
                    while boolean is False and node_nuevo.pointer2 < node_cabeza.next.pointer2: #(node_cabeza.next.data and node_nuevo.data) < node_anterior.next.data: # Mientras nuevo nodo sea menor a nodo anterior
                        #print("antes del if ")
                        if node_nuevo.pointer2 < node_anterior.next.pointer2:
                            #print("dentro del if")
                            node_cabeza.next = node_nuevo
                            #print(node_anterior.next.pointer2)
                            self.append_node(node_anterior.next)
                            #self.display_apellido_paterno()
                            return
                            boolean = True
                        else:
                            #print("dentro del else")
                            return
                            boolean = True
                #self.display_name()
                return
            else:
                #print("Node nuevo " + str(node_nuevo.pointer2) + " es mayor a node anterior " + str(node_anterior.next.pointer2))
                while node_cabeza.next != None:
                    node_cabeza = node_cabeza.next
                node_cabeza.next = node_nuevo

            node_anterior.next = node_cabeza.next # set el ultimo nodo
            #self.display_apellido_paterno()

    def append_sorted_apelldio_materno(self, apellido_materno): # este metodo
        node_nuevo = Node(None, None, apellido_materno, None)
        node_nuevo.order_by_name(apellido_materno)
        #print(node_nuevo.pointer)
        node_cabeza = self.head
        node_anterior = self.anterior

        if self.is_empty(): # Si la lista esta vacia
            #print("Vacia")
            node_cabeza.next = node_nuevo # Priximo nodo igual a nuevo nodo
            node_anterior.next = node_cabeza.next # Nodo anterior igual primer nodo
        else:
            #print("Nodo anterior "+str(node_anterior.next.pointer))
            #self.display_name()
            if node_nuevo.pointer < node_anterior.next.pointer:
                #print("Node nuevo "+str(node_nuevo.pointer) + " es menor a node anterior " + str(node_anterior.next.pointer))
                boolean = False
                #print("fuera del if")
                #print(node_cabeza.next.pointer)
                if node_nuevo.pointer < node_cabeza.next.pointer:
                    #print("2,3,5")
                    node_anterior = node_cabeza.next
                    node_cabeza.next = node_nuevo
                    self.append_node(node_anterior)
                else:
                    #print("3,4,5")
                    while  node_cabeza.next.pointer < node_nuevo.pointer:
                        node_cabeza = node_cabeza.next
                        #print("dentro while")
                    #print(node_cabeza.next.pointer)
                    while boolean is False and node_nuevo.pointer < node_cabeza.next.pointer: #(node_cabeza.next.data and node_nuevo.data) < node_anterior.next.data: # Mientras nuevo nodo sea menor a nodo anterior
                        #print("antes del if ")
                        if node_nuevo.pointer < node_anterior.next.pointer:
                            #print("dentro del if")
                            node_cabeza.next = node_nuevo
                            #print(node_anterior.next.pointer)
                            self.append_node(node_anterior.next)
                            #self.display_name()
                            return
                            boolean = True
                        else:
                            #print("dentro del else")
                            return
                            boolean = True
                #self.display_name()
                return
            else:
                #print("Node nuevo " + str(node_nuevo.pointer) + " es mayor a node anterior " + str(node_anterior.next.pointer))
                while node_cabeza.next != None:
                    node_cabeza = node_cabeza.next
                node_cabeza.next = node_nuevo

            node_anterior.next = node_cabeza.next # set el ultimo nodo
            #self.display_name()

    def append_nombre_completo(self, nombre,apellido_paterno):
        self.append_sorted_name(nombre)
        self.display_name()
        self.append_sorted_apellido_paterno(apellido_paterno)
        self.display_apellido_paterno()
        '''self.append_sorted_apelldio_materno(apellido_materno)
        self.display_apellido_materno()'''

    def addition(self): # Metodo para sumar nodos
        cur = self.head
        while cur.next != None:
            cur = cur.next
            self.sum += cur.data
        cur.next = cur
        print("La suma de todos los nodos es: "+str(self.sum))

    def cont_impar(self): # Metodo iterativo para contar los nodos impares
        cur = self.head
        while cur.data is not None and cur.next % 2 != 0:
            cur = cur.next
            self.cont_imp += 1
        cur.next = cur
        print("Hay "+str(self.cont_imp)+" numeros impares")

    def delete(self, data): # Metodo para borrar un nodo especifico
        cur_node = self.head
        while cur_node.data != data:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                last_node.next = cur_node.next
                return

    def length(self): # Medodo para regresar la longitud de la lista
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def is_empty(self): # Metodo para
        cur = self.head
        if cur.next == None:
            return True
        else:
            return False

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def display_name(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.nombre)
        print("Insertados por Nombre")
        print(elems)

    def display_apellido_paterno(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.apellido_paterno)
        print("Insertados por apellido Paterno")
        print(elems)

    def display_apellido_materno(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.apellido_materno)
        print("Insertados por apellido Materno")
        print(elems)

    def display2(self):

        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node.data)


    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None

        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return

        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list_nombre = List()
my_list_apellido_paterno = List()
my_list_apellido_materno = List()
#my_list.append_sorted_name()

'''my_list_nombre.append_sorted_name("Carlos")
my_list_apellido_paterno.append_sorted_apellido_paterno("Daasd")
my_list_apellido_materno.append_sorted_apelldio_materno("Lagsgds")

my_list_nombre.append_sorted_name("Elisa")
my_list_apellido_paterno.append_sorted_apellido_paterno("Paasd")
my_list_apellido_materno.append_sorted_apelldio_materno("Magsr")

my_list_nombre.append_sorted_name("Ana")
my_list_apellido_paterno.append_sorted_apellido_paterno("Harsgt")
my_list_apellido_materno.append_sorted_apelldio_materno("Saavs")

my_list_nombre.append_sorted_name("Daniel")
my_list_apellido_paterno.append_sorted_apellido_paterno("JibSS")
my_list_apellido_materno.append_sorted_apelldio_materno("Kiwer")

my_list_nombre.display_name()
my_list_apellido_paterno.display_apellido_paterno()
my_list_apellido_materno.display_apellido_materno()'''


def main():
    print("Bienvenido\n1) Insertar Nombre\n2)Mostrar nodos\n3)Salir")

    option = input("Seleccione una opcion: ")

    if option == "1":
        tem = input("Nombre(s): ")
        my_list_nombre.append_sorted_name(tem)
        tem = input("Apellido Paterno: ")
        my_list_apellido_paterno.append_sorted_apellido_paterno(tem)
        tem = input("Apellido Materno: ")
        my_list_apellido_materno.append_sorted_apelldio_materno(tem)
        main()
    elif option == "2":
        my_list_nombre.display_name()
        my_list_apellido_paterno.display_apellido_paterno()
        my_list_apellido_materno.display_apellido_materno()
        main()
    elif option == "3":
        exit()
    elif option == "4":

        main()
    elif option == "5":

        main()
    elif option == "6":
        exit()
    else:
        main()
main()