import math

def find(node):
    global parent
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    global parent
    p1 = find(node1)
    p2 = find(node2)
    if p1>p2:
        parent[p1] = p2
    else:
        parent[p2] = p1

def kruskal(edges):
    result = 0
    for d, node1, node2 in edges:
        if find(node1) != find(node2):
            union(node1, node2)
            result += d
    return result

n, m = map(int, input().split())
parent = {i:i for i in range(1, n+1)}
locs = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    union(node1, node2)
edges = []
for i in range(n-1):
    for j in range(i+1, n):
        dx = locs[i][0] - locs[j][0]
        dy = locs[i][1] - locs[j][1]
        dist = math.sqrt(dx**2 + dy**2)
        edges.append((dist, i+1, j+1))
edges.sort()

answer = kruskal(edges)
print('%0.2f' % answer)
'''
4 3
1 1
3 1
2 3
4 3
1 4
1 2 
2 4
'''