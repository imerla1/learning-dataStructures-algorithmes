class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value=None) -> None:
        initial_node = Node(value)
        self.head = initial_node
        self.tail = initial_node
        if value is None:
            self.length = 0
        else:
            self.length = 1

    def __repr__(self) -> str:
        ret = ""
        temp = self.head
        while temp is not None:
            ret += str(temp.value) + "/n"
            temp = temp.next

    def append(self, value):
        # append new node at the end of the DLL
        if self.head.value is None:
            ...
            

if __name__ == "__main__":
    x = DoublyLinkedList(5)
    