s = input()
t = input()
S = s
T = t
while len(S) != len(T):
    if len(S) < len(T):
        S += s
    else:
        T += t
if S == T:
    print(1)
else:
    print(0)