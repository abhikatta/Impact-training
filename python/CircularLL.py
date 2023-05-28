class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = self

# TODO:
# 1. Delete at index
# 2. Search
# 3. Insert at index
# 4. Reverse


class CircularLL():
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data: int) -> None:
        node = Node(data=data)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            while current.next is not self.head:
                current = current.next
            current.next = node
            node.next = self.head

    def insert_at_beginning(self, data: int) -> None:
        node = Node(data=data)
        first = self.head
        current = first
        if self.head is None:
            self.head = node
        else:
            while current.next is not self.head:
                current = current.next
                if current.next is self.head:
                    last = current
                    break
            self.head = node
            current = first
            node.next = first
            last.next = node
        return

    def traverse(self) -> None:
        current = self.head
        while current is not None:
            print(current.data, end=', ')
            current = current.next
            if current == self.head:
                break
        return

    # def insert_at(self, value: int, index: int) -> None:
    #     return super().insert_at(value, index)


cll = CircularLL()
cll.insert_at_end(10)
cll.insert_at_end(12)
cll.insert_at_end(13)
cll.insert_at_end(14)
cll.insert_at_end(5)
cll.insert_at_beginning(16)
cll.traverse()
