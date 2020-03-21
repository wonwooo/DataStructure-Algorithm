'''
테트로미노는 좌우 대칭, 회전이 가능하기때문에 총 19가지
하나의 테트로미노가 N X M 의 종이위에 놓일 수 있는 가짓수는 NM가지를 넘지 못함

경우의 수가 많지 않기 때문에 각각의 테트로미노에 대해 모든 칸에 놓아보도록 한다.
따라서 브루트 포스 유형
'''


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]
def go(x, y, sum, cnt):
    #탈출
    if cnt == 4:
        global ans
        if ans < sum:
            ans = sum
        return
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if c[x][y]:
        return
    c[x][y] = True
    for k in range(4):
        go(x+dx[k], y+dy[k], sum+a[x][y], cnt+1)
    c[x][y] = False


ans = 0
for i in range(n):
    for j in range(m):
        go(i,j,0,0)
        #예외 : 'ㅗ','ㅏ','ㅓ','ㅜ' 4개는 위의 go함수의 이동방식으로 확인할 수가 없어서 아래로 구현
        if j+2 < m:
            if j + 2 < m:
                temp = a[i][j] + a[i][j+1] + a[i][j+2]
                if i-1 >= 0:
                    temp2 = temp + a[i-1][j+1]
                    if ans < temp2:
                        ans = temp2
                if i+1 < n:
                    temp2 = temp + a[i+1][j+1]
                    if ans < temp2:
                        ans = temp2
        if i+2 < n:
            temp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j+1 < m:
                temp2 = temp + a[i+1][j+1]
                if ans < temp2:
                    ans = temp2
                if j-1 >= 0:
                    temp2 = temp + a[i+1][j-1]
                    if ans < temp2:
                        ans = temp2
print(ans)

