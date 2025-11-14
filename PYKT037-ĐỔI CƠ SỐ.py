def convert(N, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ''
    while N > 0:
        res = digits[N % b] + res
        N //= b
    return res or '0'

for _ in range(int(input())):
    N, b = map(int, input().split())
    print(convert(N, b))
