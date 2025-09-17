n = int(input().strip())
degree = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1

if degree.count(n - 1) == 1 and degree.count(1) == n - 1:
    print("Yes")
else:
    print("No")
