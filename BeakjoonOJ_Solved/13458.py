n = int(input())
nums = list(map(int, input().split()))
b, c = map(int, input().split())
e = [0]*n
for i in range(n):
    nums[i] -= b
    e[i] += 1
for i in range(n):
    if nums[i] <=0:
        continue
    if nums[i] % c == 0:
        e[i] += nums[i]//c
    else:
        e[i] += nums[i]//c + 1

print(sum(e))

