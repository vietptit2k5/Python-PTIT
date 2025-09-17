from math import sqrt
def check(n) :
    if n < 2 : return False
    if n%2==0 : return n==2
    for i in range(3,int(sqrt(n))+1,2) :
        if n%i==0 : return False
    return True
for _ in range(int(input())) :
    ss = input()
    if len(ss) <= 4 : 
        s=ss
    else : s=ss[len(ss)-4]+ss[len(ss)-3]+ss[len(ss)-2]+ss[len(ss)-1]
    n = int(s)
    print("YES") if check(n) else print("NO")
        