N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(M)]

def search(r, c, d):
    arr[r][c] = 2 #청소
    if d == 0: #북
        if arr[r][c-1] == 0:
            search(r, c-1, 3)

    if d == 1: #동

    if d == 2: #남
        pass
    if d == 3: #서
        pass