a,K,N = map(int,input().split())
idx = ((a+K)//K)
arr = []
b=idx*K-a
while b <= N-a :
    arr.append(b)
    idx+=1
    b=idx*K-a   
if len(arr) > 0 :
    print(*arr)
else : print(-1)