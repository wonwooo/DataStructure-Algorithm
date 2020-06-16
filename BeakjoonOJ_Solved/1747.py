def prime(n):
    if n == 1:
        return False
    result = True
    i = 2
    while True:
        if i**2 > n:
            break
        if n % i == 0:
            result = False
            break
        i += 1
    return result

def palindrome(n):

    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return palindrome(n[1:-1])
    else:
        return False

n = int(input())
answer = n
while True:
    if prime(answer) and palindrome(str(answer)):
        break
    answer += 1

print(answer)