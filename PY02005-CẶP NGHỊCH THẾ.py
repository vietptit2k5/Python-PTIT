n = int(input())
arr = list(map(int,input().split()))
cnt=0
for i in range(0,n-1,1) :
    for j in range(i+1,n,1) :
        if arr[i] > arr[j] : cnt+=1
print(cnt)