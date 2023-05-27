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
            print(root.data)
            self.traverse(root=root.next)


bstree = BST()
bstree.root = bstree.insert(value=1, root=None)
bstree.insert(value=10, root=bstree.root)
bstree.insert(value=11, root=bstree.root)
bstree.insert(value=12, root=bstree.root)
bstree.insert(value=13, root=bstree.root)
bstree.insert(value=14, root=bstree.root)
bstree.traverse(root=bstree.root)
