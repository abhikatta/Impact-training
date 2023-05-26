from Linkedlist import Node, LinkedList


class Node(Node):
    def __init__(self, data) -> None:
        self.data = data
        self.next = self


class CircularLL(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def insert_at_end(self, data: int) -> None:
        node = Node(data=data)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            while current is not self.head:
                current = current.next
            current.next = node
            node.next = self.head

    def traverse(self) -> None:
        current = self.head
        while current is not None:
            print(current.data, end=', ')
            current = current.next
            if current == self.head:
                break
        return


cll = CircularLL()
cll.insert_at_end(10)
cll.insert_at_end(12)
cll.insert_at_end(13)
cll.traverse()
