
def print_res(graph, start, stop, pred, dist):
    bfs(graph, start, stop, pred, dist)
    path = []
    path.append(stop)
    u = stop
    while pred[u] != -1:
        path.append(pred[u])
        u = pred[u]

    for i in reversed(path):
        print(i, end=" ")
    print()
def bfs(graph, start, stop, pred, dist):
    queue = []

    visited = defaultdict(bool)

    for i in graph:
        visited[i] = False
        dist[i] = float("inf")
        pred[i] = -1
    visited[start] = True
    dist[start] = 0
    queue.append(start)
    while queue:
        u = queue.pop(0)
        for i in range(len(graph[u])):
            if visited[graph[u][i]] is False:
                visited[graph[u][i]] = True
                dist[graph[u][i]] = dist[u] + 1
                pred[graph[u][i]] = u
                queue.append(graph[u][i])
                if graph[u][i] == stop:
                    return
from collections import defaultdict
start = input()
graph = defaultdict(list)
while True:
    line = input()
    if line == "-1":
        break
    line = line.split()
    graph[line[0]] += []
    for i in line[1:]:
        graph[i].append(line[0])



stop = [j for j in graph if len(graph[j]) == 0]
stop = stop[0]
pred = defaultdict(str)
dist = defaultdict(int)
print_res(graph, start, stop, pred, dist)


