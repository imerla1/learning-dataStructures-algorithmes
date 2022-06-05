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
        # create new node
        # add node to end
        ...
    def prepend(self, value):
        # create new node
        # add node to the beginning
        ...
    def insert(self, index, value):
        # create new node
        # insert node to specific place based on index
        ...

if __name__ == "__main__":
    my_ll = LinkedList(4)
