n, m, x, y, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
for i in range(k):
    moves[i] -= 1
dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
#1은 항상 top, 6은 항상 bottom이고 회전에 따라 값만 바꿔준다
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for move in moves:
    nx, ny = x + dx[move], y+dy[move]

    if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
    if move == 0:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp
    if move == 1:
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp
    if move == 2:
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp
    if move == 3:
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp
    if a[nx][ny] == 0:
        a[nx][ny] = dice[6]
    else:
        dice[6] = a[nx][ny]
        a[nx][ny] = 0
    x, y=  nx, ny
    print(dice[1])

