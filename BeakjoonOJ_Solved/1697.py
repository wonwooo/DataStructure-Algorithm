from collections import deque
n, k = map(int, input().split())
visited = [-1] * (100001)
visited[n] = 0
q = deque()
q.append(n)

while q:
    cur = q.popleft()
    if cur-1>=0 and visited[cur-1] == -1:
        visited[cur-1] = visited[cur] + 1
        q.append(cur-1)
    if cur+1<=100000 and visited[cur+1] == -1:
        visited[cur+1] = visited[cur] + 1
        q.append(cur+1)
    if 0 <= 2*cur <= 100000 and visited[2*cur] == -1:
        visited[2*cur] = visited[cur] + 1
        q.append(2*cur)

print(visited[k])

