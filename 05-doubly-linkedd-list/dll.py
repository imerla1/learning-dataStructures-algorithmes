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
            ret += f"{str(temp.value)}\n"
            temp = temp.next
        return ret
    def append(self, value):
        # append new node at the end of the DLL
        new_node = Node(value)
        if self.head.value is None:
            # we don't have any item in dll so
            # our new node will become head and tail 
            self.head = new_node
            self.tail = new_node
        else:
           prev = self.tail
           prev.next = new_node
           self.tail = new_node
           self.tail.prev = prev 
        self.length += 1

    def pop(self):
        # remove last element and return it.
        if self.length == 0:
            # our DLL is empty
            return False
        elif self.length == 1:
            # we have only 1 item in DLL 
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return temp
        else:
            # we have more than 1 node in DLL
            ret_value = self.tail
            self.tail = ret_value.prev
            self.tail.next = None
            self.length -= 1

            return ret_value
if __name__ == "__main__":
    x = DoublyLinkedList(5)
    x.append(25)
    x.append(53)