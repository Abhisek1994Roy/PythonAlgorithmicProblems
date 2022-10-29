j = []


def print_number(n):
    if n < 1:
        return

    # recursively call the printNumber function
    print_number(n - 1)
    # print n
    j.append(n)
    return j


# declare the value of n
n = 3
# call the printNumber function
print(print_number(n))
