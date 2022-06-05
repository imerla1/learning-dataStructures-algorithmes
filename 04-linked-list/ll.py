class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value) # Initial node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        "create new node add node to the end"
        ll_node = Node(value) # create new node
        # check if ll is empty
        if self.head.value == None:
            # ll doesn't have any node
            # so head and tail are both empty 
            self.head = ll_node
            self.tail = ll_node
            self.length = 1
        else:
            # LinkedList isn't empty so we need to append new_node at the end of the ll
            prev_node = self.tail
            prev_node.next = ll_node
            self.tail = ll_node
            self.length += 1
    def prepend(self, value):
        # create new node
        # add node to the beginning
        ...
    def insert(self, index, value):
        # create new node
        # insert node to specific place based on index
        ...

if __name__ == "__main__":
    my_ll = LinkedList(None)
    my_ll.append(25)
    my_ll.append(76)
    my_ll.append(26)
    my_ll.append(68)

    my_ll.print_list()