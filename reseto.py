n, k = [int(i) for i in input().split()]
temp = [0, 0]


arr = [i for i in range(2, n+1)]
arr = temp + arr
i = 0

count = 0
while count < k:
    for i in range(len(arr)):
        if arr[i] != 0:
            start = i
            break
    arr[start] = 0
    count += 1
    if count == k :
        ans = start
        break
    mult = 1
    while start * mult <= n and count < k:
        if arr[start * mult] != 0:
            count += 1
            if count == k:
                ans = start*mult
        arr[start * mult] = 0
        mult += 1


print(ans)


