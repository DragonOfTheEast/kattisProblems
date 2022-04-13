def build(arr, queries):
    table = [[None for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            table[i][j] = arr[i] + arr[j]
    for query in queries:
        diff = float('inf')
        num = len(arr)
        for x in range(num-1, 0,-1):
            for y in range(0, x):
                if diff > abs(query-table[x][y]):
                    diff = abs(query-table[x][y])
                    ans = table[x][y]
        print('Closest sum to {0} is {1}.'.format(query, ans))
index = 1
try:
    while True:
        n = int(input())
        arr = []
        queries = []
        for _ in range(n):
            arr.append(int(input()))
        m = int(input())
        for query in range(m):
            queries.append(int(input()))
        print('Case {0}:'.format(index))
        index += 1
        build(sorted(arr), queries)
except EOFError:
    pass
