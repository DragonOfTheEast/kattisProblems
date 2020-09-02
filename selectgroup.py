import sys
groups = {}
operations = {"difference", "union", "intersection"}
def operation(op, a, b, stack):
    if op == "difference":
        ans = a.difference(b)
        stack.append(ans)
    elif op == "union":
        ans = a.union(b)
        stack.append(ans)
    else:
        ans = a.intersection(b)
        stack.append(ans)
for i in sys.stdin.readlines():
    stack = []
    line = i.strip().split()
    if line[0] == 'group':
        groups[line[1]] = set(line[3:])
    else:
        line.reverse()
        for val in line:
            if val not in operations:
                stack.append(groups[val])
            else:
                a = stack.pop()
                b = stack.pop()
                operation(val,a,b,stack)
    ret = []
    for item in stack:
        for k in item:
            ret.append(k)
    print(" ".join(sorted(ret)))
