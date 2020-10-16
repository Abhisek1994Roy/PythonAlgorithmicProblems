import sys
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            l=(-1*int(str(x)[1:][::-1]))
        else:
            l=(int(str(x)[::-1]))

        if abs(l)>sys.maxsize:
            return 0
        else:
            return l


x= Solution()
print(x.reverse(1563847412))
