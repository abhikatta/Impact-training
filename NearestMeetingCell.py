from collections import defaultdict, deque
G = defaultdict(list)
n = int(input())
arr = list(map(int, input().split()))
c = list(map(int, input().split()))
c1 = c[0]
c2 = c[1]
for u, v in enumerate(arr):
    if v == -1:
        continue
    G[u].append(v)


def bfs(n, c1, c2):
    q = deque([[c1, 1], [c2, 2]])
    vis = [0] * n
    while q:
        node, num = q.popleft()
        if vis[node] == 2 and num == 1 or vis[node] == 1 and num == 2:
            return node
        if vis[node] == num:
            continue

        vis[node] = num
        for nei in G[node]:
            q.append([nei, num])

    return -1


print(bfs(n, c1, c2))
