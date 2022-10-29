def sorted(arr):
    if len(arr) == 1:
        return
    temp = arr[len(arr) - 1]
    arr.pop()
    sorted(arr)
    insert(arr, temp)
    return arr


def insert(arr, temp):
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:
        arr.append(temp)
        return

    val = arr[len(arr) - 1]
    arr.pop()
    insert(arr, temp)
    arr.append(val)


arr = [2, 3, 4, 1, 5]
print(sorted(arr))
