r, c, zr, zc = [int(i) for i in input().split()]


def my_split(string):
    return [i for i in string]

ret = [[0 for j in range(c*zc)] for i in range(zr*r)]


ret[0][0] = 1
ret[0][1] = 1

for i in range(r):
    line = my_split(input())
    for char in range(c):
        for k in range(i*zr, i*zr+zr):
            for j in range(char*zc, char*zc+zc):
                ret[k][j] = line[char]


for i in ret:
    for j in i:
        print(j, end="")
    print()