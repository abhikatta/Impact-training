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
            11: 'Traverse',
            12: 'Middle Element'
            
        }
        self.commands = [
            lambda:self.ll.insert_at_end(
                data=input("Enter the value to be added: ")),
            lambda:self.ll.insert_at_beginning(
                data=input("Enter value to be added: ")),
            lambda:self.ll.insert_at(value=input(
                "Enter value to be inserted: "), index=input("Enter index value: ")),
            lambda:self.ll.insert_value_after(value_to_be_inserted=input("Enter value to be inserted: "), value=input(
                f"Enter the value after which new value is to be inserted: ")),
            lambda:self.ll.delete_last(),
            lambda:self.ll.delete_first(),
            lambda:self.ll.delete_at(index=input("Enter the index: ")),
            lambda:self.ll.delete_value(
                value=input("Enter value to be deleted: ")),
            lambda:self.ll.reversal(),
            lambda:self.ll.search(value=input("Enter value to be searched: ")),
            lambda:self.ll.traverse(),
            lambda:self.ll.middle_element()
        ]

    def take_input(self):

        while True:
            try:
                print(self.operations, end='\n')
                i = int(input("\nEnter your operation: "))
                if i in self.operations.keys():
                    self.commands[i-1]()
                elif i == 0:
                    break
                else:
                    print("Select an option from below:")
            except ValueError:
                print("Select an option from below:")
                print(self.operations)
            except KeyboardInterrupt:
                break


test = Tests()
test.take_input()
