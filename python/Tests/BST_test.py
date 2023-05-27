import sys
sys.path.append('./')
sys.path.append('../')


class binary_search_tree_test:
    def __init__(self) -> None:
        '''Imports necessary modules required for current unit tests.'''
        from BST import BST, Node
        self.bst = BST()
        # self.root-Node()
        self.opertions = {
            1: 'Create Root Node',
            2: 'Insert Leaf Node',
            3: 'Height of Tree',
            4: 'Traverse Tree',
            5: 'Search Node',
            6: 'Delete Node',
            7: 'Diameter of Tree'
        }
        self.commands = [
            lambda:self.bst.insert(value=input(
                "Enter root node value to be inserted:"), root=None),
            lambda:self.bst.insert(value=input(
                "Enter node value to be inserted"), root=r)

        ]
