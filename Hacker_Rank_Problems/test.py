import collections

def check_order(arr):
    if len(arr)==len(set(arr)):
        return True
    else:
        return False

def count_frequency(arr):
    return collections.Counter(arr)

def whoIsTheWinner(arr):
    if check_order(arr):
        return "First"
    arr_freq = count_frequency(arr)
    singles = 0
    multiples = 0
    for i in arr_freq:
        if arr_freq[i]>1:
            multiples +=arr_freq[i]
        else:
            singles+=1
    start = True
    if singles%2==0:
        start = not start
    if multiples%2!=0:
        start = not start
    if start == True:
        return "First"
    else:
        return "Second"

# print(whoIsTheWinner([1,2,3,4,4,5,5,5,6,6,6,7]))
# print(whoIsTheWinner([1,2,3,4,4,5,5,5,6,6,7]))
# print(whoIsTheWinner([1,2,3,7]))
# print(whoIsTheWinner([1,2,3,3,7]))
print(whoIsTheWinner([1,2,2,3]))
