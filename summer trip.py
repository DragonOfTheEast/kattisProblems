a = input()

ans = []
for i in range(len(a) - 1):
    temp = a[i]
    for j in range(i+1, len(a)):
        if temp[0] == a[j]:
            break
        if a[j] not in temp:
            temp += a[j]
            ans.append(temp)
        else:
            temp += a[j]
            continue



print(len(ans))
