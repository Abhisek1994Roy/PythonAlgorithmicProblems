
def generate(numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    row = []
    arr = generate(numRows - 1)
    for i in range(numRows):
        if i == 0 or i == numRows - 1:
            row.append(1)
        else:
            row.append(arr[-1][i - 1] + arr[-1][i])
    arr.append(row)

    return arr



print(generate(5))