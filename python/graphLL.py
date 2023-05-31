from Linkedlist import Node

class Graph:
    def __init__(self,no_of_vertices) -> None:
        self.no_of_vertices=no_of_vertices
        self.graph=[None]*no_of_vertices
        
    def add_node(self,s,d):
        node=Node(d)
        self.graph[s]=node
        node.next=self.graph