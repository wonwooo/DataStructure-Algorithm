from collections import deque
n = int(input())
graph = {i:[] for i in range(1, n+1)}
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        cur = q.popleft()
        for neigh in graph[cur]:
            if not visited[neigh]:
                visited[neigh] = True
                q.append(neigh)
    return


def dfs(s):
    for neigh in graph[s]:
        if not visited[neigh]:
            visited[neigh] = True
            dfs(neigh)
    return


visited = [False] * (n+1)
visited[1] = True
bfs(1)
visited[1] = False
print(sum(visited))

