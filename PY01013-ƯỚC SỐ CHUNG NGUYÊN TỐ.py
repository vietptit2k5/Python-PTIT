from math import gcd
def check(n) :
    if n<2 : return False
    if n%2==0 : return n==2
    d=3
    while d*d <= n :
        if n%d==0 : return False
        d+=2
    return True
def tong_chu_so(a,b) :
    x = gcd(a,b)
    cnt=0
    while x > 0:
        cnt+=x%10
        x//=10
    return cnt
if __name__ == '__main__' :
    t = int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        print("YES") if check(tong_chu_so(a,b)) else print("NO")