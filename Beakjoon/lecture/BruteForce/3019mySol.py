c, type = map(int, input().split())
a = list(map(int, input().split()))

def check(idx, len, shape): #idx(시작점위치), len(시작점으로부터 길이), shape(떨어지는 지점 형태)
    global a
    if idx + len - 1 > c - 1:
        return 0
    base = a[idx : (idx+len)]

    for i in range(len):
        if base[0] + shape[0] != base[i] + shape[i]:
            return 0
    return 1

ans = 0
for idx in range(c):
    if type == 1:
        ans += check(idx, 1, [0]) + check(idx, 4,[0, 0, 0, 0])
    if type == 2:
        ans += check(idx, 2, [0,0])
    if type == 3:
        ans += check(idx, 3, [1, 1, 0]) + check(idx, 2, [0, 1])
    if type == 4:
        ans += check(idx, 3, [0, 1, 1]) + check(idx, 2, [1, 0])
    if type == 5:
        ans += check(idx, 2, [1, 0]) + check(idx, 2, [0, 1]) + check(idx, 3, [0, 0, 0]) + check(idx, 3, [0, 1, 0])
    if type == 6:
        ans += check(idx, 3, [0, 0, 0]) + check(idx, 2, [0, 0]) + check(idx, 3, [1, 0, 0]) + check(idx, 2, [0, 2])
    if type == 7:
        ans += check(idx, 3, [0, 0, 0]) + check(idx, 2, [0, 0]) + check(idx, 3, [0, 0, 1]) + check(idx, 2, [2, 0])

print(ans)



