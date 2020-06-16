import copy
from itertools import permutations
n, m , k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rotations = [list(map(int, input().split())) for _ in range(k)]

b = copy.deepcopy(a)
def rotate(rotation):
    global b
    r, c, s = rotation
    r, c = r-1, c-1

    for k in range(1, s+1): #k = 1,2, .., s까지 가야함
        tmp = b[r-k][c-k]
        for x in range(r-k, r+k, 1):
            b[x][c-k] = b[x+1][c-k]
        for y in range(c-k, c+k, 1):
            b[r+k][y] = b[r+k][y+1]
        for x in range(r+k, r-k, -1):
            b[x][c+k] = b[x-1][c+k]
        for y in range(c+k, c-k, -1): #여기서 k를 왜 s라고 썼어..
            b[r-k][y] = b[r-k][y-1]
        b[r-k][c-k+1] = tmp


order=[i for i in range(k)]
orders = list(permutations(order, k))
answer = 100*n*m
for order in orders:
    b = copy.deepcopy(a)
    for o in order:
        rotation = rotations[o]
        rotate(rotation)
    value = min((sum(row) for row in b))
    answer = min(answer, value)

print(answer)
'''
차분하게.. low level까지 집중 잃지 않고 생각해야한다.
생각의 속도를 늦춰야 low level까지 갈 수 있다.직관적으로 생각하지 않아야 한다

크기가 n*m 크기인 배열 A. 
배열 A의 값은 각 행에 있는 모든 수의 합 중 최솟값을 의미한다 
배열은 회전 연산을 수행할 수 있다. 회전연산은 세 개의 정수(R, C, S)로 이루어져 있다
가장 왼쪽 윗 칸이 r-s, c-s 가장 오른쪽 아랫칸이 r+s, c+s인 정사각형을 시계 방향으로 한 칸씩 돌린다
배열의 칸 r,c는 r행 c열을 의미한다
예를 들어 배열 A의 크기가 6*6이고 회전 연산이 (3, 4, 2)인 경우 아래 

회전 연산은 모두 한 번씩 사용해야 하며, 순서에 따라 배열의 값이 달라진다. 순서를 임의로 정해도 된다

[입력]
첫째 줄에 배열 A의 크기N,M,회전 연산의 개수 K가 주어진다
둘째 줄부터 N개의 줄에 배열 A에 있는 수 A[I][J]가 주어지고 다음 K줄에 회전 연산의 정보R,C,S가 주어진다

[출력]
배열 A값의 최솟값

r-s, c-s는 배열을 벗어나지 않는다(체크할 필요 없음)

[설계]
회전 연산의 순서를 순열로 구하고, 각 순열에 대해서

회전함수를 이용해 연산의 순서대로 A를 copy한 b를 회전한다
회전 함수는 연산만 받아서 하나의 연산만 수행하고 회전함수를 for문에서 연산 갯수만큼 불러온다.
b의 회전이 끝나면 b의 값을 구하고 정답을 갱신한다.

*회전 연산의 구현
가장 작은 r,s부터 시작해서 (r-s, c-s), (r+s, c+s) 의 s 1부터 s까지 늘려가면서 테두리를 회전시킨다
s가 정해지면, 4개의 for문을 사용해서 회전을 시작한다
우선 r-s c-s의 값을 tmp로 저장한다
1) r-s, c-s부터 r+s, c-s까지 행 내려가면서(r증가시키면서) 아랫 값을 당겨오기
2) r+s, c-s부터 r+s, c+s까찌 열 증가시키면서 오른쪽 값 당겨오기
3) r+s, c+s부터 r-s, c+s까지 행 감소시키면서 위엣 값 내려오기
4) r-s, c+s부터 r-s, c-s까지 열 감소시키면서 왼쪽 값 당겨오기
tmp 값을 r-s, c-s+1위치에 넣기



5 6 1
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
'''
