'''
모든 가짓수가 2^20 이하이므로 Brute Force
구현해야 하는 것 : N명의 사람이 1팀, 2팀에 속하는 경우를 모두 구현해야함
재쉬함수 구현 시에 호출이 끝나면 원래대로 돌려놓는 것 중요
'''

def go(index, first, second):
    if index == n: #n번째 사람까지 왔다는 뜻. 모두 팀 배정을 마쳤다는 뜻이므로 탈출
        if len(first) == 0:
            return -1
        if len(second) == 0:
            return -1
        t1 = 0
        t2 = 0
        for p1 in first:
            for p2 in first:
                if p1 == p2:
                    continue
                t1 += s[p1][p2]
        for p1 in second:
            for p2 in second:
                if p1 == p2:
                    continue
                t2 += s[p1][p2]
        diff = abs(t1-t2)
        return diff

    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 !=-1 and ans > t1):
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 !=-1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))