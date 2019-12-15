a, b = [int(i) for i in input().split()]

def bfs(arr, stop):
    visited = dict()
    pred = {}
    for i in range(1, stop+1):
        visited[i] = False
        pred[i] = -1

    q = []

    q.append(1)

    visited[1] = True
    count = 0
    ans = []
    while q:
        #count += 1
        s = q.pop(0)
        visited[s] = True
        for i in arr[s]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True
                pred[i] = s
                if i == stop:
                    return pred

    return pred


arr = dict()

for i in range(b):
    x , y = [int(i) for i in input().split()]

    if x not in arr:
        arr[x] = []
        arr[x].append(y)
        if y not in arr:
            arr[y] = []
            arr[y].append(x)
        else:
            arr[y].append(x)
    else:
        arr[x].append(y)
        if y not in arr:
            arr[y] = []
            arr[y].append(x)
        else:
            arr[y].append(x)

pred = bfs(arr, a)

ans = 0


while pred[a] != -1:
    ans +=1
    a = pred[a]

print(ans -1)
