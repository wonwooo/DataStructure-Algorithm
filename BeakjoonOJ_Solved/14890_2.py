n, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def check(ls):
    global ladder
    result = True
    for i in range(1, len(ls)):
        if ls[i] < ls[i-1]:
            if ls[i-1] - ls[i] > 1:
                result = False
                break
            if len(ls[i:]) < l:
                result = False
                break
            if not ls[i:i+l] == [ls[i]]*l:
                result = False
                break
            #차이가 1이고, l만큼 여유 있고, l개의 높이가 같으면, 사다리 놓여있는지 확인하고 사다리 놓는다
            if True in ladder[i:i+l]:
                result = False
                break
            else:
                ladder[i:i+l] = [True] * l
                continue
    return result


answer = 0
for row in a:
    ladder = [False]*n
    if check(row):
        ladder = ladder[::-1]
        if check(row[::-1]):
            answer += 1
for c in range(n):
    col = [a[i][c] for i in range(n)]
    ladder = [False] * n
    if check(col):
        ladder = ladder[::-1]
        if check(col[::-1]):
            answer += 1
print(answer)

