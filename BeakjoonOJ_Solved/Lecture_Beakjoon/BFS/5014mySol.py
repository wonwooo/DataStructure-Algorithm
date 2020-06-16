'''
U층 위, D층 아래의 정점으로 가는 가중치가 누르는 동작 하나로 결정됨.
BFS를 통해 최소 거리를 찾을 수있음
'''
f, s, g, u, d = map(int, input().split())
visited = [-1]*(f+1)

q = []
q.append(s)
visited[s] += 1
while q:
    current = q.pop(0)
    up = current + u
    if up <= f and visited[up] == -1:
        visited[up] = visited[current] + 1
        q.append(up)
    down = current - d
    if down >= 1 and visited[down] == -1:
        visited[down] = visited[current] + 1
        q.append(down)

if visited[g] != -1:
    print(visited[g])
else:
    print('use the stairs')