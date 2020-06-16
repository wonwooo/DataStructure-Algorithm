'''
Brute-Force
부분 삼각형의 갯수가 많지 않기때문에, 다 만들어본다
삼각형에 좌표를 매긴다. (r, c)에서 c가 홀수면 정, 짝수면 역삼각형
모든 단위 삼각형을 시작으로 모든 부분 삼각형을 만들어본다
정삼각형과 역삼각형의 2가지케이스로 나누어서 구현하는데, 두가지 각각 좌표상의 특징이 있음을 발견해야한다.

'''
def calc(row, left, right, sum):
    print(row, left, right, sum)
    if row < 1 or row > n:
        return
    if left < 1 or right > 2*row-1:
        return
    sum += s[row][right] - s[row][left-1]
    global ans
    if sum > ans:
        ans = sum
    if left % 2 == 0:
        calc(row-1, left-2, right, sum)
    else:
        calc(row+1, left, right+2, sum)
tc = 0
while True:
    tc += 1
    inputs = list(map(int,input().split()))
    n = inputs[0]
    if n == 0:
        break
    ans = -100000
    a = [[]]
    s = [[]]#누적합 ; 기타 chapter 구간합 구하기 4번 참고.
    k = 1
    for i in range(1, n+1):
        a.append([0]*(2*i))
        s.append([0]*(2*i))
        for j in range(1, 2*i):
            a[i][j] = inputs[k]
            k += 1
            s[i][j] = s[i][j-1] + a[i][j]
    # 모든 삼각형에 대해서
    for i in range(1, n+1):
        for j in range(1, 2*i):
            calc(i,j,j,0)
    print(str(tc)+'. '+str(ans))
