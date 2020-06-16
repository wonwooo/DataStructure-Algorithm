data = [1,2,3,4,5]
start = 0
end = 0
m = 5
n = len(data)
summary = 0

sets = []
for start in range(n):
    while summary < m and end < n:
        summary += data[end]
        end += 1
    if summary == m:

        sets.append(data[start:end])
    summary -= data[start]

print(sets)