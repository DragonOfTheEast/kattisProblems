from collections import deque
def solve(graph, s, n):
    dist = [float('inf')]*n
    dist[s] = 0
    queue = deque()
    queue.append(s)
    while queue:
        current = queue.pop()
        for j in graph[current]:
            node, weight = j[0], j[1]
            if dist[node] > dist[current] + weight:
                dist[node] = dist[current] + weight
                queue.append(node)
    return dist

while True:
    n,m,q,s = [int(i) for i in input().split()]
    if n == m == q == s == 0:
        break
    graph = [[] for i in range(n+1)]


    for i in range(m):
        u, v, w = [int(i) for i in input().split()]
        graph[u].append([v, w])
    ans = solve(graph, s, n)
    for i in range(q):
        v = int(input())
        if isinf(ans[v]):
            print("impossible")
        else:
            print(ans[v])
    print()
