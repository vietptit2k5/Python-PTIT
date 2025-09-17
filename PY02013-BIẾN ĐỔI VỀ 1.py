ok=1
while ok==1 :
    n = int(input())
    if n==0 : ok=0
    else :
        cnt = 1
        while n !=1 :
            cnt+=1
            if n%2==0 : n/=2
            else : n = n*3+1
        print(cnt)