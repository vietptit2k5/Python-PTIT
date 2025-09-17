import math
def check(n) :
    if n < 2 : return False
    if n%2==0 : return n==2
    for i in range(3,(int)(math.sqrt(n))+1,2) :
        if n % i == 0 : return False
    return True
arr = []
arr.append(2)
arr.append(3)
idx=2
valua=5
while idx < 1001 :
    if check(valua) :
        arr.append(valua)
        idx+=1
    valua+=2
N,X = map(int,input().split())
pos = []
pos.append(X)
res = X
for i in range(N) :
    res+=arr[i]
    pos.append(res)
print(*pos)