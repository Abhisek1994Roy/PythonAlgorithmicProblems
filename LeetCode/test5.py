import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        k = re.match("^[-+]?\d+",s)
        if k is not None:
            mm=k.group(0)
        else:
            return 0

        if mm != "":
            if int(mm) < -2147483647:
                return -2147483647
            elif int(mm) > 2147483647:
                return 2147483647
            else:
                return int(k.group(0))
        else:
            return 0
        return(k)

x=Solution()
print(x.myAtoi(" -112asd words and 987"))
