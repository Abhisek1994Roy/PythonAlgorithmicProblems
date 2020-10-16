import math

def maximumPower(s):
    if s.find("1") == -1:
        return -1
    m = s.index("1")
    s=s[m:]+s[:m]
    count = 0
    c=0
    for i in s:
        if i == "0":
            c+=1
        else:
            if c>count:
                count = c
            c=0
    if c>count:
        return c
    else:
        return count
print(maximumPower("01010101010"))
