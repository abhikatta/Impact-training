import sys
sys.path.append('./')
sys.path.append('../')


def BSTt():
    from BST import BST, Node
    return BST(), Node


Binary_search_Tree, root_node = BSTt()

Binary_search_Tree.root = root_node(data=10)
Binary_search_Tree.insert(value=1, root=Binary_search_Tree.root)
Binary_search_Tree.insert(value=12, root=Binary_search_Tree.root)
Binary_search_Tree.insert(value=123, root=Binary_search_Tree.root)
Binary_search_Tree.insert(value=1234, root=Binary_search_Tree.root)
Binary_search_Tree.insert(value=12345, root=Binary_search_Tree.root)
Binary_search_Tree.insert(value=123456, root=Binary_search_Tree.root)
Binary_search_Tree.traverse(root=Binary_search_Tree.root)
print()
el = Binary_search_Tree.search(
    value=1234, root=Binary_search_Tree.root, return_value=True)
print((el.next).data)
