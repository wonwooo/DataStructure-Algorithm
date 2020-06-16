dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def check(a, b, x ,y, dir):
    n = len(a)
    m = len(a[0])
    i, j  = x, y
    while 0 <= i < n and 0 <= j < m:
        if a[i][j] == 6:
            break
        b[i][j] = a[x][y] #cctv가 닿는 곳을 모두 cctv종번호로 바꿈
        i += dx[dir]
        j += dy[dir]

def go(a, cctv, index, dirs):
    global anslist
    if len(cctv) == index: #cctv들의 방향 설정이 모두 끝남
        #check를 위해 a를 copy한 b를 이용
        n = len(a)
        m = len(a[0])
        b = [row[:] for row in a]
        for i, (what, x, y) in enumerate(cctv): #what:cctv기종, x,y : 위치
            if what == 1:
                check(a, b, x, y, dirs[i])
            elif what == 2:
                check(a, b, x, y, dirs[i])
                check(a, b, x, y, (dirs[i]+2)%4) #dir[i]와 dir[i]의 반대방향
            elif what == 3:
                check(a, b, x, y, dirs[i])
                check(a, b, x, y, (dirs[i]+1)%4)

            elif what == 4:
                check(a, b, x, y, dirs[i])
                check(a, b, x, y, (dirs[i] + 1) % 4)
                check(a, b, x, y, (dirs[i] + 2) % 4)

            elif what == 5:
                check(a, b, x, y, dirs[i])
                check(a, b, x, y, (dirs[i] + 1) % 4)
                check(a, b, x, y, (dirs[i] + 2) % 4)
                check(a, b, x, y, (dirs[i] + 3) % 4)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] == 0:
                    cnt += 1
        return cnt
    ans = 100
    print('ans : ', ans, 'index : ', index, 'dirs : ', dirs)
    for i in range(4): #dir은 cctv기종마다 4가지가 가능하다
        temp = go(a, cctv, index+1, dirs+[i]) # len(cctv) == index까지 가야 아랫줄로 내려감
        print('ans : ', ans, 'index : ', index+1, 'dirs : ', dirs+[i], 'temp : ', temp)
        if ans > temp:
            ans = temp
        anslist.append((index+1, ans))
    return ans



anslist = []
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if 1<= a[i][j] <= 5:
            cctv.append((a[i][j], i, j))
print(go(a, cctv, 0, []))

print(anslist)