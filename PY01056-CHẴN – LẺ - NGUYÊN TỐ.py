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

def check_number(s):
    total = 0
    for i, ch in enumerate(s):
        digit = int(ch)
        total += digit
        if i % 2 == 0:
            if digit % 2 != 0:
                return "NO"
        else:
            if digit % 2 != 1:
                return "NO"
    if is_prime(total):
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    s = input().strip()
    print(check_number(s))