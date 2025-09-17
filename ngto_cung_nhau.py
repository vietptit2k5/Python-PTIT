import math
n,k=map(int,input().split())
r = pow(10,k)
l = pow(10,k-1)
cnt=0
arr = []
for m in range(l,r) :
    if math.gcd(m,n)==1 :
        arr.append(m)
        cnt+=1
        if cnt==10 :
            print(*arr)
            arr=[]
            cnt=0
if len(arr) > 0 : print(*arr)