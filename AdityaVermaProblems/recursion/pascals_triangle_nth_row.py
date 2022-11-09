def getRow(numRows):
    if numRows == 0: return [1]
    row = []
    arr = getRow(numRows - 1)
    for i in range(numRows + 1):
        if i == 0 or i == numRows:
            row.append(1)
        else:
            row.append(arr[i - 1] + arr[i])
    return row

print(getRow(5))