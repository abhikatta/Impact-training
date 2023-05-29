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

    def insert_at(self, value: int, index: int):
        current = self.head
        count = 0
        prev = None
        node = Node(value)
        if current is None:
            current = node
            return
        while current is not None:

            if count == index:
                prev.next = node
                node.next = current
                return
            elif count != index:
                count += 1
                prev = current
                current = current.next
            elif count > index:
                print("Index out of range!")
                return False
        self.head = current
        return

    def delete_at_end(self):
        current = self.head
        prev = None
        while current is not None:
            if current.next == self.head:
                prev.next = self.head
                return
            elif current.next != self.head:
                prev = current
                current = current.next

    def delete_at_beginning(self):
        current = self.head
        while current is not None:
            if current.next == self.head:
                current.next = self.head.next
                self.head = current.next
                return
            current = current.next

    def delete_at(self, index: int):
        current = self.head
        count = 0
        prev = None
        while current is not None:
            if count == index:
                prev.next = current.next
                return
            else:
                count += 1
                prev = current
                current = current.next
        return
