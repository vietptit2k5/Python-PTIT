n = int(input())
grid = [list(input().strip()) for _ in range(n)]

res = 0

for i in range(n):
    count = grid[i].count('C')
    res += count * (count - 1) // 2

for j in range(n):
    count = 0
    for i in range(n):
        if grid[i][j] == 'C':
            count += 1
    res += count * (count - 1) // 2

print(res)
