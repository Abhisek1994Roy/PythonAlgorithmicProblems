def knapsack(wt, val, W):
    if len(wt)==0 or W==0:
        return 0
    if wt[-1] > W:
        return knapsack(wt[:-1], val[:-1], W)
    else:
        return max(val[-1] + knapsack(wt[:-1], val[:-1], W - wt[-1]), knapsack(wt[:-1], val[:-1], W))


val = [60, 100, 120]
wt = [1, 2, 3]
W = 5
print(knapsack(wt, val, W))
