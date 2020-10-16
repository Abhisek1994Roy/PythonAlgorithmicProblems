import math

def highestPowerOf2(n):
    return (n & (~(n - 1)))

def trailing_zeros(num):
    manipulandum = num
    return len(manipulandum)-len(manipulandum.rstrip('0'))

def maximumPower(s):
    if s.find("1") == -1:
        return -1
    big_pow = 0
    pow = 0
    v = s.split("1")
    for index in range(0, len(s)):
        if (s[index:]+s[:index]).endswith("0"):
            pow = trailing_zeros(s[index:]+s[:index])
            if pow>big_pow:
                big_pow =pow
    if pow>big_pow:
        return pow
    else:
        return big_pow

print(maximumPower("10000000100"))
