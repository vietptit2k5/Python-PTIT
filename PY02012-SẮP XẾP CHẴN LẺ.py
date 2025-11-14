n = int(input())
A = []
while len(A) < n:
    A += list(map(int, input().split()))

even = sorted([x for x in A if x % 2 == 0])
odd = sorted([x for x in A if x % 2 == 1], reverse=True)

res = []
e_idx, o_idx = 0, 0
for x in A:
    if x % 2 == 0:
        res.append(even[e_idx])
        e_idx += 1
    else:
        res.append(odd[o_idx])
        o_idx += 1

print(*res)
