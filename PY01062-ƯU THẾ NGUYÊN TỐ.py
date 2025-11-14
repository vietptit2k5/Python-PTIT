def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_prime_dominant(number_str):
    prime_digits = {'2', '3', '5', '7'}
    prime_count = sum(1 for digit in number_str if digit in prime_digits)
    non_prime_count = len(number_str) - prime_count
    return is_prime(len(number_str)) and prime_count > non_prime_count

t = int(input())
for _ in range(t):
    number_str = input().strip()
    if is_prime_dominant(number_str):
        print("YES")
    else:
        print("NO")