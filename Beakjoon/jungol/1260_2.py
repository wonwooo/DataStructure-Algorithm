def dfs(vertex):
    global visited
    if not visited[vertex]:
        visited[vertex] = True
        print(vertex,end=' ')
    else:
        return
    for neighbor in sorted(graph[vertex]):
        if not visited[neighbor]:
            dfs(neighbor)


def bfs(vertex):
    global visited
    if not visited[vertex]:
        visited[vertex] = True
    else:
        return
    queue = [vertex]
    while len(queue) != 0:
        current = queue.pop(0)
        print(current, end=' ')
        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


V, E, startValue = map(int, input().split())
graph = {}
for v in range(1, V+1):
    graph[v] = set()
for i in range(E):
    src, dst = map(int, input().split())
    graph[src].add(dst)
    graph[dst].add(src)

visited = [False] * (V+1)
dfs(startValue)
print()
visited = [False] * (V+1)
bfs(startValue)
