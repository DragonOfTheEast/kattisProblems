import sys
def solve(string):
    result = 0
    for char in string:
        result ^= ord(char)
    return result


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    collisions = 0
    uniques = {}
    keys = []
    for i in range(n):
        string = sys.stdin.readline()
        if string in uniques:
            uniques[string] += 1
        else:
            uniques[string] = 1
            keys.append(string)
    for key1, i in enumerate(keys[:-1]):
        first_hash = solve(i)
        for key2, ii in enumerate(keys[key1+1:]):
            if first_hash == solve(ii):
                collisions += uniques[i] * uniques[ii]
    print(len(uniques), collisions)
