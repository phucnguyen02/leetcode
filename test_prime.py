from math import sqrt

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True


for i in range(1, 100):
    if not is_prime(3 * (2 ** i) + 2 * (3 ** i) + 1):
        print(i)
        break