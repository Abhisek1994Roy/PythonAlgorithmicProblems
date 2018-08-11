#Generate all the binary strings with n bits.
def bit_strings(n):
    if n==0: return([])
    if n==1: return(["0","1"])
    return [digit + bitstring for digit in bit_strings(1) for bitstring in bit_strings(n-1)]

print(bit_strings(4))
