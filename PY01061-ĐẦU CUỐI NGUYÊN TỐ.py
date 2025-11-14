import math
def check(n) :
    if n < 2 : return False
    elif n%2==0 : return n==2
    else :
        for i in range(3,int(math.sqrt(n))+1,2) :
            if n%i==0 : return False
        return True

for _ in range(int(input())) :
    s = str(input())
    dau = int(s[:3])
    cuoi = int(s[len(s)-3:len(s)])
    print(dau,cuoi)
    if check(dau) and check(cuoi) : print("YES")
    else : print("NO")
