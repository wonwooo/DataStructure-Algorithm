from collections import deque
n = int(input())
start, end = map(int, input().split())
visited = [0] * (n+1)
graph = {i:[] for i in range(1, n+1)}
m = int(input())
for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

q = deque()
q.append(start)
while q:
    cur = q.popleft()
    for neigh in graph[cur]:
        if not visited[neigh]:
            visited[neigh] = visited[cur] + 1
            q.append(neigh)

print(visited[end] if visited[end] else -1)


#dfs도구현해볼것