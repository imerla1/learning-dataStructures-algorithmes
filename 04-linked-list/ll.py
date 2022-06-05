class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)  # Initial node
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
        ll_node = Node(value)  # create new node
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

    def pop(self):
        "remove last item from ll and return it"
        if self.head is None:
            # we don't have any item in ll
            return False
        if self.length == 1:
            # we have only 1 node (head=tail) we can pop it and return
            return_value = self.head.value
            self.head.value = None
            self.head.next = None
            return return_value
        else:
            # we have more than 1 Node

            prev = self.head
            temp = self.head
            while temp.next != None:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1
            return temp

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
    x = my_ll.pop()
    # my_ll.print_list()
