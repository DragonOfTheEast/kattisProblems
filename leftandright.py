def _solve(string):
    left,right = 1,1

    for direction in string:
        if direction == 'R':
            for i in range(right, left-1, -1):
                print(i)
            left = right + 1
        right += 1

    for i in range(right, left-1, -1):
        print(i)

n = int(input())
string = input()

_solve(string)
