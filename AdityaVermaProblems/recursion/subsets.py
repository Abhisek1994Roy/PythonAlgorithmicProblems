def subset(ip, op):
    if ip == "":
        print(op)
        return
    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]
    subset(ip, op1)
    subset(ip, op2)
    return

subset("abc", "")
