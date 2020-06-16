'''
한 컴퓨터가 해킹 당했다
서로 의존하는 컴퓨터들은 하나둘 전염되기 시작한다.
어떤 컴 A가 B에의존한다면 B가 감염되면 그로부터 일정시간 뒤 A도 감염된다.
이때 B가 A를 의존하지 않는다면 A가 감염되더라도 B는 안전하다
해킹한 컴터 번호와 각 의존성이 주어지면 총 몇대의 컴터가 감염되며
그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성 하시오

[입력]
첫줄에 테스트케이스의 개수 : 최대 100개

하나의 테케는 다음과같다
첫줄에 컴퓨터개수, 의존성개수, 해킹당한 컴퓨터 번호 n, d, c (각각 1이상 , c는 n이하)
이어서 d 줄에 각 의존성을 나타내는 정수 a b s가 주어진다
a b를 의존, s는 거리 즉 b에서 a를 향하는 s의간선
[출력]
각 테케마다 한 줄에 걸쳐 감염되는 컴퓨터 수 , 마지막 컴퓨터까지 걸리는 시간을 공백으로 구분지어 출력
[설계]
dijkstra함수에 start, num을 전달하여 통해 distance table(최단거리 table)을 만들고
거리가 inf가 아닌 node의 갯수를 감염된 컴퓨터 갯술, 가장 긴 거리를 감염시간으로 출력한다.

'''
import heapq
cases = []
t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = {i:{} for i in range(1, n+1)}
    for _ in range(d):
        node1, node2, weight = map(int, input().split())
        graph[node2][node1] = weight
    cases.append([c, graph])

def dijkstra(start, graph):
    q = []
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    heapq.heappush(q, [distances[start], start])
    while q:
        cdist, cnode = heapq.heappop(q)
        if cdist > distances[cnode]:
            continue
        for neigh, dist in graph[cnode].items():
            if cdist+ dist < distances[neigh]:
                distances[neigh] = cdist + dist
                heapq.heappush(q, [distances[neigh], neigh])
    count = 0
    maxtime = 0
    for node, time in distances.items():
        if time != float('inf'):
            count += 1
            maxtime = max(maxtime, time)
    print(count, maxtime)
    return

for start, graph in cases:
    dijkstra(start, graph)
