t = int(input())
for _ in range(t):
    n = int(input())
    step = 10
    while n >= step:
        n = ((n + step // 2) // step) * step
        step *= 10
    print(n)