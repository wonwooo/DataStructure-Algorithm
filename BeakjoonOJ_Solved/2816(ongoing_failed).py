'''
일단 BFS 구현 - 실패(BFS는 여태까지 눌러온 채널을 기록할 수가 없는거같음)
완전탐색 구현 - 4**500이므로 시간초과
스페셜 저지이므로 다른 답이 나와도 괜찮으니 다시 시도해볼것
'''

n = int(input())
channels = [input() for _ in range(n)]
print(channels)
answer = []
def dfs(actions, count, current, channels):

    global answer
    if channels[0] == 'KBS1' and channels[1] == 'KBS2':
        print(count, actions, channels)
        answer.append(actions)
        return

    else:
        if count < 13:
            if current < n-1:
                dfs(actions + [1], count+1, current+1, channels)
                temp = channels[:]
                temp[current], temp[current+ 1] = temp[current+1], temp[current]
                dfs(actions + [3], count+1, current+1, temp)
            if current >= 0:
                dfs(actions + [2], count+1, current-1, channels)
                temp2 = channels[:]
                temp2[current], temp2[current-1] = temp2[current-1], temp2[current]
                dfs(actions + [4], count+1, current-1, channels)
        return

dfs([], 0, 0, channels)
print(answer)