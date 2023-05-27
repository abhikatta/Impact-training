from DLinkedList import Node as N


class Node(N):
    def __init__(self, data: int) -> None:
        super().__init__(data)


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value, root) -> Node:
        if root is None:
            return Node(value)
        if value > root.data:
            root.next = self.insert(value=value, root=root.next)
        elif value < root.data:
            root.prev = self.insert(value=value, root=root.prev)
        return root

    def traverse(self, root):
        if root is not None:
            self.traverse(root=root.prev)
            print(root.data, end=', ')
            self.traverse(root=root.next)

    def search(self, value, root):
        count = 0
        while root is not None:
            count += 1
            if value < root.data:
                return self.search(root=root.prev, value=value)
            elif value > root.data:
                return self.search(root=root.next, value=value)
            elif value == root.data:
                return True
        return
    # def


bstree = BST()

# Tree should be made as:
# 1. A root should be created, which can be done in 2 ways:
# -  a. bstree.root = Node(14)
# -  b. bstree.root = bstree.insert(value=14, root=None)
# 2. Pass the nodes as bstree.insert(value=some_value, root=bstree.root)


bstree.root = Node(14)
bstree.insert(value=15, root=bstree.root)
bstree.insert(value=13, root=bstree.root)
bstree.insert(value=12, root=bstree.root)
bstree.insert(value=11, root=bstree.root)
bstree.insert(value=10, root=bstree.root)
bstree.traverse(root=bstree.root)
print()
print(bstree.search(root=bstree.root, value=13))
