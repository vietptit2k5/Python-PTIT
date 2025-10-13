import math
def check(n) :
    if n<2 : return False
    if n%2==0 : return n==2
    for i in range(3,int(math.sqrt(n))+1,2) :
        if n%i==0 : return False
    return True
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(1 if check(A[i][j]) else 0, end=' ')
    print()
