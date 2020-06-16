'''
python은 pass하는 변수에 따라서 call by value / call by reference 가 달라진다는 사실을 몰라서
헷갈렸던 문제
a = 10, b = a 처럼 int를 전달하면 int는 immutable 객체이기 때문에 call by value가 적용되어서 b의 값이 바뀌어도 a는 바뀌지 않는다
immutable : int, str
mutable : list, dict
'''


a = int(input())
n = a
count = 1
while True:
    if int(n) < 10:
        new = n + n
    else:
        s = int(n[0]) + int(n[1])
        if n[1] == '0':
            new = str(s % 10)
        else:
            new = n[1] + str(s%10)
    if int(new) == a:
        break
    count += 1
    n = new

print(count)
