'''
조합의 수를 recursion으로 구해봄
'''
import copy
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
hList = []
sList = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            hList.append((i,j))
        elif a[i][j] == 2:
            sList.append((i,j))

#폐업 할 치킨집의 수가 정해지면 거리의 최소값 구하는 재귀함수
#제거 될 치킨집의 위치 list(sRemove)를 recursion을 통해 인자로 받는다
def go(numToRemain , index, cnt, sRemain):
    print(numToRemove, index, cnt, sRemove)
    global sList, hList
    if cnt == numToRemove:

        #치킨 거리 합 return
        tmp = copy.deepcopy(sList)
        for store in sRemove:
            tmp.remove(store)
        dist = 0
        for home in hList:
            dList = []
            for store in tmp:
                d = abs(home[0] - store[0]) + abs(home[1] - store[1])
                dList.append(d)
            dist += min(dList)
        return dist
    else:

        if index == len(sList):
            return -2

    ans = -1
    temp1 = go(numToRemove, index+1, cnt+1, sRemove + [sList[index]])
    if ans > temp1:
        ans = temp1

    temp2 = go(numToRemove, index+1, cnt, sRemove)
    if temp2 >= 0:
        if ans > temp2:
            ans = temp2

    return ans




