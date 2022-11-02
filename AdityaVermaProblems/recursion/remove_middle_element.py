def remove_middle_element(arr, j):
    if len(arr) == 0:
        return arr
    if j == 1:
        arr.pop()
        return
    g = arr.pop()
    remove_middle_element(arr, j-1)
    arr.append(g)
    return arr


arr = [1, 2, 3, 4, 5, 6]
j = len(arr) // 2 + 1

f = remove_middle_element(arr, j)
print(f)
