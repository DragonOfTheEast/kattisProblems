import sys

def is_safe(arr, temp):
    seen = set()
    seen.add(temp)
    return dfs(seen, temp, arr)

def dfs(seen, temp, arr):
    # if temp in list1:
    #     return list1[temp]
    if temp in arr.keys():
        for i in arr[temp]:
            if i in seen or dfs(seen.union({i}), i, arr):
                #list1[i] = True
                return True
    #list1[temp] = False
    return False
arr = dict()
file1 = list()
for line in sys.stdin.readlines():
    file1.append(line.strip())
n = int(file1[0])
for i in range(1, n+1):
    a,b = file1[i].split()
    if a not in arr.keys():
        arr[a] = list()
        arr[a].append(b)
    else:
        arr[a].append(b)
list1 = list(arr.keys())
for i in range(n+1, len(file1)):
    temp = file1[i]
    if temp in arr.keys():
        index = list1.index(temp)
        if is_safe(arr, temp) == True:
            print(temp + " safe")
        else:
            print(temp + " trapped" )
    elif temp not in arr.keys():
        print(temp + " trapped")
