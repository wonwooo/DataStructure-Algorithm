n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
marks = []
for _ in range(k):
    x, y, dir = map(int, input().split())
    marks.append((x-1, y-1, dir-1))
dirchange = {0:1, 1:0, 2:3, 3:2}
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(k):
    x, y, dir = marks[i]
    chess[x][y].append((i+1))

count = 1
done = False
while True:
    for p in range(k):
        cx, cy, dir = marks[p]
        nx, ny = cx+dx[dir], cy+dy[dir]
        #배열 밖으로 벗어나는 경우를 가장 먼저 처리하지 않으면 에러가난다
        if nx < 0 or nx >= n or ny < 0 or ny >= n or a[nx][ny] == 2:
            dir = dirchange[dir]
            nx, ny = cx+dx[dir], cy+dy[dir] #nx, ny를 바꿔주기만 하면 끝ㄴ는게아니라 바꾼 뒤에도 파란색이나 나갈것을 생각해야한다.
            if nx < 0 or nx >= n or ny < 0 or ny >= n or a[nx][ny] == 2:
                marks[p] = (cx, cy, dir)
                continue


        if a[nx][ny] == 0: #흰색
            idx = chess[cx][cy].index(p+1) #p+1이 p번째 말의 번호
            tmp = chess[cx][cy][idx:]
            chess[nx][ny] += tmp
            chess[cx][cy] = chess[cx][cy][:idx]
            for num in tmp:
                bx, by, d = marks[num-1]
                marks[num-1] = (nx, ny, d)
            marks[p] = (nx, ny, dir)

        elif a[nx][ny] == 1:#빨간색
            idx = chess[cx][cy].index(p + 1)  # p+1이 p번째 말의 번호
            tmp = chess[cx][cy][idx:]
            chess[nx][ny] += chess[cx][cy][idx:][::-1]
            chess[cx][cy] = chess[cx][cy][:idx]
            for num in tmp:
                bx, by, d = marks[num-1]
                marks[num-1] = (nx, ny, d)
            marks[p] = (nx, ny, dir)

        if len(chess[nx][ny]) >= 4:
            done = True
            break
    if done:
        break
    if count >=1001:
        break
    count += 1

print(count if count <=1000 else -1)


'''
17837 새로운 게임 

체스판을 이용한 새로운 게임을 만든다
크기 N*N인 체스판에서 진행되고 사용하는 말의 개수는 K개
하나의 말 위에 다른 말을 올릴 수 있다
체스판의 각 칸은 흰색 빨간색 파란색 중 하나로 색칠되어 있다.
게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1부터 K까지 번호가 매겨져있다.
이동방향도 미리 정해져 있고, 4방향으로 움직인다.
턴 한번은 1번부터 K번까지 순서대로 이동하는것. 올라간 말들도 같이 이동한다. 
말의 이동 방향에 있는 칸에 따라 말의 이동이 다르며 아래와 같다. 
턴 진행 중 말이 4개이상 쌓이면 게임이 종료된다. (4개가 쌓이면 해당 말 이동 하자마자 끝내야한다)
A번 말이
이동하려는 칸이 흰색이면 이동. 이동하려는 칸에 말이 있으면 가장 위에 A를 올림
위에 다른 말이 있었으면 A번말과 위의 말이 모두이동해서 위에 쌓인다.

빨간색인 경우 이동한 후 A번 말과 그 위의 모든 말이 쌓인 순서를 반대로 뒤집는다. 
즉 A위로 일단 뒤집고, 이동하려는 칸에 말이 있으면 뒤집어진 채로 올린다. 없으면 그냥 뒤집어진것만 올린다.

파란색인 경우 A말의 이동방향을 반대로 하고 한 칸 이동한다. 방향을 반대로바꾼 후에도 이동하려는 칸이
파란색이면 이동하지 않고 가만히 있는다. (방향만 바뀐 채로)

체스판을 벗어나는 경우에는 파란색과 마찬가지로, 
이동방향을 반대로 하고 한 칸 이동한다. 이때에도 이동하려는 칸이 파란색이면 방향만 바뀐 채 가만히 있고,
빨간색, 흰색이면 위의 지시를 따른다.

말은 1번말부터 순서대로이동한다 . 
[입력]
첫 줄에 N, K
둘째줄부터 N줄에 체스판의 정보. 0흰색 1빨간 2파랑
다음 K줄에 말의 정보가 1번부터 순서대로. 
말은 3개의 정수 : 행, 열, 이동방향 (이동방향은 1부터 순서대로 동서북남)
N은 4이상 12이하 / K는 4이상 10이하
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 2


[출력]
게임이 종료되는 턴의 번호. 1000보다 크거나 게임이 종료되지 않는 경우 -1

[설계]
일단 원소가 []로 이루어진 n*n 배열을 만든다
1번부터 k번까지의 위치와 방향이 담긴 list를 만든다. [x, y, dir]형태로 담는다
말판의 list에 주어진 위치대로 말을 추가한다
count = 1부터 시작하고
while문 안에서 1번부터 k번까지의 말이 모두 이동을 마치면 count를 증가한다.
1번부터 k번까지의 말이 하나 이동 할 때마다 업힌 말이 4개가 있는지 for문으로 확인하고(말의 위치만 돌면서 해당위치의
길이가 4이상인지 확인하면 된다) 확인 하면 count올라가기 전에 break걸어야한다

"이동구현"
for i in range(k):
cx, cy, dir = players[k]

nx, ny를 dir에 맞에 만들고 0흰색 1빨간색 2파란 3 배열밖에 맞게 구현한다
파란과 배열 밖은 같은 경우로 묶고, 방향을 바꾼 위 흰/빨/파에 따른다. 
방향을 바꾸는 dict도 선언한다
'''