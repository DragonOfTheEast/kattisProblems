from collections import defaultdict
def solve(graph):
    in_degree = defaultdict(int)
    for i in graph:
        for j in graph[i]:
            in_degree[j] += 1


    queue = []
    for i in graph:
        if in_degree[i] == 0:
            queue.append(i)

    count = 0
    top_order = []
    while queue:
        queue.sort()
        u = queue.pop(0)
        top_order.append(u)
        for i in graph[u]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
        count += 1

    if count != len(graph):
        print("cannot be ordered")
    else:
        print("\n".join(top_order))

def main():
    while True:
        n = int(input())
        if n == 0 :
            break
        graph = defaultdict(list)
        for i in range(n):
            line = input().split()
            if line[0] not in graph:
                graph[line[0]] = []
            for i in line[1:]:
                    graph[i].append(line[0])
        solve(graph)
        print()

if __name__ == '__main__':
    main()




