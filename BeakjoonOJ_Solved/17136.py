'''
시간 줄이는 방법 찾기
'''

import sys
sys.setrecursionlimit(100000)

a = [list(map(int, input().split())) for _ in range(10)]
empty = []
for i in range(10):
    for j in range(10):
        if a[i][j] == 1:
            empty.append((i,j))
'''
빈칸에 놓을 수 있는 종이를 모두 놓아본다 
'''

answer = 30
def go(idx, counts, filled):
    global answer
    global a
    if sum(counts) > answer:
        return
    if filled == len(empty):
        answer = min(sum(counts), answer)
        return

    x, y = empty[idx]
    if not a[x][y]:
        go(idx+1, counts, filled)
    for k in range(5, 0, -1):
        if counts[k-1] >= 5:
            continue
        if x+k-1<10 and y+k-1<10 and [a[i][y:y+k] for i in range(x, x+k)] == [[1]*k for _ in range(k)]:
            for i in range(x, x+k):
                for j in range(y, y+k):
                    a[i][j] = 0
            go(idx+1, counts[:k-1] + [counts[k-1]+1] + counts[k:], filled+(k**2))
            for i in range(x, x+k):
                for j in range(y, y+k):
                    a[i][j] = 1
    return

go(0, [0, 0, 0, 0, 0], 0)
print(answer if answer<=25 else -1)