import sys
sys.path.append('./')
sys.path.append('../')


class Tests:
    def __init__(self) -> None:
        from Linkedlist import LinkedList
        self.ll = LinkedList()
        self.operations = {
            1: 'Insert_at_end',
            2: 'Insert_at_beginning',
            3: 'Insert_at_index',
            4: 'Insert_after_value',
            5: 'Delete_last',
            6: 'Delete_first',
            7: 'Delete_at_index',
            8: 'Delete_value',
            9: 'Reverse_Linked_List',
            10: 'Search',
            11: 'Traverse'
        }

    def take_input(self):
        print(self.operations, end='\n')
        while True:
            try:
                i = int(input("\nEnter your operation: "))
                if i in self.operations.keys():
                    if i == 1:
                        self.ll.insert_at_end(data=input(
                            "Enter the value to be added: "))
                    elif i == 2:
                        self.ll.insert_at_beginning(
                            data=input("Enter value to be added: "))
                    elif i == 3:
                        a = input("Enter value to be inserted: ")
                        b = input("Enter index value: ")
                        self.ll.insert_at(value=a, index=b)
                    elif i == 4:
                        a = input("Enter value to be inserted: ")
                        b = input(
                            f"Enter the value after which {a} is to be inserted: ")
                        self.ll.insert_value_after(
                            value_to_be_inserted=a, value=b)
                    elif i == 5:
                        self.ll.delete_last()
                    elif i == 6:
                        self.ll.delete_first()
                    elif i == 7:
                        self.ll.delete_at(index=input("Enter the index: "))
                    elif i == 8:
                        self.ll.delete_value(value=input(
                            "Enter value to be deleted: "))
                    elif i == 9:
                        self.ll.reversal()
                    elif i == 10:
                        self.ll.search(value=input(
                            "Enter value to be searched"))
                    elif i == 11:
                        self.ll.traverse()
                    elif i == 0:
                        break
                else:
                    print("Select an option from below:")
                    print(self.operations)
            except ValueError:
                print("Select an option from below:")
                print(self.operations)
            except KeyboardInterrupt:
                break


test = Tests()
test.take_input()
