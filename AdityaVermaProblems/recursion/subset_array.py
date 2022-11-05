def subset(ip, op, arr):
    if len(ip) == 0:
        op3 = list(sorted(list(op)))
        if op3 not in arr:
            arr.append(op3)
        return arr
    op1 = op
    op2 = op + [ip[0]]
    ip = ip[1:]
    subset(ip, op1, arr)
    subset(ip, op2, arr)
    return arr



ip = [1, 2]
op = []
arr = []
k =subset(ip, op, arr)
print(k)
