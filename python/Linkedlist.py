class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
# TODO:
# 1. x Finding Middle element in O(logn) using 2 pointers
# 2. x Loop detection (last to any except head)
        # a. if s=f at some point, there is a loop
# 3.   Aggressive cows (Binary Search)
# 4.   Trapping rain Water(left and right)
# 5.   Graph coloring prob
# 6.   N-Queens prob

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data: int) -> None:
        '''
        Insert an element at the end.
        '''
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data: int) -> None:
        '''
        Insert an element at the beginning of the Linked list
        '''
        print("data: ")
        print(data)
        print()
        current = self.head
        new_node = Node(data=data)
        self.head = new_node
        new_node.next = current

    def insert_at(self, value: int, index: int) -> None:
        '''
        Insert a value (element/node) at the index of the LinkedList.
        '''
        current = self.head
        count = 0
        new_node = Node(value)
        prev = None
        print()
        print(index)
        print()
        
        if index == 0:
            self.insert_at_beginning(data=value)
            return
        while current is not None:
            if count != index:
                prev = current
                current = current.next
                count += 1
            elif count == index and current.next is not None:
                prev.next = new_node
                new_node.next = current
                return
            elif count == index and current.next is None:
                self.insert_at_end(data=value)
                return

    def insert_value_after(self, value_to_be_inserted: int, value: int) -> int:
        '''Insert a value after a specified value.'''
        current = self.head
        node = Node(value_to_be_inserted)
        while current is not None:
            if current.data != value:
                current = current.next
            elif current.data == value:
                temp = current.next
                current.next = node
                node.next = temp
                break
            else:
                print(
                    "Check the value of the linked list, looks like it's not present in the Linked List")

    def traverse(self) -> None:
        '''
        Print all the elements in the LinkedList.
        '''
        print("Linked List:")
        current = self.head
        while current is not None:
            print(current.data, end=', ')
            current = current.next
        print()
        return

    def delete_last(self) -> None:
        '''
        Delete the last element of the Linked List.
        '''
        current = self.head
        while current.next is not None:
            temp = current
            current = current.next
            if current.next is None:
                temp.next = None
    def loop_detection(self):
        '''Detects if a loop is present in the Linked List.'''
        current=self.head
        H=current
        T=current
        while H!=T:
            if H !=T:
                H=(H.next).next
                T=T.next
            elif H==T:
                return True
            elif T.next==None:
                return False
        
        
        
    def delete_first(self) -> None:
        '''
        Delete the first element of the Linked List.
        '''
        current = self.head
        self.head = current.next

    def delete_value(self, value: int) -> None:
        '''
        Delete a given value from the Linked List.
        '''
        current = self.head
        prev = None
        while current is not None:
            if current.data == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
            prev = current
            current = current.next

    def delete_at(self, index: int) -> None:
        '''
        Deletes a value at the specified index.
        '''
        current = self.head
        prev = None
        count = 0
        if index == 0:
            self.delete_first()
        while current is not None:
            if count != index:
                count += 1
                prev = current
                current = current.next
            elif count == index:
                prev.next = current.next
                current = current.next
                break

    def middle_element(self):
        current=self.head
        H=current
        T=current
        while H is not None:
            if H.next is None:
                print(T.data)
                return T
            elif (H.next).next is None:
                print(T.data)
                return T
            if H is not None and H.next is not None:
                T=T.next
                H=(H.next).next
                

    def search(self, value: int) -> bool:
        '''
        Searches the value in the Linked List, if found returns True and prints index of the value, else returns False.
        '''
        print(f"Searching for {value}:")
        current = self.head
        count = 0
        if current.data == value:
            print(0)
            return True
        while current is not None:
            if current.data == value:
                print(count)
                return True
            elif current.data != value:
                count += 1
                current = current.next
        print(False)

    def reversal(self) -> None:
        '''
        Reverses a Linked List and also prints it 
        self
        '''
        print("Reversing a Linked List")
        current = self.head
        prev = None

        while current is not None:
            last = current.next
            current.next = prev
            prev = current
            current = last

        # since while printing we will print starting from the self.head(first element), last element will be the first element

        self.head = prev
        self.traverse()
        
        
ll=LinkedList()
ll.insert_at(value=1,index=0)
ll.insert_at(value=2,index=1)
ll.insert_at(value=3,index=2)
ll.traverse()