def reverse_sorted(arr):
    if len(arr) == 1:
        return
    temp = arr.pop()
    reverse_sorted(arr)
    insert(arr, temp)
    return arr


def insert(arr, temp):
    if len(arr) == 0 or arr[-1] > temp:
        arr.append(temp)
        return

    val = arr.pop()

    insert(arr, temp)
    arr.append(val)


arr = [2, 3, 4, 1, 5]
print(reverse_sorted(arr))
