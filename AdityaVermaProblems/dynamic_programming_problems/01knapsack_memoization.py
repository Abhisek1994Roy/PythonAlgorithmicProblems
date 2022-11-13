ww = dict()


def knapsack(wt, val, W):
    if len(wt) == 0 or W == 0:
        return 0
    if W in ww:
        return ww.get(W)
    if wt[-1] > W:
        ww[W] = knapsack(wt[:-1], val[:-1], W)
        return ww[W]
    else:
        ww[W] = max(knapsack(wt[:-1], val[:-1], W), val[-1] + knapsack(wt[:-1], val[:-1], W - wt[-1]))
        return ww[W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapsack(wt, val, W))
