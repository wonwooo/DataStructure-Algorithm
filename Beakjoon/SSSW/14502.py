#완전 탐색
'''
1. 벽을 선택한다.
2. 바이러스를 퍼트린다.
3. 바이러스가 퍼지지 않은 안전지역 면적을 구한다.

1~3번의 과정을 벽을 선택하는 모든 경우의 수에 대해서 반복하고,
마지막에 안전지역의 max값 리턴
'''

import copy
import sys


N, M = map(int, input().strip().split())
NM = []
for i in range(N):
    L = list(map(int, input().strip().split()))
    NM.append(L)

dr = [-1, 0, 1, 0] #위아래 row단위 이동
dc = [0, 1, 0, -1] #좌우 column이동

max_value = 0 #clean 지역의 갯수를 return 하기위한 변수
virus_list = [] #NM의 2의 위치만 가져와서 virus위치가 있는 list만들기
for i in range(N):
    for j in range(M):
        if NM[i][j] == 2:
            virus_list.append([i,j])


#벽 선택하기
def select_wall(start, count):
    global max_value
    if count == 3: #종료조건, 벽 3개 선택
        sel_NM = copy.deepcopy(NM)
        for r in range(N):
            for c in range(M):
                spread_virus(r, c, sel_NM)
        '''
        for r, c in virus_list:
            spread_virus(r, c, sel_NM)
        이렇게 하면 시간 단축가능
        '''
        safe_counts = sum(i.count(0) for i in sel_NM) #clean지역 count
        max_value = max(max_value, safe_counts)
        return True

    else: #start 값이 N*M이 되면 loop는 자연스럽게 돌지 못하고 함수가 끝남

        for i in range(start, N*M): #2차원 배열에서 조합 구하기
            r = i // M #나눈 몫은 row(위아래) 좌표
            c = i % M #나는 나머지가 column(좌우) 좌표
            if NM[r][c] == 0: #벽 없으면
                NM[r][c] = 1 #벽으로 고정하고
                select_wall(i, count+1) #다음 벽 세우기위해 재귀
                NM[r][c] = 0 #conut == 3이 되어서, 개수 세고 return True받으면, 벽 없애고 다음 원소에 벽세우기 위해 진행

def spread_virus(r, c, sel_NM):
    if sel_NM[r][c] == 2: #바이러스를 기준으로
        #상하좌우 4방향을 확인하고 범위를 벗어나거나 벽을 만날때까지 반복
        for dir in range(4):
            n_r = r + dr[dir] #상하이동[하(1), 상(-1), 상하이동없음(0) 중 하나]
            n_c = c + dc[dir] #좌우이동[우(1), 좌(-1), 좌우이동없음(0) 중 하나]
            if n_r >= 0 and n_c >= 0 and n_r < N and n_c < M: #2차원 배열 내에서
                if sel_NM[n_r][n_c] == 0:
                    sel_NM[n_r][n_c] = 2
                    spread_virus(n_r, n_c, sel_NM)



select_wall(0,0)
print(max_value)


