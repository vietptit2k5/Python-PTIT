n= int(input())
arr = list(map(float,input().split()))
arr = sorted(arr)
max_valua=arr[0]
min_valua=arr[n-1]
tong=0
cnt=0
for i in range(n) :
    if arr[i] !=max_valua and arr[i] != min_valua :
        tong += arr[i]
        cnt+=1
print(f"{tong/cnt:.2f}")