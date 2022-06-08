class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __repr__(self) -> str:
        ret = ""
        temp = self.head
        while temp is not None:
            ret += str(temp.value) + "/n"
            temp = temp.next


if __name__ == "__main__":
    x = DoublyLinkedList(5)
    