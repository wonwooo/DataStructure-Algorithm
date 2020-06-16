import copy
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def transpose(arr):
    arr = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr))]
    return arr


def merge(a, dir):
    b = copy.deepcopy(a)
    l = len(b)
    for i in range(l):
        row = [b[i][j] for j in range(l) if b[i][j] != 0]
        if dir == 2:
            row = row[::-1]
        k = 0
        while k <len(row)-1: #길이가 변하는 list에 index로 접근하기 위해서 while문
            if row[k] == row[k+1]:
                row[k] *= 2
                row.pop(k+1)
                k += 1
            else:
                k += 1
        if dir == 1:
            b[i] = row + [0] * (l - len(row))
        if dir == 2:
            b[i] = [0] * (l - len(row)) + row[::-1]
    return b



def go(arr, count):

    global answer
    maxval = 0
    #더이상 개선 가능성 없을 떄 backtracking
    for i in range(n):
        for j in range(n):
            maxval = max(arr[i][j], maxval)
    answer = max(answer, maxval)


    if count < 5:
        #여기서 merge함수 쓸때마다 arr가 변하지 않도록 copy함수를 썼어야 했는데, 그렇지 않아서 많은 시간을 디버깅에 날림
        go(merge(arr, 1), count + 1)
        go(merge(arr, 2), count + 1)
        go(merge(transpose(arr), 1), count + 1)
        go(merge(transpose(arr), 2), count + 1)

    return

answer = 0
go(a, 0)

print(answer)

'''
[설계]
row마다 합치는 로직 구현방법: 
0을 모두 제거한다 (한쪽에 쏠리는 효과)
왼쪽으로 기울였을때 합쳐지는로직 구현 : 합친 뒤 부족한 길이만큼 오른쪽에 0으로 패딩
오른쪽으로 기울였을 때 합쳐지는 로직 구현 : 합친 뒤 부족한 길이만큼 왼쪽에 0으로 패딩

위로 기울일 땐 transpose 시키고 왼쪽로직 구현 후 다시 transpose
아래록 기울일 땐 tr ->오른쪽  로직구현 후 다시 transpose

최대 5개이하의 중복순열 재귀함수로 구현해서 모두 simulation돌리고 최대값 갱신
먼저 순서를 만들어 놓고 돌리면, 불필요한 연산이 늘어난다

예를들어 [1,2],[1,2,3]같은 경우는 앞의 1,2연산을 괜히 2번 중복하기 때문에, 돌려가면서 갱신하는 것이 훨씬 낫다

1로 기울이고 count+1하여 재귀함수로 쏘고(기울였다가 돌리는게 아니라 기울인 a를 인자로전달)
2로 기울이고 count+1하여 쏘고
3 ''
4 ''
이렇게 해서 재귀함수에서 받아서 바로 a의 최댓값을 갱신한다


3
2 2 2
4 4 4
8 8 8
'''