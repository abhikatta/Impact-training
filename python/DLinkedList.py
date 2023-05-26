class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.prev = None
        self.next = None

# TODO:
# 1. Insert after value
# 2. insert at index
# 3. Delete at index


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

    # def insert_after_value(self,new_value:int,value:int)->None:
    #     '''
    #     Insert given value(new_value) after given data(value).
    #     '''
    #     current=self.head
    #     count=0
    #     while current is not None:
    #         if

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


dll = DLL()
dll.insert_at_end(100)
dll.insert_at_end(200)
dll.insert_at_end(300)
dll.insert_at_end(400)
dll.insert_at_end(500)
dll.traverse()
# dll.insert_at_beginning(400)
# dll.traverse()
print()
dll.delete_at_end()
dll.traverse()
print()
dll.delete_at_beginning()
dll.traverse()
print()
dll.delete_value(200)
dll.traverse()
