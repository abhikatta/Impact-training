# 1. null matrix
# 2. append(add EDGE)
# 3. delete
# 4. size(traverse)


class Graph:
    def __init__(self, size: int) -> list:
        self.size = size
        self.matrix = [[0 for i in (range(size))] for i in (range(size))]

    def add_edge(self, node1: int, node2: int) -> None:
        self.matrix[node1][node2] = 1
        self.matrix[node2][node1] = 1

    def remove_node(self, node1: int, node2: int):
        if self.matrix[node1][node2]:
            self.matrix[node1][node2] = self.matrix[node2][node1] = 0

    def traverse(self):
        rows = [i for i in range(self.size)]
        print(rows)
        print()
        for i in range(1, len(self.matrix)):
            print(str(i)+':')
            print(self.matrix[i], end='\n')
    
    def DFS(self,start,visited):
        visited[start]=True
        print(str(start)+' ->',end=' ')
        for i in range(self.size):
            if self.matrix[start][i]==1 and not visited[i]:
                self.DFS(start=i,visited=visited)
        
        
        
        
        
# LL:
# 1. value, list of none nodes *number of chilren


size = 7
g = Graph(size=size)
# for i in range(1, size ):
#     node1, node2 = map(int, input().split())
#     g.add_edge(node1=node1, node2=node2)
# g.traverse()
# g.remove_node(node1=input("Delete edge:\nNode1: "), node2=input("Node 2: "))
# g.traverse()
g.add_edge(1, 1)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)
g.add_edge(4, 2)
g.add_edge(5, 1)
g.add_edge(5, 2)
g.add_edge(6, 3)
g.add_edge(6, 4)
g.add_edge(6, 3)
g.traverse()
visited=[False]*size
g.DFS(start=3,visited=visited)
