import sys
sys.setrecursionlimit(10000)


v, e = map(int, input().split())

graph = {'vertices':[i for i in range(1, v+1)], 'edges':[]}
for _ in range(e):
    u, v, weight = map(int, input().split())
    graph['edges'].append([weight, u, v])

parents = {}
rank = {}
def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(node_u, node_v):
    root1 = find(node_u)
    root2 = find(node_v)

    if rank[root1] < rank[root2]:
        parents[root1] = root2
    else:
        parents[root2] = root1
        if rank[root1] == rank[root2]:
            rank[root2] += 1

for v in graph['vertices']:
    parents[v] = v
    rank[v] = 0

result = 0
for edge in sorted(graph['edges']):
    weight, node_u, node_v = edge
    if find(node_u) != find(node_v):
        union(node_u, node_v)
        result += weight


print(result)





