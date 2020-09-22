while True:
    n = int(input()) 

    if n == -1:
        break
    arr = []

    for i in range(n):
        temp = [int(j) for j in input().split()]
        arr.append(temp)
        
    for i in range(n):
        isWeak = True 
        for j in range(n):
            for k in range(n):
                if i == k or i == j or j == k:
                    continue
                if arr[i][j] == 1 and arr[i][k]==1 and arr[j][k] == 1:
                    isWeak = False
                    break
        if isWeak:
            print(i, end= " ")


    print()
