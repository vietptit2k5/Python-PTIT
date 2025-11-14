import math

N = int(input())

limit = int(N**0.5) + 1
is_prime = [True] * (limit+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(limit**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, limit+1, i):
            is_prime[j] = False
primes = [i for i, val in enumerate(is_prime) if val]

count = 0

for p in primes:
    if p**8 <= N:
        count += 1
    else:
        break

primes_len = len(primes)
for i in range(primes_len):
    p = primes[i]
    p2 = p*p
    for j in range(i+1, primes_len):
        q = primes[j]
        q2 = q*q
        if p2*q2 <= N:
            count += 1
        else:
            break

print(count)
