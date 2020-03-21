'''
12886 돌 그룹

DFS로 구하면 가능한 지 , 불가능한지만 구할 수 있다.
BFS로 구하면 가/불 여부와 몇 번만에 가능한지까지 구할 수 있다.

방문확인에 필요1한 배열은 2차원이면 충분하다. 나머지 한그룹의 값은 빼주면 구할 수있다.
아래 코드는 DFS이고, BFS로도 구현 해 보자.
이문제에서 메모리 제한 넘어갈 지 가늠하는 부분 있는데 참고할것
'''
import sys
sys.setrecursionlimit(1500*1500)
check = [[False]*1501 for _ in range(1501)]
x, y, z = map(int, input().split())
s = x+y+z
def go(x, y):
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, s-x-y]
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                #for문 내부에서 a가 바뀌면 안되어서 b를 만들어 전달한다.
                b = [x, y, s-x-y]
                b[i] += a[i]
                b[j] -= a[i]
                go(b[0], b[1])
if s % 3 != 0:
    print(0)
else:
    go(x, y)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)

