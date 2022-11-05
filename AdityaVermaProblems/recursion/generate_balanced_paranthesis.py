def subset(open, close, s, arr):
    if open == 0 and close == 0:
        if s not in arr:
            arr.append(s)
        return
    if open > 0 and close > 0:
        if close == open:
            open = open - 1
            s += "("
            subset(open, close, s, arr)
        subset(open - 1, close, s + "(", arr)
        subset(open, close - 1, s + ")", arr)
    elif close > 0:
        subset(open, close - 1, s + ")", arr)

    return arr


open = 4
close = 4
s = ""
arr = []
print(subset(open, close, s, arr))
