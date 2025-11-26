def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

MAX = 10000
primes = [False] * (MAX + 1000)
for i in range(len(primes)):
    primes[i] = is_prime(i)

def min_steps_to_prime(x):
    if primes[x]:
        return 0
    step = 1
    while True:
        if x - step >= 2 and primes[x - step]:
            return step
        if x + step < len(primes) and primes[x + step]:
            return step
        step += 1

N = int(input())
A = list(map(int, input().split()))
total_steps = max(min_steps_to_prime(x) for x in A)
print(total_steps)