n = int(input())
A = list(map(int,input().split()))
min_steps = float('inf')
valua = None
for tmp in A :
    steps = sum(abs(tmp-x) for x in A)
    if steps < min_steps :
        min_steps = steps
        valua = tmp
print(f"{min_steps} {valua}")