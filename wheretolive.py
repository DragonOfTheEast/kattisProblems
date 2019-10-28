import sys
from math import floor, modf
while True:
    n = int(input())
    if n == 0:
        break
    sum_x = sum_y = 0
    for i in range(n):
        a, b = sys.stdin.readline().split()
        sum_x += int(a)
        sum_y += int(b)
    k = sum_x/n
    l = sum_y/n
    if modf(k)[0] == 0.5:
        k = floor(k)
    else:
        k = round(k)

    if modf(l)[0] == 0.5:
        l = floor(l)
    else:
        l = round(l)
    print(k,l)
