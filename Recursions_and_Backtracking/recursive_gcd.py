print("Enter the two numbers")
num = input()
nums = num.split(" ")
a, b = int(nums[0]),int(nums[1])

if b < a:
    a = a + b
    b = a - b
    a = a - b

print(a, b)

def get_gcd(a, b):
    if a!=0:
        return(get_gcd(b%a,a))
    else:
        return(b)



print(get_gcd(a, b))
