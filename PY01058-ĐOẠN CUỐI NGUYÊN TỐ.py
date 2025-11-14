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
    ss = s[len(s)-4:len(s)]

    n = int(ss)
    print("YES" if check(n) else "NO")