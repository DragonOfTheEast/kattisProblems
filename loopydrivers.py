import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
def solve(visited, stack, i):
    visited[i] = True
    for j in graph[i]:
        if visited[j] is False:
            solve(visited, stack, j)
    stack.append(i)

def DFS(graph, i, visited, ans):
    visited[i] = True
    ans.append(i)
    for i in graph[i]:
        if visited[i] is False:
            DFS(graph, i, visited, ans)
def find_diff_parts(graph, graph_reverse):
    stack = []
    visited = {}
    for i in graph:
        visited[i] =False

    for i in graph:
        if visited[i] is False:
            solve(visited, stack, i)

    for i in graph:
        visited[i] =False
    ans = []
    while stack:
        u = stack.pop()
        temp = []
        if visited[u] is False:
           DFS(graph_reverse, u, visited, temp)
           ans.append(temp)    
    return ans


graph = defaultdict(list)
graph_reverse = defaultdict(list)
for line in sys.stdin.readlines():
    a,b = line.strip().split()
    graph[a].append(b)
    graph_reverse[b].append(a)

    if b not in graph:
        graph[b] = []
    if a not in graph_reverse:
        graph_reverse[a] = []

val = list(graph_reverse.keys())
# for i in val:
#     for j in graph_reverse[i]:
#         if j not in graph_reverse:
#             graph_reverse[j] = []

ans  = find_diff_parts(graph, graph_reverse)
size_1 = []
size_not_1 = []
for i,j in enumerate(ans):
    if len(j) == 1:
        size_1.append(j)
    elif len(j) > 1:
        size_not_1.append(j)

list.sort(size_1, key= lambda x:x[0])

for i in size_not_1:
    i.sort()
list.sort(size_not_1, key=lambda x:x[0])

for i in size_not_1:
    print("okay " + " ".join(i))
if size_1:
    print("avoid ", end="")
    for i in size_1:
        print(" ".join(i), end = " ")
    print()
