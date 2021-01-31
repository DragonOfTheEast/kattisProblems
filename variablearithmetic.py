store = {}

import  sys

for line in sys.stdin.readlines():
    if line == "0":
        break
    temp = line.split()
    if len(temp) == 3 and temp[1] == "=":
        store[temp[0]] = int(temp[2])
        #print(temp)
        continue
    value = [0]
    for i in temp:
        if i == "+":
            continue
        if i.isdigit() is True or i in store:
            if i.isdigit() is False:
                val = store[i]
            else:
                val = int(i)
            value[0] += val
        else:
            value.append(i)
    print(" + ".join([str(j) for j in value if j != 0]))