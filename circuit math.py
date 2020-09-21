values = dict()

def mult(a,b):
    if a == 'T' and b == 'T':
        return 'T'
    else:
        return 'F'

def add(a,b):
    if a == 'F' and b == 'F':
        return 'F'
    else:
        return 'T'

def neg(a):
    if a == 'F':
        return 'T'
    return 'F'
n = int(input())

arr = dict()
list1 = input().split()

for i in range(n):
    arr[chr(65+ i)] = list1[i]



stack = []
for i in input():
    if i != ' ':
        if i == "*":
            temp = mult(stack[-1], stack[-2])
            stack.pop()
            stack.pop()
            stack.append(temp)
        elif i == '+':
            temp = add(stack[-1], stack[-2])
            stack.pop()
            stack.pop()
            stack.append(temp)
        elif i == '-':
            temp = neg(stack[-1])
            stack.pop()
            stack.append(temp)
        else:
            stack.append(arr[i])



print(stack[0])