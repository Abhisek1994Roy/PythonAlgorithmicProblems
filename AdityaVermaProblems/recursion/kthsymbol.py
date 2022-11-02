def ksymbol(n, k):
    if n == 1 and k == 1:
        return "0"
    if k <= (2**(n-1))//2:
        return ksymbol(n - 1, k)
    else:
        return ksymbol(n - 1, k - (2**(n-1))//2).translate(str.maketrans("01", "10"))


print(ksymbol(3, 2))
