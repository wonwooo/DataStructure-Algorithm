'''
[설계]
idx : 말판상의 위치
count : 몇번째 던지는 주사위인지 (0부터_)
주사위를 던질 때마다 해당하는 수로 1, 2,3, 4번 말을 모두 이동시켜본다.
이동시킨 뒤 idx를 return 하는 함수를 구현하고,
현재 위치가 도착점이 아니고, 옮기려는 말의 이동 시킨 뒤의 좌표가 도착점인것을 제외하고
이동 예정의 위치가 list에 있는지 확인 하고 재귀를 쏜다. 이동을 마치면 점수에 +해당 idx의 점수

재귀 탈출 조건 : count == 10:


'주사위 이동 구현'
핵심은 idx를 위한 array와, idx에 해당하는 값이 있는 array를 2개 만들어야 하고
5, 10 15에서 출발할 경우에는 다음 idx를 지정할 dictionary를 만들어야 한다.

a[0] = 1
a[1] =2
a[2] =3
...
a[20] = 21 (20이 40, 21이 도착)
a[21] = 21 이렇게 하면 도착칸에서 계속 돌수 있다.
뒤에 22부터 32까지? 계속 이어지진다



시작 할 때 파란 칸이 아닐때 즉 idx (5, 10, 15)가 아닐 땐
idx = a[idx]를 주사위에서 나온 수만큼 반복한다.

시작 할 때 파란 칸이라면 rchange써서 다음 idx를 정해주고 주사위에서 -1차감하고
a를 따라서 이동시작한다.
'''
nums = list(map(int, input().split()))
next= [0] * 33
for i in range(21):
    next[i] = i+1
next[21] = 21
next[22], next[23], next[24] = 23, 24, 30
next[25], next[26] = 26, 30
next[27], next[28], next[29] = 28, 29, 30
next[30], next[31], next[32] = 31, 32, 20
change={5:22, 10:25, 15:27}
values = [0]*33
for i in range(21):
    values[i] = i*2
values[22], values[23], values[24] = 13, 16, 19
values[27], values[28], values[29] = 28, 27, 26
values[30], values[31], values[32] = 25, 30, 35
values[25], values[26] = 22, 24

def move(idx, cnt):
    if idx in [5, 10, 15]:
        idx = change[idx]
        cnt -= 1
    for _ in range(cnt):
        idx = next[idx]
    return idx

def go(indices, count, s):
    global answer
    if count == 10:
        answer = max(s, answer)
        return

    for k in range(4):
        cidx = indices[k]
        if cidx == 21:
            continue
        nidx = move(cidx, nums[count])
        if nidx == 21:
            tmp = indices[:]
            tmp[k] = 21
            go(tmp, count+1, s)
        else:
            if nidx in indices:
                continue
            tmp = indices[:]
            tmp[k] = nidx
            go(tmp, count+1, s+values[nidx])


answer = 0
go([0, 0, 0, 0], 0, 0)
print(answer)


