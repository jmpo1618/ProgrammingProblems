import math

def isPrime(n):
    return all(n % i for i in range(2, n))

n = int(input())
for i in range(4, n // 2 + 1):
    if not isPrime(i) and not isPrime(n - i):
        print(i, n - i)
        break
