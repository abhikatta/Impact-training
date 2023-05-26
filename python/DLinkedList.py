class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.prev = None
        self.next = None

# TODO:
# 1.x Insert after value
# 2.x insert at index
# 3.x Delete at index
# 4.x Test file


class DLL:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data: int) -> None:
        '''
        Insert an node with data at the end of the Doubly Linked List.
        '''

        node = Node(data=data)
        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next is not None:

                current = current.next
            current.next = node
            node.prev = current

    def insert_at_beginning(self, value: int) -> None:
        '''
        Insert an element at the beginning of the Doubly Linked List.
        '''
        current = self.head
        node = Node(value)
        self.head = node
        node.next = current

    def insert_after_value(self, new_value: int, value: int) -> None:
        '''
        Insert given value(new_value) after given data(value).
        '''
        current = self.head
        node = Node(new_value)
        while current is not None:
            if current.data is value:
                node.next = current.next
                current.next = node
                node.prev = current
                break
            current = current.next

    def insert_at(self, index: int, value: int) -> None:
        '''
        Insert a Node element at the given index of the Doubly Linked List.
        '''
        current = self.head
        count = 0
        node = Node(value)
        prev = None
        if index == 0:
            self.insert_at_beginning(value=value)
            return
        while current is not None:
            if count != index:
                count += 1
                prev = current
                current = current.next
            elif count == index:
                node.next = current
                node.prev = prev
                prev.next = node
                current.prev = node
                return

        print('Index is more than list size')

    def delete_at_end(self) -> None:
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None

    def delete_at_beginning(self) -> None:
        '''
        Delete at beginning from Doubly Linked List.
        '''
        current = self.head
        self.head = current.next

    def delete_value(self, value: int) -> None:
        '''
        Delete value from Doubly Linked List.
        '''
        current = self.head
        prev = None
        if value == self.head.data:
            self.head = current.next
        while current is not None:
            if current.data == value:
                if prev is None:
                    prev = current
                prev.next = current.next
                current.next.prev = prev
                return
            prev = current
            current = current.next

    def delete_at_index(self, index: int) -> None:
        '''
        Deletes a node element from the Doubly Linked list at given index.
        '''
        if index == 0:
            self.delete_at_beginning()
            return
        current = self.head
        count = 0
        prev = None
        while current is not None:
            if count != index:
                count += 1
                prev = current
                current = current.next
            elif count == index:
                prev.next = current.next
                current.next.prev = prev
                return

    def traverse(self) -> None:
        '''
        Print out all the nodes in the Doubly Linked List.
        '''
        current = self.head
        prev = None
        while current is not None:
            print(current.data)
            current.prev = prev
            current = current.next
        return

    def search(self, value: int) -> bool:
        current = self.head
        count = 0
        while current is not None:
            if current.data != value:
                count += 1
                current = current.next
            elif current.data == value:
                print(count)
                return True
        print(False)
        return
