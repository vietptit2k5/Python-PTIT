def is_prime_length(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_digits = {'2','3','5','7'}

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if not is_prime_length(n):
        print("NO")
        continue
    cnt_prime = sum(1 for c in s if c in prime_digits)
    cnt_nonprime = n - cnt_prime
    print("YES" if cnt_prime > cnt_nonprime else "NO")
