import sys
from io import StringIO
lines = sys.stdin.readlines()
stringio = StringIO()
for line in lines:
    a,operation,b = line.split()
    a, b = int(a), int(b)
    if operation == '+':
        c = (a + b) % 10000
    elif operation == '*':
        c = (a * b) % 10000
    else:
        c = pow(a,b,10000)
    stringio.write(f'{c}\n')

stringio.seek(0)
print(stringio.read(), end='')
