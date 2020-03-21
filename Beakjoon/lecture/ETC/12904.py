s = input()
t = input()
while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
if s == t:
    print(1)
else:
    prin