import math
def gcd(i,j):
    print(i,j)
    if (j == 0):
        return i
    return gcd(j, i%j)

def _lcm(arr):
    lcm = arr[0]
    for i in arr[1:]:
        lcm = (i * lcm) // gcd(i, lcm)
    return int(lcm) if lcm <= 10**9 else "More than a billion."

n = int(input())
for i in range(n):
    _ = input()
    ps = [int(i) for i in input().split()]
    print(_lcm(ps))

