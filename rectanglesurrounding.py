while True:
    n = int(input())
    if n == 0:
        break
    tot = 0
    graph = [[0 for i in range(501)] for i in range(501)]
    for _ in range(n):
        x1, y1, x2, y2 = [int(i) for i in input().split()]
        for i in range(x1, x2):
            for j in range(y1, y2):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    tot += 1
    print(tot)


