'''
generate_newcurve

새로운 이전 세대의 끝(시작점), [이전 세대의 진행]을 전달받음

[이전 세대의 진행] 순서를 뒤집고 , 반시계 방향으로 90도 회전까지 시킨 [새 진행] 만듦

이전세대의 끝에서 [새 진행]으로 따라가면서 mark, 새로운 끝점 도달

새로운 끝점, ([진행] + [새 진행]) 다시 전달

문제에서 말하는 x, y가 내가 배열에서 쓰던 x(row), y(col)과 반대라서 헷갈림.
input받을 때 x,y를 반대로 받아서 해결함

'''
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]



n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * 101 for _ in range(101)] #0<=x<=100, 0<=y<=100

def markDragonCurve(endBefore, directions, cnt, generation):
    global visited
    if cnt == generation: #cnt:몇 세대까지 마크했는지

        return
    x, y = endBefore
    visited[x][y] = True
    newdir = directions[:]
    newdir.reverse()
    #반시계 90도 회전
    for i in range(len(newdir)):
        newdir[i] = (newdir[i]+1) % 4


    for dir in newdir:
        x, y = x + dx[dir], y + dy[dir]
        visited[x][y] = True

    markDragonCurve((x,y), directions+newdir, cnt+1, generation)

for curve in curves:
    y,x, dir, g = curve
    visited[x][y] = True
    visited[x+dx[dir]][y+dy[dir]] = True
    endBefore = (x + dx[dir], y+dy[dir])
    directions = [dir]
    markDragonCurve(endBefore, directions, 0, g)

#정사각형 갯수 찾기
num = 0
for i in range(100):
    for j in range(100):



        if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
            num += 1
print(num)