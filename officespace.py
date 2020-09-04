def please_work(grid, orders):
    contested = 0
    unallocated = 0
    for i in orders:
        for y in range(orders[i][1], orders[i][3]):
            for x in range(orders[i][0], orders[i][2]):
                if grid[y][x] == "free":
                    grid[y][x] = i
                else:
                    if grid[y][x] != "contested":
                        contested += 1
                    grid[y][x] = "contested"

    for i in grid:
        for j in i :
            if j == "free":
                unallocated += 1
            if j != "free" and j != "contested" and j in orders:
                orders[j][4] += 1
    return contested, unallocated


try:
   while(True):
       size_x, size_y = [int(i) for i in input().split()]
       grid = [["free" for x in range(size_x)] for y in range(size_y)]
       n = int(input())
       orders = {}
       for i in range(n):
           line = input().split()
           orders[line[0]] = []
           orders[line[0]] = [int(j) for j in line[1:]]
           orders[line[0]].append(0)
       ans =  please_work(grid, orders)
       print("Total", size_x*size_y)
       print("Unallocated",ans[1])
       print("Contested", ans[0])
       for i in orders:
           print(i, orders[i][4])
       print()
except EOFError as e:
    pass