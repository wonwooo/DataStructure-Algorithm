n = int(input())
k = int(input())
apples=[]
for _ in range(k):
    x, y = map(int, input().split())
    apples.append([x-1, y-1])

l = int(input())
change = {}
for i in range(l):
    d = input().split()
    change[int(d[0])] = d[1]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 1
dir = 0
body = [[0, 0]]

while True:
    head = body[-1]
    #print('time:{}, head:{}, body:{}'.format(time, head, body))
    nx, ny = head[0] + dx[dir], head[1] + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break
    if [nx, ny] in body:
        break
    if [nx, ny] in apples:
        body.append([nx, ny])
        apples.remove([nx, ny])
    else:
        body.append([nx, ny])
        body.pop(0)

    if body[-1] in body[:-1]:
        break

    if time in change:
        if change[time] == 'L':
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
    time += 1

print(time)
