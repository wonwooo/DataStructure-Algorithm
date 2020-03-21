a, b, c = map(int, input().split())
visited = [[False] * 1500 for _ in range(1500)]
s = sum([a, b, c])
c = s-(a+b)
import copy
def bfs(a, b):
    global s
    q = []
    q.append((a, b))
    visited[a][b] = True
    while q:
        a, b = q.pop(0)
        for x in (a, b, s-(a+b)):
            for y in (a, b, s-(a+b)):
                if x > y:
                    x -= y
                    y += y
                    if not visited[x][y]:
                        visited[x][y] = True
                        q.append((x, y))

if s%3 != 0:
    print(0)
else:
    bfs(a, b)
    if visited[s//3][s//3] == True:
        print(1)
    else:
        print(0)




