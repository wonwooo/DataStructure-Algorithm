def FibonacciDP(n):
    #setting up a memoization table
    dicFibonacci = {}
    dicFibonacci[0] = 0
    dicFibonacci[1] = 1
    #building up a bigger solutions
    for itr in range(2, n + 1):
        dicFibonacci[itr] = dicFibonacci[itr-1] + dicFibonacci[itr-2]
    return dicFibonacci[n]

for itr in range(0, 10):
    print(FibonacciDP(itr), end=" ")
