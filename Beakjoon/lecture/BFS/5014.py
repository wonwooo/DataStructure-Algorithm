'''
눌러야 하는 버튼의 '최소'값을 구하므로 BFS이용
'한 번' 누를 때마다 모든 인접 노드로 갈 수 있으므로 BFS가능하다.
노드는 현재 층수
이웃 노드는 U를 눌러 올라간 층과 D를 눌러 내려간 층
방문 체크 배열을 선언하고 방문할 때마다 몇번째 탐색인지 깊이를 저장
원하는 노드(층수) 에 도달한 순간 체크 배열에서 몇 번째 탐색인지 불러온다.
'''

from collections import deque
f, s, g, u, d = map(int, input().split())
check = [False] * (f+1)
dist = [0] * (f+1)
q = deque()
q.append(s)
check[s] = True
while q:
    now = q.popleft()
    if now+u <= f and not check[now+u]:
        #index를 벗어나지 않는지 먼저 확인하고, 아니라면 check에서 해당값이 False인지도 확인 하는 조건이지만
        #둘의 위치를 바꾸면 , check[now+u]에서 이미 index가 배열밖으로 나가서 에러가 나서 순서 조심해야한다
        dist[now+u] = dist[now] + 1
        check[now+u] = True
        q.append(now+u)
    if now-d >= 1 and not check[now-d]:
        dist[now-d] = dist[now] + 1
        check[now-d] = True
        q.append(now-d)
#그냥 다 탐색 돌리고 g에 몇번째에 도달했는지 출력한다. 도달 못하는지도 확인 해야하기 때문인듯. 도달하자마자 끝내는 방법도 구현해보자
if check[g]:
    print(dist[g])
else:
    print("use the stairs")
