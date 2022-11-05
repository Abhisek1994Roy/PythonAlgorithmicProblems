def generate_bin(s, n, arr):
    if n == 0:
        arr.append(s)
        return
    if s.count('1') > s.count('0'):
        s1 = s + "0"
        s2 = s + "1"
        generate_bin(s1, n - 1, arr)
        generate_bin(s2, n - 1, arr)
    if s.count('1') == s.count('0'):
        generate_bin(s+"1", n - 1, arr)
    return arr


n = 5
s = ""
arr = []
print(generate_bin(s, n, arr))
