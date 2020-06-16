colors, num_count  = {'R':0, 'B':0, 'Y':0, 'G':0}, {i:0 for i in range(1, 10)}
values = []
for i in range(5):
    c, n = input().split()
    colors[c] += 1
    num_count[int(n)] += 1
    values.append(int(n))

count_num = {}
for k, v in num_count.items():
    if v not in count_num:
        count_num[v] = [k]
    else:
        count_num[v].append(k)


def straight(list):
    m = min(list)
    if sorted(list) == [i for i in range(m, m+5)]:
        return True
    else:
        return False

if 5 in colors.values():
    if straight(values):
        score = max(values) + 900
    else:
        score = max(values) + 600

else:
    if 4 in count_num:
        score = count_num[4][0] + 800
    elif 3 in count_num:
        if 2 in count_num:
            score = count_num[3][0]*10 + count_num[2][0] + 700
        else:
            score = count_num[3][0] + 400
    elif 2 in count_num:
        if len(count_num[2]) == 2:
            score = max(count_num[2])*10 + min(count_num[2]) + 300
        else:
            score = count_num[2][0] + 200

    elif straight(values):
        score = max(values) + 500

    else:
        score = max(values) + 100

print(score)






