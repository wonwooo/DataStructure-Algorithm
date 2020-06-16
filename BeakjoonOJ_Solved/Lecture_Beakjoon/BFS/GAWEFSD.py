
def check(start, end, gems):
    if set(gems[start:end]) == set(gems):
        return True
    else:
        return False

def solution(gems):
    N = len(gems)
    answer = []
    for i in range((len(gems)//2)+1):
        start = i
        end = len(gems)
        minlen = len(gems)
        result = -1
        while start <= end:
            mid = (start + end) // 2
            if check(i, mid, gems):
                result = mid

                end = mid-1
            else:
                start = mid+1
        if result != -1:
            answer.append((i+1, result))
    mindist = min([ j - i for (i, j) in answer])
    res = [(x, y)  for (x, y) in answer if y-x == mindist]
    res.sort()
    return list(res[0])
