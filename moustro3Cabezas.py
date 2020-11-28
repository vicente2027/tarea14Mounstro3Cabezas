
class Node:
    def __init__(self, nombre=None,apellido_paterno=None,apellido_materno=None,data=None, pointer = None):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.data = data
        self.next = None
        self.next_next = None
        self.pointer = pointer

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



class List:
    def __init__(self):
        self.head = Node()
        self.cont = 0
        self.cont_imp = 0
        self.sum = 0
        self.elem = None

    def get_head(self):
        return self.head

    def append(self, data): # Metodo para insertar nodo
        self.cont += 1
        if data % 2 != 0:
            self.cont_imp += 1
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append_test(self, nombre): # Metodo para insertar nodo
        new_node = Node(nombre)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append_sorted(self, data): # este metodo
        new_node = Node(None, None, None, data)
        cur = Node()

        if self.is_empty(): # Si la lista esta vacia
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

        else: # Si no esta vacia
            #print("1")
            cur = self.head
            sig = Node()
            while (cur.next != None) and cur.next.data < new_node.data: # Cuando el nuevo numero es mayor al numero anterior,
                #print("2")
                #sig = cur # anterior
                cur = cur.next # next
                #print(cur.data)
                sig = cur
                while cur.next != None:
                    cur = cur.next  # next
                    sig = cur

                print("Ultimo dato "+str(sig.data))

            print("3")
            print("Ultimo dato dato " + str(sig.data))
            print(cur.data)
            #print("dato anterior "+str(sig.data))\
            if new_node.data < cur.data:
                print("Nuevo nodo es menor")
                cur = new_node
                print(cur.data)
                print(cur.next)
                '''if cur.next is None:
                    print("a")

                    cur.next = sig'''

            else:
                print("Nuevo nodo es mayor")
                cur.next = new_node

            #cur.next = new_node                                        # inserta el nuevo numero en la siguiente posision.
            #print("Dato nuevo "+ str(cur.next.data))

            #if new_node.data < cur.next.data:
                #cur.next.next = new_node
            #self.head.next = prev



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


my_list = List()
#my_list.append(1)
#my_list.append(4)
#my_list.append(6)
#my_list.append(7)
#my_list.append_test("Vicente")
#my_list.head.order_by_name("Vicente")

my_list.append_sorted(1)
my_list.append_sorted(9)
my_list.append_sorted(16)
my_list.append_sorted(11)

my_list.display()

#my_list.append_sorted()


#my_list.append_sorted(1)
#my_list.display()



