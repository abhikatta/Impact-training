import sys
sys.path.append('./')
sys.path.append('../')


class binary_search_tree_test:
    def rooter(self, Node):
        return Node(input("Enter the root value: "))

    def __init__(self) -> None:
        '''Imports necessary modules required for current unit tests.'''
        from BST import BST, Node
        self.bst = BST()
        self.opertions = {
            0: 'Exit',
            1: 'Insert Leaf Node',
            2: 'Height of Tree',
            3: 'Traverse Tree',
            4: 'Search Node',
            5: 'Delete Node',
            6: 'Diameter of Tree',
            7: 'Change root node'
        }
        self.root = self.rooter(Node)
        self.commands = [
            lambda:exit(),
            lambda: self.bst.insert(value=input(
                "Enter node value to be inserted: "), root=self.root),
            lambda: print(self.bst.height(root=self.root)),
            lambda:self.bst.traverse(root=self.root),
            lambda: print(self.bst.search(
                value=input("Enter the value to be searched: "),
                root=self.root, return_nod=bool(input("Enter if you want to return the value or not: "))).data),
            lambda: self.bst.deletion(root=self.root, value=input(
                "Enter the value you want to delete: ")),
            lambda: self.bst.diameter(root=self.root)
        ]

    def take_input(self):
        while True:
            try:
                print()
                print(self.opertions)
                print()
                i = int(input("Enter your operation: "))
                if i in self.opertions.keys():
                    self.commands[i]()
                elif i == 0:
                    break
                else:
                    print("Please enter an operation from below: ")
            except KeyboardInterrupt:
                break
            except ValueError:
                print("Please enter an operation from below: ")


test = binary_search_tree_test()
test.take_input()
