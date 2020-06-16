n, m, h = map(int, input().split())
locs = [list(map(int, input().split())) for _ in range(m)]
ladder = [[0]*n for _ in range(h)]
for x, y in locs:
    ladder[x-1][y-1] , ladder[x-1][y] = 1, 2

def play():
    global ladder
    result = True
    for c in range(n):
        start = c
        r = 0
        while r<h:
            if ladder[r][c] == 1:
                c += 1
            elif ladder[r][c] == 2:
                c -= 1
            r += 1
        if c != start:
            result = False
            break
    return result

answer = float('inf')
def go(idx, count):
    global answer
    if count > 3:
        return
    if count > answer:
        return
    else:
        if play():
            answer = min(answer, count)

    for i in range(idx, n*h):
        r = i // n
        c = i % n
        if c < n-1 and not ladder[r][c] and not ladder[r][c+1]:
            ladder[r][c], ladder[r][c+1] = 1, 2
            go(i+2, count+1)
            ladder[r][c], ladder[r][c+1] = 0, 0

    return

go(0, 0)
print(-1 if answer==float('inf') else answer)
'''
사다리게임
n개의 세로선 m개의 가로선
세로선 사이에 가로선을 놓을 수있다. 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
모든 세로선이 같은 위치를 갖는다. 
즉 세로길이 h 가로길이 n

초록선은 세로선을 나타내고 초록선과 점선이 교차하는 점은 가로선을 놓을 수 있다
가로선이 연속하면 안된다. 

i번 세로선의 결과가 i번이 나오도록 조작하기 위해 추가 할 가로선 갯수의 최솟값

[입력]
첫줄에 세로선의 갯수 n, 놓을 수 있는 가로선 갯수 m, 가로선 놓을 수 잇는 갯수 h
n은 2이상 10이하, h는 1이상 30이하
둘째줄부터 가로선의 정보가 한 줄에 하나씩 주어진다
가로선의 정보는 두 정수 a와 b
b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결 했다는 의미
즉 arr[a][b]에 두었다는 의미
2 1 3
1 1

1

추가할 가로선의 최솟값을 출력한다. 정답이 3보다 크면 -1을 출력한다. 불가능한 경우에도 -1을 출력한다
[설계]

최대 3개까지 가로선을 늘려 가면서, 모든 조합에 대해서 사다리게임을 해본다.
이때 들어온 사다리 갯수가 answer보다 크면 return하는 backtracking을 구현한다.
play함수에 넘겨서 결과가 원한대로 나오면 True를 넘겨받고 사다리 갯수를 answer로 갱신한다

0, 0부터 시작해서 column이 h-1보다 작은 경우에 모두 사다리를 놓을 수 있다.
사다리는 0부터 n*h-1까지의 idx값을 idx//h : 행번호 idx%h :열번호 로 구해서
for문으로 돌릴 수 있다. 
for문 안에서, 사다리가 있는지 확인하고,
사다리를 놓는다면, (행, 열)을 list에넣고 idx + 2/ 놓지 않는다면 idx+1해서 재귀함수를 쏜다

play함수 : ladder, candlist를 받는다 
candlist의 위치에 사다리를 놓고, 그 오른쪽에도 사다리를 놓는다
왼쪽은 1, 오른쪽은 2로 놓는다
c = 0부터 시작해서 n-1까지 a[0][c]부터 내려가본다
r = 0
while r<h:
if a[r][c] == 1: 오른칸으로 이동해서 한칸 내림 r+1
elif a[r][c] == 2: 왼 칸으로 이동해서 한 칸 내림 r+1
아니면 그냥 r+1
while문이 끝났을 때 c가 시작과 같지 않으면 result = False하고 break
 
'''


