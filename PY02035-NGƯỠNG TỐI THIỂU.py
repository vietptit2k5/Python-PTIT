s = input().strip()
k = int(input())

A = []
for i in range(0, len(s) - 1, 2):
    A.append(int(s[i:i+2]))

count = {}
for x in A:
    count[x] = count.get(x, 0) + 1

res = []
for x, c in count.items():
    if c >= k:
        res.append((x, c))

if not res:
    print("NOT FOUND")
else:
    res.sort() 
    for x, c in res:
        print(x, c)
