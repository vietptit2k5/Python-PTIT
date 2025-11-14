def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_pos = [False] * 501
for i in range(2, 501):
    prime_pos[i] = is_prime(i)

prime_digits = {'2', '3', '5', '7'}

t = int(input())
for _ in range(t):
    s = input().strip()
    ok = True
    for i in range(len(s)): 
        digit = s[i]
        if prime_pos[i]:
            if digit not in prime_digits:
                ok = False
                break
        else:
            if digit in prime_digits:
                ok = False
                break
    print("YES" if ok else "NO")