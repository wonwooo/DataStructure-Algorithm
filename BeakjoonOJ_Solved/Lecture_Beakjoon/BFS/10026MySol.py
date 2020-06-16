'''
BFS의 방문체크는 queue에서 pop할때 말고 이웃 탐색중 queue에 집어 넣을때에 해주는 것이 시간이 더 빠르다

'''


from collections import deque
n = int(input())
a = [input() for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def connected(cur, next, blind):
    if cur == next:
        return True
    if blind:
        if cur == 'R' and next == 'G':
            return True
        elif cur == 'G' and next == 'R':
            return True

    return False


def go(blind,a):
    '''
    a[0][0]부터 bfs
    '''
    ans = 0
    visited  = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            ans += 1
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            while q:
                x, y = q.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny] and connected(a[x][y], a[nx][ny], blind):
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return ans


print(go(False, a),go(True, a))