class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #Address of next node

class SingleLinkedList:
    def __init__(self):
        self.head = None #this is the default as there are no elements/nodes

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head #this has to travel from the 1st element to the last variable
            while temp:
                print(temp.data, "-->", end = " ")
                temp = temp.next

L = SingleLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
L.head.next = n1
n2 = Node(30)
n1.next = n2
L.display()

