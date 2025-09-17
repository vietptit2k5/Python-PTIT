
LIMIT = 10**18
arr = []
a=1
while a <= LIMIT :
    b=a
    while b <= LIMIT :
        c=b
        while c <= LIMIT :
            arr.append(c)
            c*=5
        b*=3
    a*=2
arr = sorted(arr)
pos = {v : i+1 for i,v in enumerate(arr)}
for t in range(int(input())) :
    n = int(input())
    if n in pos :
        print(pos[n])
    else : print("Not in sequence")