n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, z = map(int, input().split())
    trees[r-1][c-1].append(z)
nut = [[5]*n for _ in range(n)]
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def spring():
    global a, nut, trees
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            remain = []
            died = []
            for tree in sorted(trees[i][j]):#어린 나무부터
                if tree > nut[i][j]:
                    died.append(tree)
                if tree <= nut[i][j]:
                    nut[i][j] -= tree #양분 먹고
                    remain.append(tree+1)#한살 더 먹고
            trees[i][j] = remain
            #다 죽으면 그때 양분으로 추가(동시에하면안됨)
            for d in died:
                nut[i][j] += (d // 2)


def autumn():
    global a, nut, trees
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            for tree in trees[i][j]:
                if tree%5 == 0:
                    for k in range(8):
                        nx, ny = i+dx[k], j+dy[k]
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        trees[nx][ny].append(1)

def winter():
    global a, nut, trees
    for i in range(n):
        for j in range(n):
            nut[i][j] += a[i][j]

for _ in range(k):
    spring()
    autumn()
    winter()

answer =0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)
'''
NxN의 땅을 구매했다
로봇은 땅의 양분을조사해 전송, 모든칸을 조사
처음 모든 칸의 5의 양분이 있다
M개의 나무를 구매해 땅에심었다

한 칸의 여러개의 나무를 심었을 수도 있다

사계절을 보내며 반복되는것
봄에는 나이만큼 양분 먹고 나이 +1
각 나무는 자신이 있는 칸의 양분만 먹을수있다
한 칸에 여러 나무가 있다면 어린 나무부터 양분을 먹는다(나이만큼)
땅에 양분이 부족해 나이만큼 먹을 수 없으면 바로 DIE

여름에는 봄에 죽은 나무가 양분으로 변한다; 죽은 나무의 나이/2만큼 양분이 추가(소수버림)

가을에는 나무 번식

나이가 5의 배수인 나무만 번식 가능하고 인접한 8개의 칸에 나이 1인 나무를 만든다
상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다



겨울에는 로봇이 땅에 양분을 추가한다 . 각 칸마다 A[r][c]만큼 추가된다. 입력으로 주어짐
K년이 지난 후 땅에 살아있는 나무의 갯수 출력

[입력]
첫 줄 N,M,K
둘재줄부터 N줄에 A배열 
다음 M줄에 나무의 정보 X, Y, Z : 나무의 위치 XY, 나무의 나이 Z

[출력]
K년뒤 생존한 나무갯수 
[제한]
N은 1이상 10이하 M은 1이상 100이하 K는 1이상 1000이하
나이 Z는 1이상 10이하 
입력시 나무의 위치는 모두 서로 다름

[설계]
n * n 배열 양분 5로 초기화
tree 배열 n*n으로, 각 원소 비어있는 list로 초기화
m개의 나무는 위치의 list에 나이값으로 추가
k년 뒤
나무위치는 받아서 1 빼고 나이는 그대로



5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

2




'''