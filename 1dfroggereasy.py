n,s,m = [int(i) for i in input().split()]
squares = [int(i) for i in input().split()]
i = 0
s -= 1
seen = [0]*n
while True:
    if s < 0:
        print('left')
        break
    if s >= n:
        print('right')
        break
    if squares[s] == m:
        print('magic')
        break
    if seen[s] == 1:
        print('cycle')
        break
    seen[s] = 1
    s += squares[s]
    i+= 1

print(i)
