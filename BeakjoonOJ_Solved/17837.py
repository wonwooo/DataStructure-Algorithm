'''
말마다 방향과 위치를 dict로 기록하고
체스판 array를 만들어서 어디에 어떤 말이 있는지 list로 기록

말마다 돌아가면서
이동하려는 칸의 색에 따라서 다르게 구현
'''
n, k = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
marks = {}
for num in range(1, k+1):
    i, j, dir = map(int, input().split())
    marks[num] = {'loc' : [i-1,j-1], 'dir' : dir-1}
    chess[i-1][j-1].append(num)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dirchange = {0:1, 1:0, 2:3, 3:2}

count = 1


while True:

    for mark in range(1, k+1):
        x, y = marks[mark]['loc'] #현위치
        dir = marks[mark]['dir'] #현재 방향
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx>=n or ny<0 or ny>=n or color[nx][ny] == 2:
            dir = dirchange[dir]
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx>=n or ny<0 or ny>=n or color[nx][ny] == 2:#그대로 있는다

                marks[mark]['dir'] = dir
            elif color[nx][ny] == 0:
                idx = chess[x][y].index(mark)
                chess[nx][ny] += chess[x][y][idx:]
                for m in chess[x][y][idx:]:
                    marks[m]['loc'] = [nx, ny]
                marks[mark]['dir'] = dir
                chess[x][y] = chess[x][y][:idx]


            elif color[nx][ny] == 1:
                idx = chess[x][y].index(mark)
                chess[nx][ny] += chess[x][y][idx:][::-1]
                for m in chess[x][y][idx:]:
                    marks[m]['loc'] = [nx, ny]
                marks[mark]['dir'] = dir
                chess[x][y] = chess[x][y][:idx]

        elif color[nx][ny] == 0:
            idx = chess[x][y].index(mark)
            chess[nx][ny] += chess[x][y][idx:]
            for m in chess[x][y][idx:]:
                marks[m]['loc'] = [nx,ny]
            chess[x][y] = chess[x][y][:idx]

        elif color[nx][ny] == 1:
            idx = chess[x][y].index(mark)
            chess[nx][ny] += chess[x][y][idx:][::-1]
            for m in chess[x][y][idx:]:
                marks[m]['loc'] = [nx,ny]
            chess[x][y] = chess[x][y][:idx]



        check = False

        for i in range(n):
            for j in range(n):
                if len(chess[i][j]) >= 4:
                    check = True
                    break
        if check:
            break
    if check:
        break

    count += 1
    if count > 1000:
        count = -1
        break
print(count)

