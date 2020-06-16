import re
n = int(input())
a = [input() for _ in range(n)]

a_transpose = [''.join([a[i][j] for i in range(n)]) for j in range(n)]

answer_h = 0
for row in a:
    row = re.sub('X', ' ', row).split()
    for set in row:
        if set.count('.') >= 2:
            answer_h += 1

answer_v = 0
for row in a_transpose:
    row = re.sub('X', ' ', row).split()

    for set in row:
        if set.count('.') >= 2:
            answer_v += 1

print(answer_h, answer_v)