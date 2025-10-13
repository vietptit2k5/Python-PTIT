import math
n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
k = int(input())
sum_main = 0
sum_tmp = 0
for i in range(n) :
    for j in range(n) :
        if j > i :
            sum_main += A[i][j]
        elif j < i :
            sum_tmp += A[i][j]
ans = abs(sum_main-sum_tmp)
print("YES" if ans <= k else "NO")    
print(ans)