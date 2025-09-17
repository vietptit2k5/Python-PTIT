t=int(input())
for _ in range(t) :
    s=input()
    a=s.split()
    n,x,m=map(float,a)
    cnt=0
    while n<m :
        n+=n*x/100
        cnt+=1
    print(cnt)
