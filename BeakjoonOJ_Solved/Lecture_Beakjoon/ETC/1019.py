ans = [0]*10
def calc(n, ten):
    while n > 0:
        ans[n%10] += ten
        n //= 10
start = 1
end = int(input())
ten = 1
while start <= end:
    while start%10 != 0 and start <= end:
        calc(start, ten)
        start += 1
    if start > end:
        break
    while end % 10 != 9 and start <= end:
        calc(end, ten)
        end -= 1
    cnt = (end//10 - start//10 + 1)
    for i in range(10):
        ans[i] += cnt*ten
    start //= 10
    end //= 10
    ten *= 10
print(' '.join(map(str,ans)))