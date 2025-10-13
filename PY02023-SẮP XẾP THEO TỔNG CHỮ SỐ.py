def digit_sum(n):
    return sum(int(d) for d in str(n))

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort(key=lambda x: (digit_sum(x), x))
    print(*A)
