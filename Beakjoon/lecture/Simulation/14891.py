n = 4
a = [list(input()) for _ in range(n)] #톱니바퀴 상태
k = int(input())
for _ in range(k):
    no, dir = map(int, input().split()) #dir = +=1
    no -= 1
    d = [0]*n
    d[no] = dir #지정된 톱니바퀴의 회전방향
    for i in range(no-1, -1, -1): #no번째 톱니바퀴 왼쪽부터 순회
        if a[i][2] != a[i+1][6]: # 왼쪽 톱니의 오른편과 오른쪽 톱니의 왼편
            d[i] = -d[i+1] #왼쪽의 회전방향은 오른쪽의 반대
        else:
            break # 극이 같다면 움직이지 않으므로 더 왼쪽으로 갈 필요 없음

    for i in range(no+1, n):
        if a[i][6] != a[i-1][2]:
            d[i] = -d[i-1]
        else:
            break

    for i in range(n):
        if d[i] == 0:
            continue
        if d[i] == 1:
            temp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        elif d[i] == -1:
            temp = a[i][0]
            for j in range(7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp

ans = 0
for i in range(n):
    if a[i][0] == '1':
        ans += 2**i
print(ans)
