#Reverse a string using recursive technique
#Write a recursive function to reverse a string. Write a recursive
#function to reverse the words in a string, i.e., "cat is running"
#becomes "running is cat".

print("Enter your string")
words= input()
final_string=[]
str=""
def reverse(words,str=""):
    if (len(words)==0):
        final_string.append(str)
        return()
    if words[-1] == " ":
        final_string.append(str)
        str=""
        reverse(words[:-1])
    else:
        str = words[-1] + str
        words = words[:-1]
        reverse(words, str)

reverse(words, str)
print(" ".join(final_string))
