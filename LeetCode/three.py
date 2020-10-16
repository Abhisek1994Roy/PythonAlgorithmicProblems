
def lengthOfLongestSubstring(s):
    substring = []
    longest_substring = []
    for element in range(0, len(s)):
        print("-----")
        print(element)
        if s[element] not in substring:
            print("s element "+s[element])
            print("substring element "+str(substring))
            substring.append(s[element])
        else:
            if len(substring) >= len(longest_substring):
                longest_substring=substring
            print("****")
            print(substring.index(s[element]))
            substring=substring[(substring.index(s[element]))+1:]
            substring.append(s[element])

            print(substring)
            print("****")
        print(substring)
        print(longest_substring)
    if len(substring)>len(longest_substring):
        longest_substring=substring
    return(len(longest_substring))


print(lengthOfLongestSubstring("hkcpmprxxxqw"))
