class Solution:
    def find_longest_palin(self, s, start, end):
        while end<len(s) and start>=0:
            if s[start] != s[end]:
                return s[start+1:end]
            else:
                pal = s[start:end+1]
            start = start-1
            end = end+1
        return pal

    def longestPalindrome(self, s: str) -> str:
        longest_palin = s[0]
        index=0
        while index<len(s):

            print("index is-"+str(index))
            if index+1<len(s) and s[index-1] == s[index+1] and index>0 :
                print("a palin =>")
                print(index-1, index+1)
                palin = self.find_longest_palin(s, index-1, index+1)
                print(palin)
                if len(palin)>len(longest_palin):
                    longest_palin=palin
            if s[index-1] == s[index] and index>0:
                print("b palin =>")
                print(index-1,index)
                palin= self.find_longest_palin(s, index-1,index)
                print(palin)
                if len(palin)>len(longest_palin):
                    longest_palin=palin
                print(longest_palin)
            index = index+1

        return longest_palin

x= Solution()
# print(x.longestPalindrome("aaaa"))
# print(x.longestPalindrome("b"))
# print(x.longestPalindrome("ccc"))
# print(x.longestPalindrome("dddddddde"))
# print(x.longestPalindrome("rrryyxltlxyyzzvvvvzz"))
print(x.longestPalindrome("cbbd"))
