MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    M = 0
    powN = 1
    k = K
    while k > 0:
        if k & 1:
            M = (M + powN) % MOD
        powN = (powN * N) % MOD
        k >>= 1
    print(M)
