import math
n =int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
for i in range(0,n-1,1) :
    for j in range(i+1,n,1) :
        if math.gcd(arr[i],arr[j])==1 : print(arr[i],arr[j])