from collections import deque
def check(r1,c1,new_color):
    queue = deque()
    queue.append((r1,c1))
    old_color = arr[r1][c1]

    if old_color == new_color:
        return
    while queue:
        x,y = queue.popleft()
        if x < 0 or x >= r or y < 0 or y >= c or color[x][y] != 0 or arr[x][y] != arr[r1][c1]:
            continue

        color[x][y] = new_color
        queue.append((x, y-1))
        queue.append((x,y+1))
        queue.append((x+1, y))
        queue.append((x-1, y))

r,c = [int(i) for i in input().split()]

arr = []
color = []
for _ in range(r):
    arr.append([int(i) for i in input()])
    color.append([0 for _ in range(c)])

new_color = 1
for i in range(r):
    for j in range(c):
        if color[i][j] == 0:
            new_color += 1
            check(i,j, new_color)

n = int(input())
for _ in range(n):
    r1,c1,r2,c2 = [int(i)-1 for i in input().split()]

    binary = decimal = False

    if arr[r1][c1] == arr[r2][c2] == 0 and color[r1][c1] == color[r2][c2]:
        binary = True

    elif arr[r1][c1] == arr[r2][c2] == 1 and color[r1][c1] == color[r2][c2]:
        decimal = True

    if decimal:
        print('decimal')
    elif binary:
        print('binary')
    else:
        print('neither')

