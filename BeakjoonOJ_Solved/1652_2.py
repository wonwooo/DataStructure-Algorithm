n = int(input())
a = [input() for _ in range(n)]
a_transpose = [''.join([a[i][j] for i in range(n)]) for j in range(n)]

def count(row):
    num = 0
    cnt = 0
    for e in row:
        if e == '.':
            cnt += 1
        elif e == 'X':
            if cnt >= 2:
                num += 1
            cnt = 0
    if cnt >= 2:
        num += 1
    return num

answer_h = 0
for row in a:
    answer_h += count(row)
answer_v = 0
for row in a_transpose:
    answer_v += count(row)

print(answer_h)
print(answer_v)