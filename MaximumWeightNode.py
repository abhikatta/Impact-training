import collections


def MaxWeightNode(size, cells):
    nodes = collections.defaultdict(int)
    for k, size in enumerate(cells):
        if size != -1:
            nodes[size] += k
    req = max(nodes.values())
    for k, size in nodes.items():
        if size == req:

            break
    return k


size = int(input())
cells = list(map(int, input().split()))
print(MaxWeightNode(size, cells=cells))
