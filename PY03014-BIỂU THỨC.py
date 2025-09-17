MAX = 2000000
spf = [0] * (MAX + 1)

def sieve():
    for i in range(2, MAX + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= MAX:
                for j in range(i * i, MAX + 1, i):
                    if spf[j] == 0:
                        spf[j] = i

def sum_prime_factors(n):
    total = 0
    while n > 1:
        total += spf[n]
        n //= spf[n]
    return total

def main():
    import sys
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    nums = list(map(int, input_data[1:]))

    sieve()
    ans = 0
    for x in nums:
        ans += sum_prime_factors(x)
    print(ans)

if __name__ == "__main__":
    main()
