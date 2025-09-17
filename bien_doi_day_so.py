ok=1
while ok==1 :
    a,b,c,d=map(int,input().split())
    if a==0 and b==0 and c==0 and d==0 : ok=0
    else :
        cnt=0
        while a!=b or b!=c or c!=d :
            cnt+=1
            tmp1=a
            a=abs(a-b)
            b=abs(b-c)
            c=abs(c-d)
            d=abs(d-tmp1)
        print(cnt)