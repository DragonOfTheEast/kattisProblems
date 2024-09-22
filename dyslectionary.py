
arr = []
longest = 0
first = True
while True:
    try:
        temp = input()
    except EOFError as e :
        break
    if temp == '':
        arr = sorted(arr, key=lambda k: (k, len(k)))
        for i in arr:
            print(i[::-1].rjust(longest))
        arr.clear()
        longest = 0
        print()
    else:
        if len(temp) > longest:
            longest = len(temp)
        arr.append(temp[::-1])


arr = sorted(arr, key=lambda k: (k, len(k)))
for i in arr:
    print(i[::-1].rjust(longest))
