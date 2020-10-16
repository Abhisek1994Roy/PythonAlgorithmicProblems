class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x%10)
        if(x < 0 or (x % 10 == 0 and x != 0)) :
            print("Here")
            return False

        c=0
        while x>c:
            c=c*10+x%10
            x=x//10

        if x==c//10 or x==c:
            return True
        return False

x=Solution()
print(x.isPalindrome(1))
