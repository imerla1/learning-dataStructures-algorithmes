import time

from rich.live import Live
from rich.table import Table


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

    def __len__(self):
        return self.length

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

    def prepend(self, value):
        # create new node
        # add node to the beginning
        new_node = Node(value)
        if self.length == 0:
            # our DLL is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def display_nodes(self):
        # pretty represent all nodes
        table = Table()
        table.add_column("Node ID")
        table.add_column("Prev Node Value")
        table.add_column("Value")
        table.add_column("Next Node Value")

        nodes = []
        temp = self.head
        while temp is not None:
            print(temp.value)
            nodes.append(temp)
            temp = temp.next

        with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
            for node_id, node in enumerate(nodes):
                try:
                    node_prev_value = node.prev.value
                except AttributeError:
                     node_prev_value = None
                try:
                    node_value = node.value
                except AttributeError:
                     node_value = None
                try:
                    node_next_value = node.next.value
                except AttributeError:
                     node_next_value = None
                table.add_row(
                    f"{node_id}", str(node_prev_value), str(node_value), str(node_next_value)
                )
                time.sleep(0.2)


if __name__ == "__main__":
    x = DoublyLinkedList(5)
    x.append(25)
    x.append(25)
    x.append(25)
    x.append(25)

    a = x.display_nodes()
