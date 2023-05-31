from DLinkedList import Node as N

# TODO:
# 0. x Insertion
# 1. x Deletion
# 2. x Search
# 3. x Height
# 4.   Diameter
# 5. x find_parent
# 6.   DFS


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
        '''Research going on. To be implemented. Deletes the given value from the Binary Search Tree.'''
        # 3 cases:
        # 1. no child nodes / value to be deleted is a leaf node
        # 2. one child node left or right
        # 3. 2 child nodes: replace with inorder successor
        if root is None:
            return None

        elif value < root.data:
            root.prev = self.deletion(root=root.prev, value=value)
        elif value > root.data:
            root.next = self.deletion(root=root.next, value=value)

        else:

            # case 1
            if root.next is None and root.prev is None:
                root = None

            # case 2
            elif root.prev is None:
                root = root.next
            elif root.next is None:
                root = root.prev

            # case 3
            else:
                # either take max value in left sub tree or min value in right sub tree and replace
                # that value with current node's value(not node, but VALUE).
                # here  max value  of the 2 successors is being taken.
                # again that successor may also have successsor(s), so the deletion function is being applied again on the successor.
                successor = self.inorder_successor(root=root.prev)
                root.data = successor.data
                self.deletion(root=root.prev, value=root.prev)

        # 4. left max has a child
        return root

    def traverse(self, root: Node) -> None:
        '''Traverses and prints the Binary Search Tree.'''
        if root is not None:
            self.traverse(root=root.prev)
            print(root.data, end=', ')
            self.traverse(root=root.next)

    def inorder_predecessor(self, root: Node) -> Node:
        while root.prev:
            root = root.prev
        print(root.data)
        return root

    def inorder_successor(self, root: Node) -> Node:
        while root.next:
            root = root.next
        print(root.data)
        return root
    
    def find_parent(self, root: Node, leaf_value: int) -> Node:
        '''Finds the parent of the leaf. Returns None if not found.'''
        # since root node does not have a parent
        # track current node, parent node, if current.data=value return parent node
        parent = None
        current = root
        while current is not None:
            if current.data == leaf_value:
                print(parent.data)
                return parent
            parent = current
            if current.data < leaf_value:
                current = current.next
            else:
                current = current.prev
        return None

    def search(self, value: int, root: Node, return_node=False) -> int:
        '''Traverses the Binary Search tree and returns True if the value is found else returns None.
            - If return_value is given as True, the value, if found the value will be returned.
            - return_value = False by default.
        '''
        count = 0
        while root:
            count += 1
            if value < root.data:
                # return self.search(root=root.prev, value=value,) with these, the default parameter cannot be passed
                root = root.prev
            elif value > root.data:
                # return self.search(root=root.next, value=value) with these, the default parameter cannot be passed
                root = root.next
            elif value == root.data:
                if return_node:
                    return root
                else:
                    return True
            return False

    def height(self, root: Node) -> int:
        '''Calculates and returns the height of the Binary Search Tree from the root.
            - Height is basically the length of the longest path from the root node to leaf node.
        '''
        if not root:
            return 0
        elif root:
            H = 1+max(self.height(root=root.prev), self.height(root=root.next))
            return H

# TODO:
    def diameter(self, root: Node) -> int:
        '''
        - To Be implmented.
        - Calculates and returns the height of the Binary Search Tree from the root. 
        - Diameter is something I still don't know, still researching.
        '''
        pass


asd = BST()
asd.root = Node(10)
asd.insert(value=12, root=asd.root)
asd.insert(value=13, root=asd.root)
asd.insert(value=9, root=asd.root)
asd.insert(value=8, root=asd.root)
asd.insert(value=14, root=asd.root)
asd.traverse(root=asd.root)
print()
asd.deletion(value=9, root=asd.root)
# asd.findparent(root=asd.root, leaf_value=9)
asd.traverse(root=asd.root)
