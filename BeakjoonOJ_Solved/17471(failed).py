from collections import deque

n = int(input())
graph = {i : [] for i in range(1, n+1)}
peoples = list(map(int, input().split()))
a = [i for i in range(1, n+1)]
for i in range(1, n+1):
    info = list(map(int, input().split()))
    num = info[0]
    if num > 0:
        neighbors = info[1:]
        for neigh in neighbors:
            graph[i].append(neigh)
print(graph)
def check(a1,a2):
    global n
    #bfs 2번
    s = a1[0]
    q = deque()
    visited = [False] * (n+2)
    visited[s] = True
    q.append(s)
    res1 = [s]
    while q:
        cur = q.popleft()
        for nei in graph[cur]: #이웃들
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)
                res1.append(nei)
    result1 = True
    for e in a1:
        if e not in res1:
            result1 = False


    visited = [False] * (n+1)
    s = a2[0]
    q.append(s)
    res2 = [s]
    visited[s] = True
    while q:
        cur = q.popleft()
        for nei in graph[cur]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)
                res2.append(nei)
    result2 = True
    for e in a2:
        if not e in res2:
            result2 = False
    #print(res1, res2)
    if result1 and result2:
        return True
    else:
        return False

answer = -1
def go(idx, a1):

    global answer
    if 0 < len(a1) <= n/2:
        a2 = [i for i in range(1, n+1) if i not in a1]

        if check(a1, a2):
            s1 = sum([peoples[area-1] for area in a1])
            diff = abs(sum(peoples) - 2*s1)
            if answer == -1:
                answer = diff
            else:
                answer = min(answer, diff)
        #여기 return 넣으면 진행안된다...a1 갯수가 n<2이면 계속 가야하니까 return 넣지말것

    if idx < n:
        go(idx+1, a1+[idx])
        go(idx+1, a1)
    return

go(1, [])
print(answer)