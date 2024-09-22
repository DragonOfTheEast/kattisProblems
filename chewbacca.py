def _solve(i,j,k):
    levels = 0
    while i != j:
        if i > j:
            i,j = j,i
        j = (j-1)//k
        levels += 1
    return levels
if '__main__' == __name__:
    n, k, q = [int(i) for i in input().split()]
    for _ in range(q):
        i, j = (int(i)-1 for i in input().split())
        ans = _solve(i,j,k)
        print(ans)
