import math
def check(n,m) :
    if math.gcd(n,m) == 1 :
        return True
    return False
n = int(input())
A = list(map(int,input().split()))
A.sort()
for i in range(len(A)-1) :
    for j in range(i+1,len(A)) :
        if(check(A[i],A[j])) :
            s = str(A[i])+" "+str(A[j])
            print(s)