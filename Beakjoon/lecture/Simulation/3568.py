s = input()
a = []
now = ''
for x in s:
    if x in ' ,;':
        if now:
            a.append(now)
        now = ''
    else:
        now += x
base = a[0]
for i in range(1, len(a)):
    t = base
    s = list(a[i])
    while s and not('a' <= s[-1] <= 'z'):
        if s[-1] == '[':
            t += ']'
        elif s[-1] == ']':
            t += '['
        else:
            t += s[-1]
        s.pop()
    print(t + ' ' + ''.join(s) + ';')
