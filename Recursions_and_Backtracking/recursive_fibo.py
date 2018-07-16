print("Enter the position of the fibonacci number that you want")
n = int(input())
a = 1
b = 1
def find_fibo(a,b,n):
    print(a,b,n)
    if n==0:
        return(a)
    if n!=0:
        return(find_fibo(b+a,a,n-1))
if n==1:
    print(0)
elif n==2:
    print(1)
else:
    x=(find_fibo(a,b,n-3))
    print(x)
