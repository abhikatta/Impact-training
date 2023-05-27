from DLinkedList import Node as N

# TODO:
# 0. Insertion x
# 1. Deletion
# 2. Search
# 3. Height
# 4. Diameter


class Node(N):
    def __init__(self, data: int) -> None:
        super().__init__(data)


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int, root: Node) -> Node:
        '''
        Insert an element into the Binary search tree.
        Root node of the Binary search tree can be created in 2 ways:

        - BST_class_obj.root_name = Node(value)
        - BST_class_obj.root_name = bstree.insert(value, root=None)

        Other leaf nodes should be inserted as:
        - bstree.insert(value, root=BST_class_obj.root_name)

        '''
        if root is None:
            return Node(value)
        if value > root.data:
            root.next = self.insert(value=value, root=root.next)
        elif value < root.data:
            root.prev = self.insert(value=value, root=root.prev)
        return root

    def deletion(self, root: Node, value: int) -> None:
        '''Deletes the given value from the Binary Search Tree.'''
        pass

    def traverse(self, root: Node) -> None:
        '''Traverses and prints the Binary Search Tree.'''
        if root is not None:
            self.traverse(root=root.prev)
            print(root.data, end=', ')
            self.traverse(root=root.next)

    def search(self, value: int, root: Node, return_value=False) -> int:
        '''Traverses the Binary Search tree and returns True if the value is found else returns None.
            - If return_value is given as True, the value, if found the value will be returned.
            - return_value = False by default.
        '''
        count = 0
        while root is not None:
            count += 1
            if value < root.data:
                # return self.search(root=root.prev, value=value,) with these, the default parameter cannot be passed
                root = root.prev
            elif value > root.data:
                # return self.search(root=root.next, value=value) with these, the default parameter cannot be passed
                root = root.next
            elif value == root.data:
                if return_value:
                    return root.data
                else:
                    return True
        return False

    def height(self, root: Node) -> int:
        '''Calculates and returns the height of the Binary Search Tree from the root.
            - Height is basically the length of the longest path from the root node to leaf node.
        '''
        pass

    def diameter():
        pass


bstree = BST()

# Tree should be made as:
# 1. A root should be created, which can be done in 2 ways:
# -  a. bstree.root = Node(14) (the better way IMO)
# -  b. bstree.root = bstree.insert(value=14, root=None)
# 2. Pass the nodes as bstree.insert(value=some_value, root=bstree.root)

# bstree.my_function()
bstree.root = Node(14)
bstree.insert(value=-15, root=bstree.root)
bstree.insert(value=-13, root=bstree.root)
bstree.insert(value=12, root=bstree.root)
bstree.insert(value=11, root=bstree.root)
bstree.insert(value=-10, root=bstree.root)
bstree.traverse(root=bstree.root)
print()
# bstree.height()
print(bstree.search(root=bstree.root, value=-13, return_value=True))
