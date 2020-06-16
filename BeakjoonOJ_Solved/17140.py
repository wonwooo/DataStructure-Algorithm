r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]


def arrange(lst):
    lst = [e for e in lst if e!=0]
    numToCount = {}
    countToNum = {}
    for e in lst:
        if e not in numToCount:
            numToCount[e] = 1
        else:
            numToCount[e] += 1
    for k, v in numToCount.items():
        if v not in countToNum:
            countToNum[v] = [k]
        else:
            countToNum[v].append(k)
    counts = sorted(countToNum.keys())
    result = []
    for count in counts:
        for number in sorted(countToNum[count]):
            result += [number, count]
    return result, len(result)


def performR(arr):
    for i in range(len(arr)):
        arr[i] , length = arrange(arr[i])
        if i == 0:
            maxlength = length
        else:
            if length > maxlength:
                maxlength = length
    for i in range(len(arr)):
        arr[i] = arr[i] + [0]*(maxlength - len(arr[i]))

    return arr

count = 0
while True:
    if len(a) >=r and len(a[0]) >= c and a[r-1][c-1] == k:
        break
    if count == 100:
        count = -1
        break
    rnum = len(a)
    cnum = len(a[0])
    if rnum >= cnum:
        a = performR(a)
    else:
        a = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
        a = performR(a)
        a = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
    if len(a) >= 100:
        a = a[:100]
    if len(a[0]) >= 100:
        a = [row[:100] for row in a]
    count += 1

print(count)