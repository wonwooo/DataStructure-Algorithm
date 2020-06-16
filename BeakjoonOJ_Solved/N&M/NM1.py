n, m = map(int, input().split())
answer = []
def combination(idx, comb, n, m):
    global answer
    if len(comb) == m:
        answer.append(comb)
        return

    if idx <= n:
        combination(idx+1, comb + [idx], n, m)
        combination(idx+1, comb, n, m)
    return

def permutation(lst, n):
    result = []
    if len(lst) < n:
        return result
    if n == 1:
        for e in lst:
            result.append([e])
        return result

    for k in lst:
        temp = lst[:]
        temp.remove(k)
        for perm in permutation(temp, n-1):
            result.append([k]+perm)
    return result

answer = permutation([i for i in range(1, n+1)], m)
answer.sort()
for l in answer:
    print(' '.join(map(str, l)))
