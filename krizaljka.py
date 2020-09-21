a, b = input().split()
stop = False
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            index = i
            index_2 = j
            stop = True
            break
    if stop is True:
        break

ret = [['.' for i in range(len(a))] for j in range(len(b))]

for i in range(len(a)):
    ret[index_2][i] = a[i]

for i in range(len(b)):
    ret[i][index] = b[i]


for i in ret:
    print("".join(i))

