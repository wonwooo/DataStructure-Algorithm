def calc(i, s): #s 가 101 이라는건 받아들이는 블럭의 형태가 101 형태여야 높이가 균일하다는 의미.
    if i+len(s) > n:
        return 0
    base = a[i] - (ord(s[0]) - ord('0'))
    for j in range(len(s)):
        if base != a[i+j] - (ord(s[j])-ord('0')):
            return 0
    return 1

n,m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
    if m == 1:
        ans += calc(i, '0') + calc(i, '0000')
    elif m == 2:
        ans += calc(i, '00')
    elif m == 3:
        ans += calc(i, '001') + calc(i, '10')
    elif m == 4:
        ans += calc(i, '100') + calc(i, '01')
    elif m == 5:
        ans += calc(i, '000') + calc(i, '101') + calc(i, '10') + calc(i,'01')
    elif m == 6:
        ans += calc(i, '000') + calc(i, '00') + calc(i, '011') + calc(i, '20')
    elif m == 7:
        ans += calc(i, '000') + calc(i, '02') + calc(i, '00') + calc(i, '110')

print(ans)





