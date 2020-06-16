from collections import deque
t = int(input())
cases = []
for _ in range(t):
    ls = []
    n = int(input())
    for _ in range(n+2):
        ls.append(list(map(int, input().split())))
    cases.append(ls)

def check(ls):
    q = deque()
    visited = [False]*len(ls)
    q.append(0)
    visited[0] = True
    while q:
        cur = q.popleft()
        cx, cy = ls[cur]
        for i in range(len(ls)):
            if visited[i]:
                continue
            nx, ny = ls[i]
            dist = abs(cx - nx) + abs(cy - ny)
            if dist<=1000:
                visited[i] = True
                q.append(i)
    if visited[-1]:
        return 'happy'
    else:
        return 'sad'

answer = []
for case in cases:
    answer.append(check(case))

for ans in answer:
    print(ans)

'''
맥주를 마시면서 걷는다
상근이네 집에서 출발, 한박스 들고출발
한박스는 맥주 20개
50m에 한병씩 마신다
가다가 편의점에 들르면 빈 병을 버리고 새 맥주를 살 수 있다
하지만 20병을 넘을 수 없다
편의점/집/목적지의 좌표가 주어지면 맥주를 계속 마시면서 갈 수 있는지 구하라

[입력]
첫줄에 테케갯수 t (50이하)
각 테케 첫줄에는 맥주파는 편의점갯수 n(0이상 100이하)
다음 n+2줄에 집, 편의점/ 목적지 좌표가 주어진다
각 좌표는 x,y로 이루어짐 ( 모두 정수, 미터값)
두 좌표간의 거리는 x차이 + y차이(맨해튼거리)

[출력]
'happy' or 'sad'

[설계]
맥주가 떨어지지 않고 갈 수 있는지 확인하는 방법
집에서 출발해서 편의점을 들르면서 목적지까지 맥주가 떨어지지 않으면 된다

n+2 사이즈의 list에 집, 편의점, 목적지의 위치(x,y)를 담는다
visited list를 n+2로 담는다

BFS 구현
인접 노드들 : 맥주가 떨어지지 않고 갈 수 있는 node
집에서 시작해서 for문으로 편의점 포함 락페 좌표까지 탐색하며 인접 노드이면 모두 que에 담고 visited처리

탐색이 끝나면 락페가 visited처리 되어있는지 확인하고 맞으면 happy 아니면 sad


2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000

happy
sad
'''