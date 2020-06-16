from collections import deque
n = int(input())
num = list(map(int, input().split()))
graph = {i:[] for i in range(1, n+1)}
for i in range(1, n+1):
    info = list(map(int, input().split()))
    if info[0] == 0:
        continue
    for area in info[1:]:
        graph[i].append(area)
        graph[area].append(i)


def check(a1, a2):
    #a1을 check할땐 a2의 방문을 모두 True처리할것; a2할때도 마찬가지
    #bfs가 끝나면 a1의 구역들이 모두 방문처리 되었는지 확인하면 된다
    visited = [False]*(n+1)
    for a in a2:
        visited[a] = True
    q = deque()
    q.append(a1[0])
    visited[a1[0]] = True
    while q:
        cur = q.popleft()
        for neigh in graph[cur]:
            if not visited[neigh]:
                visited[neigh] = True
                q.append(neigh)
    connected1 = True if False not in visited[1:] else False

    visited = [False] * (n + 1)
    for a in a1:
        visited[a] = True
    q = deque()
    q.append(a2[0])
    visited[a2[0]] = True
    while q:
        cur = q.popleft()
        for neigh in graph[cur]:
            if not visited[neigh]:
                visited[neigh] = True
                q.append(neigh)
    connected2 = True if False not in visited[1:] else False
    #단순히 a1, a2만 연결 되었는지 확인하면 안되고 visited전체가 True인지 확인해야한다
    #a1, a2가 둘다 섬처럼 동떨어진 경우도 있기 때문
    if connected1 and connected2:
        return True
    else:
        return False


answer = float('inf')
def go(idx, a1, a2):
    global answer
    if idx == n+1 and len(a1) >= 1 and len(a2) >= 1:
        s1 = 0
        for a in a1:
            s1 += num[a-1]
        s2 = sum(num) - s1
        diff = abs(s2 - s1)
        if diff >= answer:
            return
        if check(a1, a2):
            answer = diff
        return

    if idx < n+1:
        go(idx + 1, a1+[idx], a2)
        go(idx + 1, a1, a2+[idx])
    return

go(1, [], [])
print(answer if answer!= float('inf') else -1)


'''
공평하게 선거구를 확정
N개의 구역, 1번부터 N번까지 매겨진 번호
두개의 선거구
각 구역은 두 선거구 중 하나에 포함
선거구는 구역을 적어도 하나 포함
한 선거구 내의 구역은 모두 연결되어이써야 한다
구역 A에서 B로 갈때 인접한 구역들이 모두 같고, 그 구역들들을 통해 B에 도달한다면 A와 B는 같은 구역
공평하게 선거구를 나누기 위해 두 선거구에 포함된 인구차를 최소화 하려한다
인구차의 최솟값을 구하자

[입력]
첫줄에 구역의 개수 N
둘째줄에 1번부터 N번까지의 인구가 공백으로 한줄로 
셋째 줄부터 N개의 줄에 각 구역과 인접한 구역의 정보(1번구역부터) 
각 정보의 첫번째 정수는 그 구역과 인접한 구역의 수 
이후 인접한 구역의 번호가 주어진다. 모든 값은 정수
인접한 구역이 없을 수도 있다.

[출력]
두 선거구로 나누었을때 인구 차의 최솟값을 출력한다
두 선거구로 나눌 수 없을 경우에는 -1을 출력한다

N은 2이상 10이하
구역 내의 인구수는 1이상 100이하 

[설계]
1부터 N까지를 조합으로 구역 1과 2에 각각 넣어가면서 탐색
N까지 탐색 끝나면 각 구역 크기가 1 이상인경우에 한해서 
두 구역이 모두 이어져 있는지, 이어져있다면 인구 차이가 몇인지 CHECK해서
answer list에 기록
answer list가 공백이면 -1, 아니라면 최소값 출력

각 구역의 인구수는 list로 기록
graph로 인접 구역정보 저장


6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2

1
'''