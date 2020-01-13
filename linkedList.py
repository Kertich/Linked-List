# Node class
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.start = None 

    # Inserting in the Linked List
    def insert(self, value):
        if self.start == None:
            self.start = Node(value)

        current = self.start

        while current.next is not None:
            current = current.next

        current.next = Node(value)

    # Traversing Linked List
    def print(self):
        current = self.start

        while current is not None:
            print(current.value)
            current = current.next

linkedlist = LinkedList()
linkedlist.insert(10)
linkedlist.insert(20)
linkedlist.insert(30)
linkedlist.insert(40)
linkedlist.insert(50)

