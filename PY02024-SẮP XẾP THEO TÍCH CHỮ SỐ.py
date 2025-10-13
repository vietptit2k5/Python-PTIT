def tich_digit(n) :
    tmp=1
    for x in str(n) :
        tmp *= int(x)
    return tmp
for _ in range(int(input())) :
    n = int(input())
    A = list(map(int,input().split()))
    A.sort(key=lambda x : (tich_digit(x),x))
    print(*A)