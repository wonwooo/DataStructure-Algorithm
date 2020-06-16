'''
유형 : 시뮬레이션; 문제에 나와있는 모든 조건을 구현해야 한다.

가장 처음에 주사위의 모든 면에 0이 적혀져 있음
주사위를 굴렸을 때, 이동한 칸에 써 있는 수가 0이면, 주사위의 바닥면에 써 있는 수가 칸에 복사된다
0이 아닌 경우에는 칸에 써 있는 수가 주사위의 바닥면으로 복사되어야 하며 칸에 써 있는 수는 0이 된다
바깥으로 이동시키려 하는 경우에는 해당 명령을 무시해야 하며 출력해서도 안된다.

각 면의 번호를 붙이고, 굴러서 이동하는 방향에 따라 각 면에 있는 값들이 어떻게 교환되는지 생각해봐야 한다.
'''



dx = [0,0,-1,1]
dy = [1,-1,0,0] #0동 1서 2북 3남으로 설정
n,m,x,y,l = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dice = [0]*7 #i번 면에 적혀있는 수
move = list(map(int,input().split()))
for k in move:
    k -= 1 #하나씩 작아야함
    nx,ny = x+dx[k],y+dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: #바깥으로 이동하는 경우 무시
        continue
    if k == 0:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif k == 1:
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif k == 2:
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    else:
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp
    x,y = nx,ny
    if a[x][y] == 0:
        a[x][y] = dice[6]
    else:
        dice[6] = a[x][y]
        a[x][y] = 0
    print(dice[1])
