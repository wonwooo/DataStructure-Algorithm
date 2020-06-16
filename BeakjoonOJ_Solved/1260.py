from collections import deque
n, m, s = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
def dfs(s):
    print(s, end=' ')
    visited[s] = True
    for n in sorted(graph[s]):
        if not visited[n]:

            dfs(n)

    return


def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for n in sorted(graph[cur]):
            if not visited[n]:
                visited[n] = True
                q.append(n)
    return

dfs(s)
print()
visited = [False] * (n+1)
bfs(s)



