'''
14890 경사로
구현 할 때 경우를 잘 나누어야 반복문을 최대한 짧게 구현할 수 있다.
지나치게 조건이 많아진다면 의심해 볼 것
'''

def go(a, l):
    n = len(a)
    c = [False] * n
    #해당 칸에 경사로를 놓았는지 확인하는 배열. 나는 구현 안해서 틀렸던 것 같다.
    for i in range(1, n): #0번째 칸은 무조건 가능
        if a[i-1] != a[i]: #한 칸씩 탐색 하면서 다른 높이가 나왔을 때에 조건문을 시작하는 게 중요
            diff = abs(a[i] - a[i-1])
            if diff != 1:
                return False
            if a[i-1] < a[i]:
                for j in range(1, l+1):#높이가 다르면 역으로 탐색 해 가면서 l개 높이가 같은지
                    if i-j < 0: #l개 놓을 자리도 없으면
                        return False
                    if a[i-1] != a[i-j]:
                        return False
                    if c[i-j]:
                        return False
                    c[i-j] = True # True처리하고 넘어간다
            else: #낮은 칸으로 가는 경우
                for j in range(0,l):
                    if i+j >= n: #현재 index가 i면 i+j는 j를 더했을 때의 index이므로 n-1보다 크면 안됨
                        return False
                    if a[i] != a[i+j]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True


n,l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    d = a[i]
    if go(d, l):
        ans += 1
for j in range(n):
    d = [a[i][j] for i in range(n)]
    if go(d, l):
        ans += 1
print(ans)



