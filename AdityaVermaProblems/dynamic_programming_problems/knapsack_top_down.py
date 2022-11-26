def knapsack(wt, val, W):
    arr = [[0 for i in range(W + 1)] for j in range(len(val) + 1)]
    for i in range(1, len(val) + 1):
        for j in range(1, W + 1):
            if wt[i - 1] > W:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = max(val[i - 1] + arr[i - 1][j - wt[i - 1]], arr[i - 1][j])
    return arr


val = [60, 100, 120]
wt = [1, 2, 3]
W = 5
print(knapsack(wt, val, W)[-1][-1])
