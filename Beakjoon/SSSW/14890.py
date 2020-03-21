def blnTest(road, L):
    record = []
    decision = True

    for i in range(len(road)):
        if i == 0:
            record.append((road[i], i))
        if 1 <= i < len(road) - 1:
            if road[i] == road[i - 1]:
                pass
            if road[i] > road[i - 1]:
                if road[i] - road[i - 1] == 1:

                    if len(record) == 1:
                        if i - record[0][1] >= L:
                            record.append((road[i], i))

                        else:
                            decision = False
                            break
                    else:
                        last = record[-1]
                        beforeLast = record[-2]
                        if last[0] < beforeLast[0]:
                            if i - last[1] >= 2 * L:
                                record.append((road[i], i))

                            else:
                                decision = False
                                break
                        elif last[0] > beforeLast[0]:
                            if i - last[1] >= L:
                                record.append((road[i], i))

                            else:
                                decision = False
                                break
                else:
                    decision = False
                    break

            if road[i] < road[i - 1]:
                if road[i - 1] - road[i] == 1:
                    if len(record) == 1:
                        record.append((road[i], i))


                    else:
                        beforeLast = record[-2]
                        last = record[-1]
                        if beforeLast[0] > last[0]:
                            if i - last[1] >= L:
                                record.append((road[i], i))

                            else:
                                decision = False
                                break
                        elif beforeLast[0] < last[0]:
                            record.append((road[i], i))

        if i == len(road) - 1:
            if road[i] == road[i - 1]:

                if len(record) == 1:
                    pass
                else:
                    current = record[-1]
                    last = record[-2]
                    if road[i] > last[0]:
                        pass
                    elif road[i] < last[0]:
                        if i - current[1] + 1 >= L:
                            pass
                        else:
                            decision = False
                            break

            elif road[i] > road[i - 1]:

                if road[i] - road[i - 1] == 1:
                    if len(record) == 1:
                        if i - record[-1][1] >= L:
                            pass
                    else:
                        last = record[-1]
                        beforeLast = record[-2]
                        if last[0] > beforeLast[0]:
                            if i - last[1] >= L:
                                pass
                            else:
                                decision = False
                                break
                        elif last[0] < beforeLast[0]:
                            if i - last[1] >= 2 * L:
                                pass
                            else:
                                decision = False
                                break
                else:
                    decision = False
                    break

            elif road[i] < road[i - 1]:

                if road[i - 1] - road[i] == 1:
                    if L == 1:

                        pass
                    else:
                        decision = False
                        break
                else:
                    decision = False
                    break

    return decision


N, L = map(int, input().split())
roadList = [list(map(int, input().split())) for i in range(N)]
cnt = 0
for roadHorizontal in roadList:
    if blnTest(roadHorizontal, L):
        # print(roadHorizontal, 'pass')
        cnt += 1

for c in range(N):
    roadVertical = [roadList[i][c] for i in range(N)]

    if blnTest(roadVertical, L):
        # print(roadVertical, 'pass')
        cnt += 1

print(cnt)

