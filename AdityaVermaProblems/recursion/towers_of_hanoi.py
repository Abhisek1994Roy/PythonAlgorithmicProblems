# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
n = int(line)

s = "A"
h = "C"
d = "B"
g = n


def solve(s, d, h, n, g):
    if n == 1:
        print("Moving ring " + str(n) + " from " + s + " to " + d)
        return
    solve(s, h, d, n - 1, g)
    print("Moving ring " + str(n) + " from " + s + " to " + d)
    solve(h, d, s, n - 1, g)
    return


solve(s, d, h, n, g)
