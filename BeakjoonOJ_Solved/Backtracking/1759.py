l, c = map(int, input().split())
a = input().split()
a.sort()
j, m = 0, 0
for e in a:
    if e in ['a', 'e', 'i', 'o', 'u']:
        m += 1
    else:
        j += 1

def go(idx, candidate, jcount,jleft, mcount, mleft):
    global answer
    if 2 - jcount > jleft:
        return
    if 1 - mcount > mleft:
        return
    if l - len(candidate) > c - idx:#남은 문자 갯수보다 채워야 할 문자가 더 많은경우
        return
    if len(candidate) == l:
        if jcount >= 2 and mcount >= 1:
            answer.append(candidate)
        return

    if a[idx] in ['a', 'e', 'i', 'o', 'u']:
        go(idx + 1, candidate +[a[idx]], jcount, jleft, mcount + 1, mleft - 1)
        go(idx + 1, candidate, jcount, jleft, mcount, mleft - 1)
    else:
        go(idx + 1, candidate + [a[idx]], jcount + 1, jleft - 1, mcount, mleft)
        go(idx + 1, candidate, jcount, jleft - 1, mcount, mleft)

answer = []
go(0, [], 0, j, 0, m)
for ls in answer:
    print(''.join(ls))
