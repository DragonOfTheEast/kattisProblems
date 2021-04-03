def is_prime(n):
    if n <= 3:
        return n > 1
    if n%2 == 0 or n %3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n% (i+2) == 0:
            return False
        i += 6
    return True
while True:
    n = int(input())

    if n == 0:
        break

    state = is_prime(n)

    num = 2*n
    found = False
    while not found:
        num += 1
        found = is_prime(num)


    print(num) if state else print(f'{num} ({n} is not prime)')
