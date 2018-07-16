#Given a random array, check if array is sorted using recursion.
print("Enter array elements")
user_input=input()
user_array=user_input.split(" ")

def is_array_sorted(user_array):
    if len(user_array)==1:
        return(True)
    return(user_array[0] <= user_array[1] and is_array_sorted(user_array[1:]))

print(is_array_sorted(user_array))
