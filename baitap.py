import math
def check(n) :
    if n < 2 : return False
    if n%2==0 : return n==2
    for i in range(3,int(math.sqrt(n))+1,2) :
        if n%i==0 : return False
    return True
arr = []
id=2
arr.append(0)
arr.append(2)
arr.append(3)
valua = 5
while id < 1002 :
    if check(valua) :
        arr.append(valua)
        id+=1
    valua+=2
N,X = map(int,input().split())
id = 0
pos = []
while id <= N :
    X+=arr[id]
    pos.append(X)
    id+=1
print(*pos)

