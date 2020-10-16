def trailing_zeros(manipulandum):
    return len(manipulandum)-len(manipulandum.rstrip('0'))

def maximumPower(s):
    if s.find("1") == -1:
        return -1
    big_pow = 0
    pow = 0
    for index in range(0, len(s)):
        if (s[index:]+s[:index]).endswith("0"):
            pow = trailing_zeros(s[index:]+s[:index])
            if pow>big_pow:
                big_pow =pow
    if pow>big_pow:
        return pow
    else:
        return big_pow

print(maximumPower("11100000001110101"))
