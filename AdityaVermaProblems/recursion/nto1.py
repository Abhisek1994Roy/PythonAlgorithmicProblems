def reverse_print(n):
    if n == 1:
        print(n, end=' ')
        return
    print(n, end=' ')
    reverse_print(n - 1)


reverse_print(5)
